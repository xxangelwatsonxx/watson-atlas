# Watson Atlas help chat relay

The live site chat on `/help/` calls `POST /api/chat` on the same here.now origin.

## What is hosted today

here.now does not run backend code, but it does support proxy routes. The published file `.herenow/proxy.json` forwards `POST /api/chat` to `https://api.x.ai/v1/chat/completions` and injects the API key server-side from the here.now account variable `XAI_API_KEY`. Browser requests are same-origin only. The route is limited to 30 requests per hour per IP.

The key must never be placed in HTML, JavaScript, or any file in `dist/` or Drive.

## How to rotate the key

1. Put the new key in the box environment as `XAI_API_KEY`, or have it ready to paste only into the API call below.
2. Update the here.now account variable (values are never returned later):

```
PUT https://here.now/api/v1/me/variables/XAI_API_KEY
Authorization: Bearer <here.now API key>
Content-Type: application/json

{"value":"<new xAI key>","allowedUpstreams":["api.x.ai"]}
```

3. No republish is required for a key rotation. Republish is required if you change `.herenow/proxy.json`.

To delete the variable: `DELETE https://here.now/api/v1/me/variables/XAI_API_KEY`.

## Optional standalone worker

`worker.js` is a Cloudflare Worker that enforces the system prompt, message length, turn cap, max tokens, rate limit, and CORS (locked to `https://present-bridge-9s3b.here.now`) on the server. Deploy it only if you need that extra enforcement, then point the here.now proxy upstream at the worker (and pin `allowedUpstreams` to the worker host) or change the page to call the worker directly.

It was not deployed from this box, because no Cloudflare (or Vercel / Deno) account session was available to use headlessly.
