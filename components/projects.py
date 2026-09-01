from utils import config as cfg


def render(st):
    st.markdown('<div class="section" id="projects">', unsafe_allow_html=True)
    st.markdown('<div class="section-kicker">Projects</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Things I\'ve actually built</h2>', unsafe_allow_html=True)

    projects = cfg.PROJECTS
    for row_start in range(0, len(projects), 2):
        row = projects[row_start:row_start + 2]
        cols = st.columns(len(row), gap="medium")
        for col, project in zip(cols, row):
            with col:
                _render_card(st, project)

    st.markdown('</div>', unsafe_allow_html=True)


def _render_card(st, project):
    tech_pills = "".join(f'<span class="tech-pill">{t}</span>' for t in project["tech"])
    features = "".join(f"<li>{f}</li>" for f in project["features"])

    link_html = ""
    if project.get("github_url"):
        link_html += f'<a class="btn btn-secondary" style="margin-top:0.9rem;" href="{project["github_url"]}" target="_blank">View code</a>'
    else:
        link_html += '<div class="link-placeholder">Repo link — add in config.py</div>'

    st.markdown(
        f"""
        <div class="glass-card" style="margin-bottom:1.2rem;">
            <div class="project-name">{project['name']}</div>
            <p class="muted">{project['description']}</p>
            <div class="project-problem">{project['problem']}</div>
            <ul class="muted" style="margin:0 0 0 1.1rem; padding:0;">{features}</ul>
            <div class="tech-row">{tech_pills}</div>
            {link_html}
        </div>
        """,
        unsafe_allow_html=True,
    )
