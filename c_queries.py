def yearly_fare_trend(con, start_year, end_year):
    # Analyzes how airline pricing and demand change over time (by year).
    #
    # For each year, this computes:
    # avg_fare: average ticket price
    # avg_fare_gap: difference between dominant vs cheapest carrier
    # total_passengers: total demand

    query = f"""
    SELECT
        Year,
        AVG(fare) AS avg_fare,
        AVG(fare_lg - fare_low) AS avg_fare_gap,
        SUM(passengers) AS total_passengers
    FROM flights
    WHERE Year BETWEEN {start_year} AND {end_year}
      AND fare_lg IS NOT NULL
      AND fare_low IS NOT NULL
    GROUP BY Year
    ORDER BY Year;
    """
    return con.execute(query).df()


def route_market_summary(con, top_n=10):
    # Analyzes each route (city1 → city2) to understand competition and pricing.
    #
    # For each route, this computes:
    # avg_market_share (large_ms): how dominant the biggest airline is
    # avg_fare_gap: pricing difference between airlines
    # total_passengers: demand on that route

    query = f"""
    SELECT
        city1,
        city2,
        AVG(large_ms) AS avg_market_share,
        AVG(fare_lg - fare_low) AS avg_fare_gap,
        SUM(passengers) AS total_passengers
    FROM flights
    WHERE fare_lg IS NOT NULL
      AND fare_low IS NOT NULL
    GROUP BY city1, city2
    ORDER BY total_passengers DESC
    LIMIT {top_n};
    """
    return con.execute(query).df()

def high_concentration_routes(con, threshold=0.7, top_n=20):
    # Finds routes where one airline dominates the market.
    #
    # This filters only rows where large_ms >= 0.7 (meaning one carrier controls ≥70% of the market)
    # city1, city2, market share of the largest carrier, average market share,
    # average fare of the largest carrier, lowest fare, fare gap,
    # routes where the dominant carrier has high market share (large_ms >= 0.7)

    query = f"""
    SELECT
        Year,
        city1,
        city2,
        large_ms,
        fare_lg,
        fare_low,
        (fare_lg - fare_low) AS fare_gap,
        passengers
    FROM flights
    WHERE large_ms >= {threshold}
      AND fare_lg IS NOT NULL
      AND fare_low IS NOT NULL
    ORDER BY fare_gap DESC
    LIMIT {top_n};
    """
    return con.execute(query).df()

## EXPLAIN

def explain_yearly_fare_trend(con, start_year, end_year):
    query = f"""
    SELECT
        Year,
        AVG(fare) AS avg_fare,
        AVG(fare_lg - fare_low) AS avg_fare_gap,
        SUM(passengers) AS total_passengers
    FROM flights
    WHERE Year BETWEEN {start_year} AND {end_year}
      AND fare_lg IS NOT NULL
      AND fare_low IS NOT NULL
    GROUP BY Year
    ORDER BY Year;
    """
    return con.execute("EXPLAIN " + query).fetchone()[1]

def explain_route_market_summary(con, top_n=10):
    query = f"""
    SELECT
        city1,
        city2,
        AVG(large_ms) AS avg_market_share,
        AVG(fare_lg - fare_low) AS avg_fare_gap,
        SUM(passengers) AS total_passengers
    FROM flights
    WHERE fare_lg IS NOT NULL
      AND fare_low IS NOT NULL
    GROUP BY city1, city2
    ORDER BY total_passengers DESC
    LIMIT {top_n};
    """
    return con.execute("EXPLAIN " + query).fetchone()[1]


def explain_high_concentration_routes(con, threshold=0.7, top_n=20):
    query = f"""
    SELECT
        Year,
        city1,
        city2,
        large_ms,
        fare_lg,
        fare_low,
        (fare_lg - fare_low) AS fare_gap,
        passengers
    FROM flights
    WHERE large_ms >= {threshold}
      AND fare_lg IS NOT NULL
      AND fare_low IS NOT NULL
    ORDER BY fare_gap DESC
    LIMIT {top_n};
    """
    return con.execute("EXPLAIN " + query).fetchone()[1]