from urllib.parse import quote_plus

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.types import Unicode

from hr_pipeline.config import SQL_SERVER_NAME, SQL_DATABASE_NAME, SQL_DRIVER


class HRDatabase:
    """Handles the SQL Server connection: connect, load data, run queries."""

    def __init__(self, server=SQL_SERVER_NAME, database=SQL_DATABASE_NAME,
                 driver=SQL_DRIVER):
        self.server = server
        self.database = database
        self.driver = driver
        self.engine = None

    def _build_url(self):
        """Build the connection string for SQL Server (Windows authentication)."""
        odbc = (
            f"DRIVER={{{self.driver}}};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )
        return "mssql+pyodbc:///?odbc_connect=" + quote_plus(odbc)

    def connect(self):
        """Create the connection engine and test it."""
        self.engine = create_engine(self._build_url(), fast_executemany=True)
        with self.engine.connect() as conn:
            conn.execute(text("SELECT 1"))

    def close(self):
        """Close all connections."""
        if self.engine is not None:
            self.engine.dispose()
            self.engine = None

    def load_table(self, df, table_name="employees"):
        """Save a DataFrame as a table in SQL Server."""
        df = df.copy()

        # Category columns (AgeGroup, ...) are saved as plain text
        for col in df.select_dtypes(include="category").columns:
            df[col] = df[col].astype(str)

        # Text columns become NVARCHAR(255) so symbols like the rupee sign are kept
        text_cols = [c for c in df.columns if pd.api.types.is_string_dtype(df[c])]
        sql_types = {col: Unicode(255) for col in text_cols}

        df.to_sql(table_name, self.engine, if_exists="replace",
                  index=False, dtype=sql_types)

    def query(self, sql):
        """Run a SQL query and return the result as a DataFrame."""
        with self.engine.connect() as conn:
            return pd.read_sql(text(sql), conn)