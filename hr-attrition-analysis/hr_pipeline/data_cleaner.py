import pandas as pd


class HRDataCleaner:
    """Cleans the raw HR data and checks its quality."""

    DATE_COLUMNS = ["HireDate", "LastPromotionDate"]

    def __init__(self, df):
        self.df = df.copy()

    def convert_dates(self):
        """Convert date columns from text to real dates."""
        for col in self.DATE_COLUMNS:
            self.df[col] = pd.to_datetime(self.df[col])

    def add_attrition_flag(self):
        """Create AttritionFlag: 1 = left the company, 0 = still working."""
        self.df["AttritionFlag"] = (self.df["Attrition"] == "Yes").astype(int)

    def clean(self):
        """Run all cleaning steps and return the clean DataFrame."""
        self.convert_dates()
        self.add_attrition_flag()
        return self.df

    def validate(self):
        """Return a dictionary with basic data quality checks."""
        return {
            "Missing values": int(self.df.isna().sum().sum()),
            "Duplicated rows": int(self.df.duplicated().sum()),
            "EmployeeID is unique": self.df["EmployeeID"].is_unique,
            "Promotion before hire": int(
                (self.df["LastPromotionDate"] < self.df["HireDate"]).sum()
            ),
        }