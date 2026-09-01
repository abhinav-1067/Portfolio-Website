from utils import config as cfg


def render(st):
    st.markdown(
        f"""
        <div class="hero" id="home">
            <div class="hero-grid-bg"></div>
            <div class="hero-content">
                <div class="hero-eyebrow"><span class="dot"></span>Open to internships</div>
                <h1 class="hero-title">{cfg.HEADLINE}</h1>
                <p class="hero-sub">{cfg.SUBHEADLINE}</p>
                <div class="hero-ctas">
                    <a class="btn btn-primary" href="#{cfg.PRIMARY_CTA_TARGET}">{cfg.PRIMARY_CTA_LABEL}</a>
                    <a class="btn btn-secondary" href="#{cfg.SECONDARY_CTA_TARGET}">{cfg.SECONDARY_CTA_LABEL}</a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
