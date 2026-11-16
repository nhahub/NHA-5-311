import sys
from pathlib import Path

# Make sure Python can find the hr_pipeline folder
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Force Python to re-read our files from disk on every run
for name in list(sys.modules):
    if name.startswith("hr_pipeline"):
        del sys.modules[name]

from hr_pipeline.config import PROCESSED_DATA_PATH
from hr_pipeline.data_loader import HRDataLoader
from hr_pipeline.summary_loader import HRSummaryLoader
from hr_pipeline.data_cleaner import HRDataCleaner
from hr_pipeline.feature_engineer import HRFeatureEngineer
from hr_pipeline.visualizer import HRVisualizer
from hr_pipeline.database import HRDatabase


def main():
    # 1) Load the main data (Raw Data sheet)
    df = HRDataLoader().load()
    print("Raw shape:", df.shape)

    # 2) Clean
    cleaner = HRDataCleaner(df)
    df_clean = cleaner.clean()

    print("\n--- Data quality report ---")
    for check, result in cleaner.validate().items():
        print(f"{check}: {result}")

    # 3) Feature engineering
    engineer = HRFeatureEngineer(df_clean)
    df_final = engineer.create_features()
    print("\nFinal shape:", df_final.shape)

    # 4) Save the clean data
    df_final.to_csv(PROCESSED_DATA_PATH, index=False)
    print("Saved to:", PROCESSED_DATA_PATH)

    # 5) Charts (EDA)
    visualizer = HRVisualizer(df_final)
    visualizer.plot_all()
    print("Charts saved to:", visualizer.output_dir)

    # 6) Load the other sheets (summaries + data dictionary)
    summaries = HRSummaryLoader().load_all()

    # 7) Load everything into the SQL database
    db = HRDatabase()
    db.connect()
    try:
        db.load_table(df_final, "employees")
        for table_name, table_df in summaries.items():
            db.load_table(table_df, table_name)

        print("\n--- Tables in the database ---")
        for table_name in ["employees"] + list(summaries):
            count = db.query(f"SELECT COUNT(*) AS n FROM {table_name}")["n"][0]
            print(f"{table_name}: {count} rows")
    finally:
        db.close()


if __name__ == "__main__":
    main()