# Spam Mail

A small Streamlit app and model for identifying spam email messages.

Contents
- `app.py` — Streamlit application
- `model_app.py` — Model and inference code
- `mail_data.csv` — Dataset (committed)

Quick start
1. Create a virtualenv and install requirements:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
2. Run the app locally:
```
streamlit run app.py
```

Notes
- The CSV dataset is included in this repository; if you prefer not to store datasets in GitHub long-term, consider using Git LFS or an external data store.
- If you'd like I can add a LICENSE, CI, or more documentation.