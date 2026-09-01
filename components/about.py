from utils import config as cfg


def render(st):
    st.markdown('<div class="section" id="about">', unsafe_allow_html=True)
    st.markdown('<div class="section-kicker">About</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Currently building the fundamentals, on purpose</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1.6], gap="large")
    with col1:
        st.markdown(
            f"""
            <div class="glass-card">
                <p class="muted" style="margin-bottom:0.6rem;">Status</p>
                <p style="font-weight:700; margin-bottom:1rem;">1st-year BTech CS student</p>
                <p class="muted" style="margin-bottom:0.6rem;">Direction</p>
                <p style="font-weight:700; margin-bottom:1rem;">Aspiring Data Scientist</p>
                <p class="muted" style="margin-bottom:0.6rem;">Focus right now</p>
                <p style="font-weight:700;">Python, data analysis, Flask, DSA</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        for para in cfg.ABOUT_PARAGRAPHS:
            st.markdown(f'<p class="muted" style="font-size:1.02rem;">{para}</p>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
