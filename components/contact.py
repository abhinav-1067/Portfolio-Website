from utils import config as cfg


def render(st):
    st.markdown('<div class="section" id="contact">', unsafe_allow_html=True)
    st.markdown('<div class="section-kicker">Contact</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Let\'s connect</h2>', unsafe_allow_html=True)

    links_html = ""
    if cfg.EMAIL:
        links_html += f'<a class="btn btn-primary" href="mailto:{cfg.EMAIL}">Email me</a>'
    else:
        links_html += '<span class="link-placeholder">Email — add in config.py</span>'

    links_html += f'<a class="btn btn-secondary" href="{cfg.GITHUB_URL}" target="_blank">View GitHub</a>'

    if cfg.LINKEDIN_URL:
        links_html += f'<a class="btn btn-secondary" href="{cfg.LINKEDIN_URL}" target="_blank">LinkedIn</a>'
    else:
        links_html += '<span class="link-placeholder">LinkedIn — add in config.py</span>'

    st.markdown(
        f"""
        <div class="glass-card">
            <p class="muted">
                Open to internship opportunities, collaboration on small
                projects, or just talking data and Python.
            </p>
            <div class="contact-links">{links_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    _render_resume_button(st)
    st.markdown('</div>', unsafe_allow_html=True)


def _render_resume_button(st):
    import os

    if os.path.exists(cfg.RESUME_PATH):
        with open(cfg.RESUME_PATH, "rb") as f:
            st.download_button(
                "Download resume",
                data=f.read(),
                file_name="resume.pdf",
                mime="application/pdf",
            )
    else:
        st.markdown(
            '<span class="link-placeholder">Resume PDF — add file at '
            f'{cfg.RESUME_PATH}</span>',
            unsafe_allow_html=True,
        )
