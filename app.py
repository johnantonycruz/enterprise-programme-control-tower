import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Enterprise Programme Control Tower", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    path = Path(__file__).parent / "data" / "projects.csv"
    df = pd.read_csv(path)
    df["next_milestone"] = pd.to_datetime(df["next_milestone"])
    return df

projects = load_data()
st.title("Enterprise Programme Control Tower")
st.caption("Demonstration using fictional retail technology portfolio data — not client information")

with st.sidebar:
    st.header("Filters")
    workstreams = st.multiselect("Workstream", sorted(projects["workstream"].unique()), default=sorted(projects["workstream"].unique()))
    statuses = st.multiselect("RAG status", ["Green", "Amber", "Red"], default=["Green", "Amber", "Red"])

filtered = projects[projects["workstream"].isin(workstreams) & projects["rag"].isin(statuses)].copy()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Projects", len(filtered))
c2.metric("Red projects", int((filtered["rag"] == "Red").sum()))
c3.metric("Total budget", f"£{filtered['budget_gbp'].sum():,.0f}")
c4.metric("Forecast variance", f"£{(filtered['forecast_gbp'] - filtered['budget_gbp']).sum():+,.0f}")

left, right = st.columns(2)
with left:
    st.subheader("Delivery RAG")
    counts = filtered["rag"].value_counts().reindex(["Green", "Amber", "Red"], fill_value=0)
    st.bar_chart(counts)
with right:
    st.subheader("Budget vs forecast by workstream")
    summary = filtered.groupby("workstream")[["budget_gbp", "forecast_gbp"]].sum()
    st.bar_chart(summary)

st.subheader("Project register")
st.dataframe(
    filtered.sort_values("next_milestone").rename(columns={
        "project_id": "ID", "project_name": "Project", "workstream": "Workstream",
        "rag": "RAG", "owner": "Owner", "budget_gbp": "Budget (£)",
        "forecast_gbp": "Forecast (£)", "next_milestone": "Next milestone", "milestone_name": "Milestone"
    }),
    use_container_width=True, hide_index=True,
)
st.info("Version 1 is read-only. Later versions will add demand prioritisation, capacity planning, dependencies and reporting.")
