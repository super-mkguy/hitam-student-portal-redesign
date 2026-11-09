# HITAM Student Portal — UI/UX redesign demo

A Streamlit prototype for a student portal redesign. This is a design demo and is not connected to HITAM systems.

## Contents

- `TASK2.py` — the Streamlit app
- `assets/hitam-logo.png` — HITAM logo from the [official website](https://hitam.org/)
- `.streamlit/config.toml` — green, high-contrast theme
- `requirements.txt` — pinned Streamlit dependency

All student, academic, timetable, results, transport, and hostel details are illustrative sample data. They are not live HITAM records.

## Run locally

```bash
python -m pip install -r requirements.txt
python -m streamlit run TASK2.py
```

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository and upload the contents of this folder to its root.
2. Visit [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Choose **Create app**, then select the repository and its default branch.
4. Set the app file path to `TASK2.py` and deploy.
5. Set the app to public if you want anyone with the link to view it; otherwise invite specific reviewers.

Streamlit Community Cloud installs the packages listed in `requirements.txt`. Keep this prototype free of personal records, passwords, and private credentials before publishing.
