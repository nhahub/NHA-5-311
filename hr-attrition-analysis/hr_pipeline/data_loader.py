# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:17:02 2026

@author: Admin
"""

import pandas as pd

from hr_pipeline.config import RAW_DATA_PATH, RAW_SHEET_NAME


class HRDataLoader:
    """Responsible for reading the raw HR data from Excel."""

    def __init__(self, file_path=RAW_DATA_PATH, sheet_name=RAW_SHEET_NAME):
        self.file_path = file_path
        self.sheet_name = sheet_name

    def load(self):
        """Read the Excel sheet and return it as a DataFrame."""
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")
        return pd.read_excel(self.file_path, sheet_name=self.sheet_name)
