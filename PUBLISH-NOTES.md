# Watson Atlas website: publishing notes
- Live: https://present-bridge-9s3b.here.now/ (slug present-bridge-9s3b, free plan)
- Password: kept privately, not in this repository
- Rebuild: python3 build.py
  (writes Classic Navy to index.html, awaabs-law/index.html, help/index.html, copies favicons, and mirrors that tree plus .herenow/proxy.json into dist/)
- Republish: PATH=/tmp/shim:$PATH bash /workspace/here-now-publish.sh dist --slug present-bridge-9s3b --client cursor
  (/tmp/shim/file is a stub because `file` isn't installed on the box)
- Make public: PATCH /api/v1/publish/present-bridge-9s3b/metadata {"password": null}  (or here.now dashboard > site > access > anyone with link)
  and remove <meta name="robots" content="noindex, nofollow"> from build.py before republishing.
- Custom name: here.now gave the site the label "watson-atlas-uk-housing-software". A vanity URL ({label}.{name}.here.now) needs a paid plan. "watson-atlas" is available as a vanity subdomain name. A custom domain (watsonatlas.com) can be connected via POST /api/v1/domains.

- Pages: / (home), /awaabs-law/ (Awaab's Law explainer), /help/ (How can we help? chat). All sit behind the same site password.

- Landing: visitors should arrive on the home page. The here.now password gate has no setting for a post-unlock path; after a correct password it 303-redirects back to the URL that was requested. A sessionStorage flag (`wa-atlas-entry`) is set when Home loads and when any same-origin link is clicked. `/awaabs-law/` and `/help/` only redirect to `/` when that flag is missing in this tab (a fresh entry, including after unlocking the password on a subpage). If the flag is present, or sessionStorage is blocked, they never redirect, so menu navigation works even when the referrer is stripped. On a fresh Home load (no flag yet), any `#hash` is stripped, history.scrollRestoration is set to 'manual', and the page starts at the top. Later in-site links to `/#section` keep their hash.
- Help chat: the browser posts to same-origin `/api/chat`. here.now proxy route in `.herenow/proxy.json` forwards that POST to https://api.x.ai/v1/chat/completions and injects account variable `XAI_API_KEY` server-side (allowed upstream: api.x.ai). Rate limit 30/hour/ip. The key must never be written into HTML, JS, dist, or Drive.
- Rotate the xAI key: PUT /api/v1/me/variables/XAI_API_KEY with {"value":"<new key>","allowedUpstreams":["api.x.ai"]}. No republish needed for a key-only change. See /workspace/website/relay/README.md.
- After a publish that includes `.herenow/proxy.json`, check the finalize response `warnings` array. An invalid manifest goes live with proxy routes silently disabled.
