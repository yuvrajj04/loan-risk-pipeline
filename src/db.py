import sqlite3
import pandas as pd


def save_to_db(df: pd.DataFrame, db_name: str = "loan_risk.db"):
    """
    Save DataFrame to SQLite database.
    """
    try:
        conn = sqlite3.connect(db_name)
        df.to_sql("loans", conn, if_exists="replace", index=False)
        conn.close()
        print("✅ Data saved to SQLite database successfully.")
    except Exception as e:
        print(f"❌ Error saving to database: {e}")
        raise