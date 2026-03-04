# Loan Risk Analytics Pipeline

## Overview

The **Loan Risk Analytics Pipeline** is a mini data engineering project that processes loan datasets to evaluate borrower risk.
The pipeline ingests raw CSV data, performs validation checks, applies financial transformations (EMI and Debt-to-Income ratio), stores processed data in a database, and generates analytics reports.

This project simulates a **real-world financial data processing workflow** used in lending and credit risk systems.

---

## Problem Statement

Financial institutions must evaluate borrower risk before approving loans. Raw loan data must be cleaned, validated, and transformed into meaningful financial metrics to determine borrower risk levels.

This project demonstrates how a **data pipeline** can automate that process by:

- Ingesting raw loan datasets
- Validating data quality
- Computing financial metrics
- Classifying loan risk
- Persisting processed data
- Generating analytics reports

---

## Architecture

```
                +-------------+
                |   CSV Data  |
                | loan_data   |
                +------+------+
                       |
                       v
                +-------------+
                | Data Ingest |
                +------+------+
                       |
                       v
                +-------------+
                | Data Validate |
                | (quality checks) |
                +------+------+
                       |
                       v
                +-------------+
                | Transformation |
                | EMI / DTI Calc |
                +------+------+
                       |
                       v
                +-------------+
                | SQLite DB  |
                | loans table |
                +------+------+
                       |
                       v
                +-------------+
                | Analytics   |
                | Risk Report |
                +-------------+
```

---

## Data Flow

1. **Data Ingestion**
   - Reads loan dataset from CSV using Pandas.

2. **Data Validation**
   - Detects null values
   - Detects negative loan amounts
   - Validates interest rates
   - Checks duplicate loan IDs

3. **Data Transformation**
   - Calculates EMI (Equated Monthly Installment)
   - Calculates monthly income
   - Computes Debt-to-Income Ratio (DTI)
   - Classifies borrower risk (Low / Medium / High)

4. **Data Storage**
   - Stores transformed dataset in a SQLite database.

5. **Analytics**
   - Calculates summary metrics
   - Generates risk distribution report
   - Exports analytics CSV files.

---

## Tech Stack

- **Python 3**
- **Pandas** – Data processing
- **SQLite** – Lightweight database
- **Pytest** – Unit testing
- **Logging module** – Pipeline monitoring

---

## Project Structure

```
loan-risk-pipeline/
│
├── data/
│   └── loan_data.csv
│
├── src/
│   ├── ingest.py
│   ├── validate.py
│   ├── transform.py
│   ├── db.py
│   ├── risk_analysis.py
│   └── main.py
│
├── tests/
│   └── test_pipeline.py
│
├── loan_risk.db
├── requirements.txt
└── README.md
```

---

## How to Run

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/loan-risk-pipeline.git
cd loan-risk-pipeline
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Pipeline

```bash
python src/main.py
```

---

## Sample Output

```
🚀 Starting Loan Risk Analytics Pipeline

INFO | Loading dataset...
INFO | Running validation...
INFO | Validation successful
INFO | Running data transformation...
INFO | Saving data to SQLite database...
INFO | Generating analytics report...

📊 Loan Risk Analytics Report

Total Loans: 10
Average Loan Amount: 505000

Risk Distribution
Low      4
Medium   3
High     3

Pipeline completed successfully
```

Generated files:

```
loan_risk.db
summary_report.csv
risk_distribution.csv
```

---

## Testing

Run unit tests using pytest:

```bash
pytest
```

Expected output:

```
6 passed in 0.35s
```

---

## Key Concepts Demonstrated

- Data pipeline architecture
- Data validation and quality checks
- Financial risk modeling
- Database persistence
- Analytics reporting
- Unit testing
- Logging for production pipelines

---

## Future Improvements

Possible enhancements:

- Integrate **AWS S3** for data ingestion
- Store results in **PostgreSQL or AWS RDS**
- Schedule pipeline using **Apache Airflow**
- Add **Streamlit dashboard** for visualization
- Implement **Docker containerization**
- Add **CI/CD pipeline with GitHub Actions**

---

## Author

**Yuvraj Singh Rana**

Software Engineer
Passionate about building scalable systems and intuitive digital experiences.
