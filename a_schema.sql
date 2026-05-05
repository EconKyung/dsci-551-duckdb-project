CREATE OR REPLACE TABLE flights AS
SELECT
    Year,
    quarter,
    city1,
    city2,
    airport_1,
    airport_2,
    passengers,
    fare,
    carrier_lg,
    large_ms,
    fare_lg,
    carrier_low,
    lf_ms,
    fare_low
FROM read_csv_auto('US Airline Flight Routes and Fares 1993-2024.csv');