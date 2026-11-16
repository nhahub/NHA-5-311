# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:56:24 2026

@author: Admin
"""

import pandas as pd

from hr_pipeline.config import RAW_DATA_PATH, SUMMARY_SHEETS


class HRSummaryLoader:
    """Reads the summary sheets and the data dictionary from the Excel file."""

    # The first 2 rows of each sheet are a title and an empty row
    HEADER_ROW = 2

    # Names that are reserved words in SQL Server get a safe name
    RENAME_MAP = {"Column": "ColumnName", "Type": "DataType"}

    def __init__(self, file_path=RAW_DATA_PATH, sheets=SUMMARY_SHEETS):
        self.file_path = file_path
        self.sheets = sheets

    def _clean_column_name(self, name):
        """Make a column name safe for SQL: no spaces, '%' becomes 'Pct'."""
        name = str(name).strip().replace("%", "Pct").replace(" ", "")
        return self.RENAME_MAP.get(name, name)

    def load_all(self):
        """Return a dictionary {table_name: DataFrame} for every summary sheet."""
        tables = {}
        for sheet_name, table_name in self.sheets.items():
            df = pd.read_excel(self.file_path, sheet_name=sheet_name,
                               header=self.HEADER_ROW)
            df.columns = [self._clean_column_name(c) for c in df.columns]
            tables[table_name] = df.dropna(how="all")
        return tables