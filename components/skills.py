from utils import config as cfg


def render(st):
    st.markdown('<div class="section" id="skills">', unsafe_allow_html=True)
    st.markdown('<div class="section-kicker">Skills</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">What I actually work with</h2>', unsafe_allow_html=True)

    categories = list(cfg.SKILLS.items())
    cols = st.columns(3, gap="medium")

    for i, (category, skills) in enumerate(categories):
        with cols[i % 3]:
            badge_parts = []
            for name, note in skills:
                note_html = f'<span class="note">{note}</span>' if note else ""
                badge_parts.append(f'<span class="skill-badge">{name}{note_html}</span>')
            badges = "".join(badge_parts)
            st.markdown(
                f"""
                <div class="glass-card" style="margin-bottom:1.2rem;">
                    <div class="skill-category-title">{category}</div>
                    <div class="badge-row">{badges}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown('</div>', unsafe_allow_html=True)
