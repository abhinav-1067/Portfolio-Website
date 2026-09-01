from utils import config as cfg

STATUS_LABEL = {"done": "Done", "current": "In progress", "upcoming": "Up next"}


def render(st):
    st.markdown('<div class="section" id="journey">', unsafe_allow_html=True)
    st.markdown('<div class="section-kicker">Learning journey</div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">The roadmap I\'m working through</h2>', unsafe_allow_html=True)

    items_html = ""
    for item in cfg.JOURNEY:
        status = item["status"]
        items_html += (
            f'<div class="timeline-item {status}">'
            f'<span class="timeline-label">{item["label"]}</span>'
            f'<span class="timeline-status">{STATUS_LABEL[status]}</span>'
            f'</div>'
        )

    st.markdown(f'<div class="glass-card"><div class="timeline">{items_html}</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
