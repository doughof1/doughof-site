# doughof.com — standalone rebuild

A dependency-free static rebuild of Doug Hof's portfolio. No Squarespace runtime, database, CMS, npm, or server is required.

## Build

```bash
python3 build.py
```

The deployable site is generated in `dist/`.

## Preview locally

```bash
cd dist
python3 -m http.server 8080
```

Open `http://localhost:8080`.

## Deploy to Cloudflare Pages

This site can be deployed as a static folder. Either upload `dist/` directly or connect the repository and use:

- Build command: `python3 build.py`
- Build output directory: `dist`

Then add `doughof.com` as the custom domain.

## Editing content

Project content lives in the `projects` list near the top of `build.py`. Shared layout and page copy are also generated there. Styling is in `public/assets/site.css`.

## Migration note

The included project images are locally copied into this repository from the current public Squarespace site, so the generated site does not hot-link those assets from Squarespace.
