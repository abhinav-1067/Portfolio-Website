"""
Central configuration for the portfolio.

Edit the values in this file to update the site's content — you should not
need to touch app.py or the components/ folder for routine content changes.

Anything marked PLACEHOLDER is intentionally left blank/generic because it
was not provided. Fill it in with your real information before deploying.
"""

# ---------------------------------------------------------------------------
# Identity
# ---------------------------------------------------------------------------
NAME = "Abhinav Yadav"
HEADLINE = "Data Scientist in training, one dataset at a time"
SUBHEADLINE = (
    "1st-year Computer Science (BTech) student building a practical "
    "foundation in Python, data analysis, and backend development — "
    "working toward internships and a career in data science."
)

# Profile image path — replace with your own photo/avatar.
PROFILE_IMAGE = "assets/images/profile.png"  # PLACEHOLDER — add your image here

# Primary / secondary hero call-to-actions
PRIMARY_CTA_LABEL = "View projects"
PRIMARY_CTA_TARGET = "projects"  # anchor id on the page
SECONDARY_CTA_LABEL = "Get in touch"
SECONDARY_CTA_TARGET = "contact"

# ---------------------------------------------------------------------------
# About
# ---------------------------------------------------------------------------
ABOUT_PARAGRAPHS = [
    "I'm in my first year of a BTech in Computer Science, and I'm using "
    "these early years to build real, hands-on skill rather than waiting "
    "for later semesters — my goal is to start applying for data-related "
    "internships as early as I reasonably can.",
    "Most of my time goes into the Python and data-science stack: NumPy "
    "and Pandas for working with data, SQL for storing and querying it, "
    "and Matplotlib/Seaborn for making sense of it visually. Alongside "
    "that, I'm learning Flask to build small backends and APIs, and I use "
    "Git/GitHub as the backbone for every project I ship.",
    "I'm currently branching into C++ and data structures & algorithms, "
    "and picking up Streamlit to turn scripts and analyses into things "
    "people can actually interact with — this site is one example of "
    "that. Machine learning, and eventually cloud platforms like AWS or "
    "Azure, are next on the roadmap.",
    "My approach is to learn by building — small, complete projects over "
    "half-finished tutorials — and to keep stacking those projects until "
    "they add up to something worth showing an employer.",
]

# ---------------------------------------------------------------------------
# Skills
# Each category maps to a list of (skill_name, note) tuples. `note` is a
# short, honest qualifier — not a fake percentage. Use "" for no note.
# ---------------------------------------------------------------------------
SKILLS = {
    "Programming": [
        ("Python", "core language"),
        ("C++", "learning DSA"),
    ],
    "Data Science": [
        ("NumPy", ""),
        ("Pandas", ""),
        ("Matplotlib", ""),
        ("Seaborn", ""),
        ("Statistics", ""),
        ("Machine Learning", "next up"),
    ],
    "Databases": [
        ("SQL", ""),
        ("SQLite", ""),
    ],
    "Backend": [
        ("Flask", ""),
        ("REST APIs", ""),
        ("Jinja", ""),
    ],
    "Tools": [
        ("Git", ""),
        ("GitHub", ""),
        ("VS Code", ""),
        ("Anaconda", ""),
        ("Streamlit", ""),
    ],
    "Currently exploring": [
        ("DSA", ""),
        ("Cloud (AWS/Azure)", ""),
    ],
}

# ---------------------------------------------------------------------------
# Projects
# github_url left as None -> UI shows a clearly marked "add link" placeholder
# instead of a dead/fake button.
# ---------------------------------------------------------------------------
PROJECTS = [
    {
        "name": "Student Performance Analyzer",
        "description": (
            "A SQLite-backed tool for analyzing student performance data, "
            "with a clean split between data access, analysis, and "
            "graphing logic."
        ),
        "problem": "Makes it easy to query and visualize performance trends "
        "instead of reading raw rows in a database.",
        "features": [
            "SQLite database layer (database.py)",
            "Analysis logic separated from data access (analysis.py)",
            "Chart generation for performance trends (graphs.py)",
        ],
        "tech": ["Python", "SQLite", "Matplotlib"],
        "github_url": "https://github.com/abhinav-1067/Practice-Projects/tree/main/Student%20Perfomance%20Analyzer",
        "demo_url": None,
    },
    {
        "name": "Sales Data Analyzer",
        "description": (
            "A NumPy-driven analysis script that loads raw sales data and "
            "extracts summary statistics and trends."
        ),
        "problem": "Turns a raw sales CSV into usable numeric summaries "
        "without pulling in a heavier data framework.",
        "features": [
            "Data loading via numpy.genfromtxt",
            "Array-based aggregation and analysis",
        ],
        "tech": ["Python", "NumPy"],
        "github_url": "https://github.com/abhinav-1067/Practice-Projects/tree/main/Sales%20Analyzer",
        "demo_url": None,
    },
    {
        "name": "Contact Book",
        "description": "A basic Python application for storing and managing contacts.",
        "problem": "A foundational project for practicing core Python "
        "application structure and data handling.",
        "features": [
            "Add / view / manage contact records",
            "Core Python data structures, no external dependencies",
        ],
        "tech": ["Python"],
        "github_url": "https://github.com/abhinav-1067/Practice-Projects/tree/main/Contact%20Book",
        "demo_url": None,
    },
    {
        "name": "IPL Team API",
        "description": (
            "A Flask API serving IPL team-vs-team data, with query-"
            "parameter based filtering and JSON responses."
        ),
        "problem": "Practices building a real REST-style API on top of a "
        "structured sports dataset.",
        "features": [
            "Flask routes for team-vs-team lookups",
            "Query-parameter filtering",
            "JSON response formatting",
        ],
        "tech": ["Python", "Flask", "REST API"],
        "github_url": "https://github.com/abhinav-1067/Practice-Projects/tree/main/ipl-api-service",
        "demo_url": None,
    },
    {
        "name": "Flask Practice Suite",
        "description": (
            "A set of small Flask apps covering the core patterns of web "
            "backends — templating, auth flows, and JSON storage."
        ),
        "problem": "Builds fluency with Flask fundamentals through small, "
        "focused exercises rather than one large app.",
        "features": [
            "Jinja-templated pages",
            "Registration/login flow",
            "JSON-based data storage",
        ],
        "tech": ["Python", "Flask", "Jinja"],
        "github_url": "https://github.com/abhinav-1067/Data-Science-Learning/tree/main/Section-18-flask/flask11",
        "demo_url": None,
    },
]

# ---------------------------------------------------------------------------
# Learning journey / roadmap — shown as a timeline.
# `status` is one of: "done", "current", "upcoming"
# ---------------------------------------------------------------------------
JOURNEY = [
    {"label": "Python fundamentals", "status": "done"},
    {"label": "NumPy & Pandas", "status": "done"},
    {"label": "SQL / SQLite", "status": "done"},
    {"label": "Data analysis & visualization", "status": "done"},
    {"label": "Flask & APIs", "status": "done"},
    {"label": "Statistics", "status": "current"},
    {"label": "DSA with Python & C++", "status": "current"},
    {"label": "Streamlit", "status": "current"},
    {"label": "Machine Learning", "status": "upcoming"},
    {"label": "Cloud (AWS / Azure)", "status": "upcoming"},
    {"label": "Internships", "status": "upcoming"},
]

# ---------------------------------------------------------------------------
# GitHub / developer section
# ---------------------------------------------------------------------------
GITHUB_USERNAME = "abhinav-1067"

# ---------------------------------------------------------------------------
# Contact — fill these in with your real details before deploying.
# ---------------------------------------------------------------------------
EMAIL = "mailto:abhinavyadav1673@gmail.com"  # PLACEHOLDER — add your email
GITHUB_URL = f"https://github.com/{GITHUB_USERNAME}"
LINKEDIN_URL = "https://www.linkedin.com/in/abhinav-yadav-3a4a05375/"  # PLACEHOLDER — add your LinkedIn URL
RESUME_PATH = "assets/resume.pdf"  # PLACEHOLDER — drop your resume PDF here

PAGE_TITLE = f"{NAME} — Portfolio"
PAGE_ICON = "🧭"
