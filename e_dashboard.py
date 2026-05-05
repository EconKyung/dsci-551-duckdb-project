import duckdb
import streamlit as st
from c_queries import (
    yearly_fare_trend,
    route_market_summary,
    high_concentration_routes,
    explain_yearly_fare_trend,
    explain_route_market_summary,
    explain_high_concentration_routes,
)

st.set_page_config(page_title="Airline Market Analysis Dashboard", layout="wide")

st.title("Kyung's DuckDB-Based Airline Market Analysis Dashboard")
st.write(
    "This dashboard analyzes airline pricing, passenger demand, and market concentration "
    "using DuckDB."
)

# Connect to DuckDB
con = duckdb.connect("us_airline_data.duckdb")

# Sidebar inputs
st.sidebar.header("User Inputs")

start_year = st.sidebar.slider("Start Year", min_value=1993, max_value=2024, value=2015)
end_year = st.sidebar.slider("End Year", min_value=1993, max_value=2024, value=2024)
top_n_routes = st.sidebar.slider("Top N Routes", min_value=5, max_value=50, value=10)
market_share_threshold = st.sidebar.slider(
    "High Concentration Threshold",
    min_value=0.50,
    max_value=0.95,
    value=0.70,
    step=0.05,
)
top_n_high_conc = st.sidebar.slider(
    "Top N High-Concentration Routes",
    min_value=5,
    max_value=50,
    value=20,
)

# Section 1
st.header("1. Yearly Fare Trend")
yearly_df = yearly_fare_trend(con, start_year, end_year)
st.dataframe(yearly_df, use_container_width=True)

if not yearly_df.empty:
    st.subheader("Average Fare by Year")
    st.line_chart(yearly_df.set_index("Year")["avg_fare"])

    st.subheader("Average Fare Gap by Year")
    st.line_chart(yearly_df.set_index("Year")["avg_fare_gap"])

# Section 2
st.header("2. Route Market Summary")
route_df = route_market_summary(con, top_n=top_n_routes)
st.dataframe(route_df, use_container_width=True)

# Section 3
st.header("3. High-Concentration Routes")
high_conc_df = high_concentration_routes(
    con,
    threshold=market_share_threshold,
    top_n=top_n_high_conc
)
st.dataframe(high_conc_df, use_container_width=True)

# Section 4
st.header("4. Internal Database Mechanism (EXPLAIN)")

st.write(
    "This section shows DuckDB execution plans for each major application operation."
)

explain_choice = st.selectbox(
    "Choose an operation to explain:",
    [
        "Yearly Fare Trend",
        "Route Market Summary",
        "High-Concentration Routes",
    ],
)

if st.button("Show EXPLAIN Plan"):
    if explain_choice == "Yearly Fare Trend":
        plan_text = explain_yearly_fare_trend(con, start_year, end_year)

    elif explain_choice == "Route Market Summary":
        plan_text = explain_route_market_summary(con, top_n=top_n_routes)

    else:
        plan_text = explain_high_concentration_routes(
            con,
            threshold=market_share_threshold,
            top_n=top_n_high_conc
        )

    st.code(plan_text)