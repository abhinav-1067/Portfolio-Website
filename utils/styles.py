"""
Design system for the portfolio: one CSS string, injected once from app.py.

Token summary
-------------
Color:
    --bg:        #0B1120  deep navy-black base
    --surface:   #131B2E  card / panel surface
    --surface-2: #1B2540  raised surface (hover, nested cards)
    --border:    #26314E  hairline borders on dark
    --text:      #E8ECF4  primary text
    --text-muted:#8B96AC  secondary text
    --accent:    #E8A33D  warm amber — "highlighted cell" accent
    --accent-2:  #5FA8D3  muted cyan-blue — secondary/data accent
    --good:      #6FCF97  status: done
    --warn:      #E8A33D  status: current
Type:
    Display/headline: 'Newsreader' (serif)
    Body/UI:           'Manrope' (sans)
    Code/badges:        'JetBrains Mono' (used sparingly, tech badges only)
Layout:
    Left-aligned content, generous vertical rhythm, a faint dot-grid
    background evoking a data notebook rather than generic particles.
"""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,500&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --bg: #0B1120;
    --surface: #131B2E;
    --surface-2: #1B2540;
    --border: #26314E;
    --text: #E8ECF4;
    --text-muted: #8B96AC;
    --accent: #E8A33D;
    --accent-2: #5FA8D3;
    --good: #6FCF97;
    --warn: #E8A33D;
}

@media (prefers-reduced-motion: reduce) {
    * { animation: none !important; transition: none !important; }
}

html, body, [class*="css"] {
    font-family: 'Manrope', -apple-system, sans-serif;
    color: var(--text);
}

.stApp {
    background:
        radial-gradient(circle at 1px 1px, rgba(232,163,61,0.07) 1px, transparent 0) 0 0 / 28px 28px,
        var(--bg);
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 4rem; max-width: 1100px; }

h1, h2, h3, .display {
    font-family: 'Newsreader', Georgia, serif;
    font-weight: 500;
    letter-spacing: -0.01em;
    color: var(--text);
}

p, li, span, div { line-height: 1.65; }

.section {
    padding: 4.5rem 0 1rem 0;
    border-top: 1px solid var(--border);
    scroll-margin-top: 5rem;
}
.section:first-of-type { border-top: none; }

.section-kicker {
    color: var(--accent-2);
    font-size: 0.95rem;
    margin-bottom: 0.4rem;
    font-family: 'Manrope', sans-serif;
    font-weight: 700;
}

.section-title {
    font-size: 2rem;
    margin-bottom: 1.5rem;
    max-width: 34ch;
}

.muted { color: var(--text-muted); }

/* ---------- Nav ---------- */
.portfolio-nav {
    position: sticky;
    top: 0;
    z-index: 999;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.9rem 0;
    background: rgba(11,17,32,0.85);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--border);
    margin-bottom: 0.5rem;
}
.portfolio-nav .brand {
    font-family: 'Newsreader', serif;
    font-size: 1.15rem;
    color: var(--text);
    text-decoration: none;
}
.portfolio-nav .links a {
    color: var(--text-muted);
    text-decoration: none;
    margin-left: 1.6rem;
    font-size: 0.92rem;
    font-weight: 600;
    transition: color 0.15s ease;
}
.portfolio-nav .links a:hover { color: var(--accent); }

/* ---------- Hero ---------- */
.hero {
    position: relative;
    padding: 4rem 0 3rem 0;
    overflow: hidden;
}
.hero-grid-bg {
    position: absolute;
    inset: -20% -10%;
    background-image:
        linear-gradient(rgba(95,168,211,0.08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(95,168,211,0.08) 1px, transparent 1px);
    background-size: 46px 46px;
    -webkit-mask-image: radial-gradient(ellipse 70% 60% at 30% 30%, black 40%, transparent 75%);
    mask-image: radial-gradient(ellipse 70% 60% at 30% 30%, black 40%, transparent 75%);
    animation: driftGrid 22s linear infinite;
    z-index: 0;
}
@keyframes driftGrid {
    0% { transform: translate(0, 0); }
    100% { transform: translate(46px, 46px); }
}
.hero-content { position: relative; z-index: 1; }
.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--accent-2);
    font-weight: 700;
    font-size: 0.95rem;
    margin-bottom: 1rem;
}
.hero-eyebrow .dot {
    width: 7px; height: 7px; border-radius: 50%;
    background: var(--good);
    box-shadow: 0 0 0 4px rgba(111,207,151,0.15);
}
.hero-title {
    font-size: clamp(2.1rem, 5vw, 3.4rem);
    line-height: 1.12;
    max-width: 16ch;
    margin-bottom: 1.1rem;
}
.hero-sub {
    color: var(--text-muted);
    font-size: 1.08rem;
    max-width: 56ch;
    margin-bottom: 2rem;
}
.hero-ctas { display: flex; gap: 0.9rem; flex-wrap: wrap; }

.btn {
    display: inline-block;
    padding: 0.7rem 1.4rem;
    border-radius: 8px;
    font-weight: 700;
    font-size: 0.95rem;
    text-decoration: none;
    transition: transform 0.15s ease, box-shadow 0.15s ease, background 0.15s ease;
    border: 1px solid transparent;
}
.btn-primary { background: var(--accent); color: #1A1200; }
.btn-primary:hover { transform: translateY(-1px); box-shadow: 0 8px 24px rgba(232,163,61,0.25); }
.btn-secondary { background: transparent; color: var(--text); border-color: var(--border); }
.btn-secondary:hover { border-color: var(--accent-2); color: var(--accent-2); }

/* ---------- Cards / glass ---------- */
.glass-card {
    background: linear-gradient(180deg, var(--surface) 0%, rgba(19,27,46,0.6) 100%);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.4rem 1.5rem;
    backdrop-filter: blur(6px);
    transition: border-color 0.15s ease, transform 0.15s ease;
    height: 100%;
}
.glass-card:hover { border-color: rgba(232,163,61,0.4); }

/* ---------- Skills ---------- */
.skill-category-title {
    font-weight: 800;
    font-size: 0.85rem;
    color: var(--accent-2);
    text-transform: none;
    margin-bottom: 0.7rem;
}
.badge-row { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.skill-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: var(--text);
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 0.32rem 0.6rem;
    white-space: nowrap;
}
.skill-badge .note {
    color: var(--text-muted);
    font-family: 'Manrope', sans-serif;
    font-size: 0.72rem;
    margin-left: 0.4rem;
}

/* ---------- Projects ---------- */
.project-name { font-size: 1.15rem; margin-bottom: 0.3rem; }
.project-problem {
    color: var(--accent-2);
    font-size: 0.88rem;
    margin: 0.6rem 0 0.5rem 0;
}
.tech-row { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 0.8rem; }
.tech-pill {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-muted);
    border: 1px solid var(--border);
    border-radius: 999px;
    padding: 0.2rem 0.6rem;
}
.link-placeholder {
    color: var(--text-muted);
    font-size: 0.82rem;
    font-style: italic;
    border: 1px dashed var(--border);
    border-radius: 6px;
    padding: 0.35rem 0.7rem;
    display: inline-block;
    margin-top: 0.9rem;
}

/* ---------- Timeline ---------- */
.timeline { position: relative; padding-left: 1.6rem; }
.timeline::before {
    content: "";
    position: absolute;
    left: 5px; top: 6px; bottom: 6px;
    width: 2px;
    background: var(--border);
}
.timeline-item { position: relative; padding-bottom: 1.5rem; }
.timeline-item::before {
    content: "";
    position: absolute;
    left: -1.6rem; top: 4px;
    width: 11px; height: 11px;
    border-radius: 50%;
    border: 2px solid var(--bg);
}
.timeline-item.done::before { background: var(--good); }
.timeline-item.current::before { background: var(--warn); box-shadow: 0 0 0 4px rgba(232,163,61,0.18); }
.timeline-item.upcoming::before { background: var(--surface-2); border-color: var(--border); }
.timeline-label { font-weight: 700; }
.timeline-status {
    font-size: 0.78rem;
    color: var(--text-muted);
    margin-left: 0.5rem;
}

/* ---------- GitHub panel ---------- */
.gh-stat { text-align: center; }
.gh-stat .num { font-family: 'Newsreader', serif; font-size: 1.8rem; color: var(--accent); }
.gh-stat .label { color: var(--text-muted); font-size: 0.82rem; }

/* ---------- Contact ---------- */
.contact-links { display: flex; gap: 0.9rem; flex-wrap: wrap; margin-top: 1rem; }

/* ---------- Footer ---------- */
.pf-footer {
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid var(--border);
    color: var(--text-muted);
    font-size: 0.85rem;
    text-align: left;
}

@media (max-width: 640px) {
    .block-container { padding-left: 1rem; padding-right: 1rem; }
    .hero-title { max-width: 100%; }
    .portfolio-nav .links a { margin-left: 0.9rem; font-size: 0.82rem; }
}
</style>
"""


def inject_css(st):
    """Inject the design system once. Call at the top of app.py."""
    st.markdown(CSS, unsafe_allow_html=True)
