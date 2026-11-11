/**
 * Optional standalone relay for the Watson Atlas help chat.
 * The live site currently uses a here.now proxy route (see PUBLISH-NOTES.md)
 * so the xAI key never reaches the browser. Deploy this worker if you need
 * server-side enforcement of the system prompt and body limits.
 *
 * Runtime: Cloudflare Workers (or any fetch-compatible worker).
 * Secrets: XAI_API_KEY
 * Optional env: ALLOWED_ORIGIN (default https://present-bridge-9s3b.here.now)
 */
const DEFAULT_ORIGIN = "https://present-bridge-9s3b.here.now";
const MODEL = "grok-4.3";
const MAX_TOKENS = 400;
const MAX_MSG = 1200;
const MAX_TURNS = 12;
const MAX_BODY = 80_000;
const RATE_WINDOW_MS = 60 * 60 * 1000;
const RATE_MAX = 30;

const SYSTEM = `You are Joe, a friendly helper on the Watson Atlas website. Watson Atlas is UK housing software from the team behind Rowe AI, a Scottish software company. You help visitors work out what they need and what help they want.

Be warm, concise and professional, in British English. Do not use en dashes or em dashes. Use commas, colons or short sentences instead.

What Watson Atlas offers:
- Resonest is a privacy-first digital twin, built for Awaab's Law. It uses existing property and weather data, with no in-home sensors or tenant monitoring. It helps social landlords get ahead of damp, mould and cold homes by showing which homes will struggle first in winter and why, with clear action lists and deadlines, and an audit trail of what was done.
- SiteOps is a housing compliance platform for capturing inspections on site and turning them into consistent, branded PDF reports. It includes a property register keyed on UPRN, a no-code form and report designer, job planning, and a mobile app for on-site capture. A repairs and maintenance module is on the roadmap.
- Around those products, Watson Atlas also offers building safety and cladding reporting, a field and surveyor app, property data, integrations with a landlord's existing housing system, and bespoke housing software.
- Rowe AI holds Cyber Essentials certification.

Rules you must follow:
- Never name clients or customer organisations.
- Never give legal advice. If asked about legal duties under Awaab's Law, give a short plain-English outline and point people to the official UK government guidance at https://www.gov.uk/government/collections/awaabs-law-in-the-social-rented-sector and to the explainer on this site at /awaabs-law/.
- Never invent prices, contracts, timescales for our work, or promises of legal compliance. Using Resonest does not, on its own, mean a landlord has complied with Awaab's Law.
- If you are unsure, say so.
- When it is natural, nudge the visitor to leave their details or start a conversation via the contact section on this page, or by emailing info@rowe.ai.

Keep answers short: a few short paragraphs or a short list, unless the visitor asks for more detail.`;

const hits = new Map();

function allowedOrigin(env, origin) {
  const allow = env.ALLOWED_ORIGIN || DEFAULT_ORIGIN;
  return origin === allow;
}

function cors(origin) {
  return {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Accept",
    "Access-Control-Max-Age": "86400",
    Vary: "Origin",
  };
}

function rateKey(request) {
  return request.headers.get("CF-Connecting-IP") || request.headers.get("x-forwarded-for") || "unknown";
}

function limited(ip) {
  const now = Date.now();
  const row = hits.get(ip) || [];
  const fresh = row.filter((t) => now - t < RATE_WINDOW_MS);
  if (fresh.length >= RATE_MAX) {
    hits.set(ip, fresh);
    return true;
  }
  fresh.push(now);
  hits.set(ip, fresh);
  return false;
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    const allow = env.ALLOWED_ORIGIN || DEFAULT_ORIGIN;
    if (request.method === "OPTIONS") {
      if (!allowedOrigin(env, origin)) return new Response(null, { status: 403 });
      return new Response(null, { status: 204, headers: cors(origin) });
    }
    if (request.method !== "POST") {
      return new Response("Method not allowed", { status: 405, headers: cors(allow) });
    }
    if (!allowedOrigin(env, origin)) {
      return new Response("Forbidden", { status: 403 });
    }
    if (limited(rateKey(request))) {
      return new Response(JSON.stringify({ error: "rate_limited" }), {
        status: 429,
        headers: { ...cors(origin), "Content-Type": "application/json" },
      });
    }
    const key = env.XAI_API_KEY;
    if (!key) {
      return new Response(JSON.stringify({ error: "not_configured" }), {
        status: 501,
        headers: { ...cors(origin), "Content-Type": "application/json" },
      });
    }
    let body;
    try {
      const raw = await request.text();
      if (raw.length > MAX_BODY) throw new Error("too big");
      body = JSON.parse(raw);
    } catch {
      return new Response(JSON.stringify({ error: "bad_request" }), {
        status: 400,
        headers: { ...cors(origin), "Content-Type": "application/json" },
      });
    }
    const incoming = Array.isArray(body.messages) ? body.messages : [];
    const cleaned = [];
    for (const m of incoming) {
      if (!m || (m.role !== "user" && m.role !== "assistant")) continue;
      const content = String(m.content || "").slice(0, MAX_MSG);
      if (!content) continue;
      cleaned.push({ role: m.role, content });
    }
    const users = cleaned.filter((m) => m.role === "user");
    if (!users.length) {
      return new Response(JSON.stringify({ error: "empty" }), {
        status: 400,
        headers: { ...cors(origin), "Content-Type": "application/json" },
      });
    }
    if (users.length > MAX_TURNS) cleaned.splice(0, cleaned.length - MAX_TURNS * 2);
    const payload = {
      model: MODEL,
      messages: [{ role: "system", content: SYSTEM }, ...cleaned],
      max_tokens: MAX_TOKENS,
      temperature: 0.6,
    };
    const upstream = await fetch("https://api.x.ai/v1/chat/completions", {
      method: "POST",
      headers: {
        Authorization: "Bearer " + key,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });
    const text = await upstream.text();
    return new Response(text, {
      status: upstream.status,
      headers: { ...cors(origin), "Content-Type": "application/json" },
    });
  },
};
