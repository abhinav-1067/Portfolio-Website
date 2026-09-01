import streamlit as st

from utils import config as cfg
from utils.styles import inject_css
from components import navbar, hero, about, skills, projects, journey, github_panel, contact

st.set_page_config(
    page_title=cfg.PAGE_TITLE,
    page_icon=cfg.PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)

inject_css(st)

navbar.render(st)
hero.render(st)
about.render(st)
skills.render(st)
projects.render(st)
journey.render(st)
github_panel.render(st)
contact.render(st)

st.markdown(
    f'<div class="pf-footer">Built with Python &amp; Streamlit. '
    f'&copy; {cfg.NAME}.</div>',
    unsafe_allow_html=True,
)
