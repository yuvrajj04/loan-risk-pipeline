import pandas as pd


def generate_report(df: pd.DataFrame):
    """
    Generate analytics summary and export report.
    """

    print("\n📊 ===== LOAN RISK ANALYTICS REPORT =====")

    # 1️⃣ Total loans
    total_loans = len(df)
    print(f"\nTotal Loans: {total_loans}")

    # 2️⃣ Average loan amount
    avg_loan = df["loan_amount"].mean()
    print(f"Average Loan Amount: {avg_loan:.2f}")

    # 3️⃣ Risk distribution
    print("\nRisk Distribution:")
    risk_dist = df["risk_category"].value_counts()
    print(risk_dist)

    # 4️⃣ Export CSV report
    summary_df = pd.DataFrame({
        "Metric": ["Total Loans", "Average Loan Amount"],
        "Value": [total_loans, avg_loan]
    })

    risk_df = risk_dist.reset_index()
    risk_df.columns = ["Risk Category", "Count"]

    summary_df.to_csv("summary_report.csv", index=False)
    risk_df.to_csv("risk_distribution.csv", index=False)

    print("\n✅ Reports exported:")
    print(" - summary_report.csv")
    print(" - risk_distribution.csv")