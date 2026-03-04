import pandas as pd
import numpy as np


def calculate_emi(principal: float, annual_rate: float, years: int) -> float:
    """
    Calculate Equated Monthly Installment (EMI).

    Args:
        principal (float): Loan amount.
        annual_rate (float): Annual interest rate.
        years (int): Loan duration in years.

    Returns:
        float: Monthly EMI value.
    """
    monthly_rate = annual_rate / (12 * 100)
    months = years * 12

    if monthly_rate == 0:
        return principal / months

    emi = principal * monthly_rate * (1 + monthly_rate) ** months \
        / ((1 + monthly_rate) ** months - 1)

    return emi


def classify_risk(dti: float) -> str:
    """
    Classify risk based on DTI ratio.
    """
    if dti > 0.5:
        return "High"
    elif dti > 0.3:
        return "Medium"
    else:
        return "Low"


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform financial transformations:
    - EMI
    - Monthly income
    - DTI ratio
    - Risk classification
    """

    # 1️⃣ EMI
    df["emi"] = df.apply(
        lambda row: calculate_emi(
            row["loan_amount"],
            row["interest_rate"],
            row["loan_term_years"]
        ),
        axis=1
    )

    # 2️⃣ Monthly Income
    df["monthly_income"] = df["annual_income"] / 12

    # 3️⃣ Debt-to-Income Ratio
    df["dti"] = df["emi"] / df["monthly_income"]

    # 4️⃣ Risk Category
    df["risk_category"] = df["dti"].apply(classify_risk)

    return df