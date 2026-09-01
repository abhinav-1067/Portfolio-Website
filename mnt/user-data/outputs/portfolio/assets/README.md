# Assets

Drop your real files here — nothing in this folder is generated/fake:

- `images/profile.png` — your profile photo or avatar (referenced by `utils/config.py -> PROFILE_IMAGE`, currently unused in the UI until you add one and wire it into `components/hero.py` with `st.image`).
- `resume.pdf` — your resume (referenced by `utils/config.py -> RESUME_PATH`; the Contact section will automatically show a working download button once this file exists).
- `icons/`, `animations/` — optional, for any custom icons or Lottie/SVG assets you want to add later.
