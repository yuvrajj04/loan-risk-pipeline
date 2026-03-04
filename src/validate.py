import pandas as pd

def validate_data(df: pd.DataFrame) -> list:
    """
    Validate loan dataset.
    Returns a list of validation error messages.
    """

    errors = []

    # 1️⃣ Check for null values
    if df.isnull().values.any():
        errors.append("Null values found in dataset.")

    # 2️⃣ Check negative or zero loan amount
    if (df["loan_amount"] <= 0).any():
        errors.append("Invalid loan amount detected (<= 0).")

    # 3️⃣ Check invalid interest rate
    if (df["interest_rate"] <= 0).any() or (df["interest_rate"] > 100).any():
        errors.append("Invalid interest rate detected (must be between 0 and 100).")

    # 4️⃣ Check duplicate IDs
    if df["id"].duplicated().any():
        errors.append("Duplicate loan IDs found.")

    return errors