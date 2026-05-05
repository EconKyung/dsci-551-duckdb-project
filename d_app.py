import duckdb
from c_queries import (yearly_fare_trend, route_market_summary, high_concentration_routes, explain_yearly_fare_trend)

# Connect to the DuckDB database
con = duckdb.connect("us_airline_data.duckdb")

print("=== 1. Yearly Fare Trend ===")
print(yearly_fare_trend(con).head(10))

print("\n=== 2. Route Market Summary ===")
print(route_market_summary(con).head(10))

print("\n=== 3. High-Concentration Routes ===")
print(high_concentration_routes(con).head(10))

# print("\n=== EXPLAIN: Yearly Fare Trend Query ===")
# print(explain_yearly_fare_trend(con))

# Close the connection
con.close()