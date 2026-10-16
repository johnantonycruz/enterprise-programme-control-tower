# Enterprise Programme Control Tower

A beginner-friendly, interview-ready portfolio dashboard built with Python, Pandas and Streamlit. All project data is **fictional**.

## Run locally

1. Install Python 3.11 or newer.
2. Open a terminal in this folder.
3. Create a virtual environment (optional but recommended): `python -m venv .venv`.
4. Activate it: Windows PowerShell `.venv\Scripts\Activate.ps1` or macOS/Linux `source .venv/bin/activate`.
5. Install dependencies: `pip install -r requirements.txt`.
6. Launch: `streamlit run app.py`.
7. Open the local URL displayed in the terminal (usually http://localhost:8501).

## GitHub + hosting

Create a new GitHub repository and upload `app.py`, `requirements.txt`, `README.md` and the `data` folder. On Streamlit Community Cloud, choose **Create app**, connect the repository and select `app.py` as the entry point. Never upload confidential employer or client data.

## V1 features

- Filter projects by workstream and RAG status
- See portfolio KPIs and forecast variance
- Compare budget and forecast by workstream
- Inspect a milestone-ordered project register

## Next versions

Demand prioritisation, resource capacity, integrated dependencies, RAID and executive reporting.
