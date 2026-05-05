import duckdb

# Step 1: Connect to DuckDB (creates file if not exists)
con = duckdb.connect("US_airline_data.duckdb")

print("Connected to DuckDB")

# Step 2: Read schema.sql
with open("a_schema.sql", "r") as f:
    schema_sql = f.read()

print("Loaded a_schema.sql")

# Step 3: Execute schema (this creates 'flights' table)
con.execute(schema_sql)

print("Created 'flights' table")

# Step 4: Verify table creation
row_count = con.execute("SELECT COUNT(*) FROM flights").fetchone()[0]
print(f"Rows loaded into flights table: {row_count}")

# Step 5: Show preview (optional but helpful)
preview = con.execute("SELECT * FROM flights LIMIT 5").df()
print("\nPreview of data:")
print(preview)

# Step 6: Close connection
con.close()

print("Database setup complete")