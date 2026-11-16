from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "HR_Business_Performance.xlsx"
RAW_SHEET_NAME = "Raw Data"

PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "hr_clean.csv"

# SQL Server settings
SQL_SERVER_NAME = r"."
SQL_DATABASE_NAME = "HR_Project"
SQL_DRIVER = "ODBC Driver 18 for SQL Server"
CHARTS_DIR = BASE_DIR / "outputs" / "charts"


# Summary sheets in the Excel file -> table names in the database
SUMMARY_SHEETS = {
    "KPI Summary": "kpi_summary",
    "Dept Summary": "dept_summary",
    "Salary Band Summary": "salary_band_summary",
    "Age Group Summary": "age_group_summary",
    "Business Unit Summary": "business_unit_summary",
    "Data Dictionary": "data_dictionary",
}