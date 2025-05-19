from storage.duckdb_backend import DuckDBStorage

if __name__ == "__main__":
    db = DuckDBStorage("data/figurex.db")
    print("✅ DuckDB initialized with schema!")
