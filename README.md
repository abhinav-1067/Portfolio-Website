# Portfolio — Streamlit + Python

A single-page, dark-themed developer/data-science portfolio built entirely
with Streamlit and Python. All content is driven from one config file, so
you rarely need to touch the components themselves.

## Project structure

```
portfolio/
├── app.py                  # entry point — wires everything together
├── requirements.txt
├── utils/
│   ├── config.py           # ALL editable content lives here
│   └── styles.py           # design system (CSS) — colors, type, layout
├── components/
│   ├── navbar.py
│   ├── hero.py
│   ├── about.py
│   ├── skills.py
│   ├── projects.py
│   ├── journey.py
│   ├── github_panel.py     # live GitHub stats via public API (graceful fallback)
│   └── contact.py
└── assets/
    ├── images/              # add profile.png here
    ├── icons/
    ├── animations/
    └── resume.pdf           # add your resume PDF here (enables download button)
```

## 1. Setup

Requires Python 3.9+.

```bash
cd portfolio
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Run locally

```bash
streamlit run app.py
```

This opens the site at `http://localhost:8501`.

## 3. Add your real content

Open `utils/config.py` and fill in the values marked `PLACEHOLDER`:

| What | Variable | Notes |
|---|---|---|
| Profile photo | `PROFILE_IMAGE` | put the file in `assets/images/`, then add an `st.image(cfg.PROFILE_IMAGE)` call in `components/hero.py` where you'd like it to appear |
| Resume | `RESUME_PATH` | drop a PDF at `assets/resume.pdf` — the Contact section auto-detects it and shows a real download button |
| Email | `EMAIL` | shown as a `mailto:` link in Contact |
| LinkedIn | `LINKEDIN_URL` | shown as a button in Contact |
| Project repo links | `PROJECTS[i]["github_url"]` | until filled in, the UI shows an honest "add link" placeholder instead of a dead button |

Skills, the learning-journey timeline, and project descriptions are also all
in `utils/config.py` — edit the lists/dicts directly.

## 4. Deploy on Streamlit Community Cloud

1. Push this project to a public (or private, with Cloud access) GitHub repo.
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app**, pick the repo/branch, and set the main file path to `app.py`.
4. Deploy. Streamlit Cloud installs `requirements.txt` automatically.
5. Any time you push to the connected branch, the deployed app redeploys.

## Notes on the GitHub panel

`components/github_panel.py` calls the public GitHub REST API
(`api.github.com/users/<username>`) for repo/follower counts, cached for an
hour with `st.cache_data`. If the request fails for any reason (offline,
rate-limited, username typo) it fails silently and just shows the profile
link — it never fabricates numbers.

## Design notes

- Dark navy base (`#0B1120`) with a warm amber accent (`#E8A33D`) and a muted
  cyan secondary (`#5FA8D3`) — chosen to feel like a data-notebook rather
  than a generic dark SaaS template.
- Headings use **Newsreader** (serif) for character; body text uses
  **Manrope**; tech badges use **JetBrains Mono**, sparingly.
- The hero background is a slowly drifting dot/line grid (data-grid motif),
  not particle confetti.
- Layout is left-aligned throughout, with one signature animated element
  (the hero grid) rather than motion on every card.
