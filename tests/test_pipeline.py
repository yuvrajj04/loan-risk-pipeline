import pandas as pd
import sys
import os

# Allow tests to import src files
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from transform import calculate_emi, classify_risk
from validate import validate_data


# -------------------------
# Test EMI Calculation
# -------------------------

def test_emi_calculation():
    emi = calculate_emi(100000, 10, 2)
    assert emi > 0


# -------------------------
# Test Risk Classification
# -------------------------

def test_risk_low():
    assert classify_risk(0.2) == "Low"


def test_risk_medium():
    assert classify_risk(0.4) == "Medium"


def test_risk_high():
    assert classify_risk(0.7) == "High"


# -------------------------
# Test Data Validation
# -------------------------

def test_validation_clean_data():

    data = {
        "id": [1, 2],
        "loan_amount": [100000, 200000],
        "annual_income": [500000, 600000],
        "interest_rate": [10, 12],
        "loan_term_years": [5, 3]
    }

    df = pd.DataFrame(data)

    errors = validate_data(df)

    assert errors == []


def test_validation_negative_loan():

    data = {
        "id": [1],
        "loan_amount": [-100000],
        "annual_income": [500000],
        "interest_rate": [10],
        "loan_term_years": [5]
    }

    df = pd.DataFrame(data)

    errors = validate_data(df)

    assert len(errors) > 0