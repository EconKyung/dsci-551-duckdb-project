# DuckDB Airline Analysis Dashboard

This project is a DuckDB-based analytical dashboard that analyzes airline pricing, passenger demand, and market concentration across U.S. routes.

Built for DSCI 551, the project focuses on connecting database internals with application behavior using EXPLAIN plans.

---

## Features

- Yearly fare trend analysis
- Route-level market summary
- High-concentration route filtering
- Query execution plan visualization (EXPLAIN)

---

## Technologies Used

- DuckDB
- Python
- Streamlit
- Pandas

---

## 1. Environment Setup

Make sure you have:

- Python 3.9 or higher installed

---

## 2. Install Dependencies

Run:

- pip install -r requirements.txt

---

## 3. Dataset Setup

This project uses the dataset:

- **US Airline Flight Routes and Fares (1993–2024).csv**


Download dataset from:

[https://www.kaggle.com/datasets/bhavikjikadara/us-airline-flight-routes-and-fares-1993-2024]


Place it in the project folder with this exact name:

- US Airline Flight Routes and Fares 1993-2024.csv

---

## 4. Database Setup

Run:

- python b_setup_database.py

This will:
- create `us_airline_data.duckdb`
- load the dataset into the `flights` table

---

## 5. Run the Application

Run the dashboard:


python -m streamlit run e_dashboard.py

---

## 6. How to Use

- Adjust filters from the sidebar:
  - Year range
  - Number of routes
  - Market concentration threshold
- View results in tables and charts
- Use the EXPLAIN section to inspect query execution plans

---

## 7. Reproducing Results

To fully reproduce the project:

1. Install dependencies  
2. Download dataset  
3. Run setup script  
4. Launch dashboard  

---

## Notes

- No secret keys or credentials are required for this project.
- The dataset is static and does not require external APIs.
