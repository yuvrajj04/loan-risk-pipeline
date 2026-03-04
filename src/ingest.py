import pandas as pd
from pathlib import Path


def load_data(file_path: str | None = None) -> pd.DataFrame:
    """
    Load CSV file into a pandas DataFrame.

    When *file_path* is not provided or is a relative path,
    resolve it relative to the project root (two levels above this file).

    This makes the function more resilient when called from
    different working directories.
    """
    base = Path(__file__).parents[1]  # project root
    if file_path is None:
        file_path = base / "data" / "loan_data.csv"
    else:
        file_path = Path(file_path)
        if not file_path.is_absolute():
            file_path = base / file_path

    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully.")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        raise


if __name__ == "__main__":
    # Path relative to project root
    file_path = "../data/loan_data.csv"

    df = load_data(file_path)

    print("\n🔎 First 5 rows:")
    print(df.head())