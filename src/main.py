import os
import logging
from ingest import load_data
from validate import validate_data
from transform import transform_data
from db import save_to_db
from risk_analysis import generate_report


# ------------------------
# Configure Logging
# ------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def run_pipeline():
    logging.info("🚀 Starting Loan Risk Analytics Pipeline")

    try:
        # Get correct data path
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(base_dir, "data", "loan_data.csv")

        # 1️⃣ Load Data
        logging.info("Loading dataset...")
        df = load_data(data_path)

        # 2️⃣ Validate Data
        logging.info("Running data validation...")
        errors = validate_data(df)

        if errors:
            logging.error("Validation errors detected:")
            for error in errors:
                logging.error(error)
            logging.error("Pipeline stopped due to validation failure.")
            return

        logging.info("Validation successful")

        # 3️⃣ Transform Data
        logging.info("Running data transformation...")
        df = transform_data(df)

        # 4️⃣ Save to Database
        logging.info("Saving data to SQLite database...")
        save_to_db(df)

        # 5️⃣ Generate Analytics
        logging.info("Generating analytics report...")
        generate_report(df)

        logging.info("🎯 Pipeline completed successfully!")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")


if __name__ == "__main__":
    run_pipeline()