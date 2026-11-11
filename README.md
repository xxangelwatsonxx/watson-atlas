# Watson Atlas website

Marketing website for Watson Atlas, UK housing software (Resonest and SiteOps).

- `build.py` and `subpages.py` generate the site. Run `python3 build.py` to rebuild.
- Output: `index.html`, `awaabs-law/`, `help/`, mirrored into `dist/` for publishing.
- `drafts/` holds alternative design concepts; `variants/` holds colour scheme variants.
- `relay/` holds an optional serverless relay for the help chat. API keys are never stored in this repo.
- See `PUBLISH-NOTES.md` for publishing details.
