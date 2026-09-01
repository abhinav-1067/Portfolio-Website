from utils import config as cfg


def render(st):
    st.markdown('<div class="section" id="github">', unsafe_allow_html=True)
    st.markdown('<div class="section-kicker">Developer</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">On GitHub</h2>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="glass-card">
            <p class="muted" style="margin-bottom:1.2rem;">
                Live repository and contribution data loads from GitHub's public API
                below. If it doesn't load (e.g. no network access, or rate limits),
                visit the profile directly.
            </p>
            <a class="btn btn-secondary" href="{cfg.GITHUB_URL}" target="_blank">
                @{cfg.GITHUB_USERNAME} on GitHub
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    stats = _fetch_github_stats(cfg.GITHUB_USERNAME)
    if stats:
        cols = st.columns(3)
        labels = [("public_repos", "Public repos"), ("followers", "Followers"), ("following", "Following")]
        for col, (key, label) in zip(cols, labels):
            with col:
                st.markdown(
                    f'<div class="glass-card gh-stat" style="margin-top:1rem;">'
                    f'<div class="num">{stats.get(key, "—")}</div>'
                    f'<div class="label">{label}</div></div>',
                    unsafe_allow_html=True,
                )

    st.markdown('</div>', unsafe_allow_html=True)


def _fetch_github_stats(username):
    """Best-effort fetch of public GitHub stats. Returns None on any failure
    (no network, rate limit, bad username) — the UI degrades gracefully."""
    try:
        import streamlit as st_cache_mod  # local import so file works without streamlit at import time in tests
        return _cached_fetch(username)
    except Exception:
        return None


def _cached_fetch(username):
    import streamlit as st

    @st.cache_data(ttl=3600, show_spinner=False)
    def _fetch(u):
        import requests
        resp = requests.get(f"https://api.github.com/users/{u}", timeout=4)
        if resp.status_code != 200:
            return None
        data = resp.json()
        return {
            "public_repos": data.get("public_repos"),
            "followers": data.get("followers"),
            "following": data.get("following"),
        }

    try:
        return _fetch(username)
    except Exception:
        return None
