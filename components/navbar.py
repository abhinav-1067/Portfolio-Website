from utils import config as cfg

NAV_LINKS = [
    ("About", "about"),
    ("Skills", "skills"),
    ("Projects", "projects"),
    ("Journey", "journey"),
    ("GitHub", "github"),
    ("Contact", "contact"),
]


def render(st):
    links = "".join(f'<a href="#{anchor}">{label}</a>' for label, anchor in NAV_LINKS)
    st.markdown(
        f"""
        <div class="portfolio-nav">
            <a class="brand" href="#home">{cfg.NAME}</a>
            <div class="links">{links}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
