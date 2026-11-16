# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 15:32:57 2026

@author: Admin
"""

import pandas as pd


class HRFeatureEngineer:
    """Creates new analysis-ready columns from the clean HR data."""

    REFERENCE_DATE = pd.Timestamp("2026-06-15")

    def __init__(self, df):
        self.df = df.copy()

    def add_age_group(self):
        """Group employees by age."""
        self.df["AgeGroup"] = pd.cut(
            self.df["Age"],
            bins=[21, 30, 40, 50, 60],
            labels=["22-30", "31-40", "41-50", "51+"],
        )

    def add_hire_year(self):
        """Extract the year of hiring."""
        self.df["HireYear"] = self.df["HireDate"].dt.year

    def add_years_since_promotion(self):
        """Years passed since the last promotion."""
        days = (self.REFERENCE_DATE - self.df["LastPromotionDate"]).dt.days
        self.df["YearsSincePromotion"] = (days / 365.25).round(1)

    def add_tenure_group(self):
        """Group employees by years of experience in the company."""
        self.df["TenureGroup"] = pd.cut(
            self.df["TenureYears"],
            bins=[0, 2, 5, 10, 20],
            labels=["0-2 yrs", "2-5 yrs", "5-10 yrs", "10+ yrs"],
        )

    def add_engagement_level(self):
        """Convert the engagement score into Low / Medium / High."""
        self.df["EngagementLevel"] = pd.cut(
            self.df["EngagementScore"],
            bins=[0, 50, 75, 100],
            labels=["Low", "Medium", "High"],
        )

    def add_high_performer(self):
        """1 = performance rating of 4 or more, 0 = otherwise."""
        self.df["HighPerformer"] = (self.df["PerformanceRating"] >= 4).astype(int)

    def create_features(self):
        """Run all feature steps and return the DataFrame."""
        self.add_age_group()
        self.add_hire_year()
        self.add_years_since_promotion()
        self.add_tenure_group()
        self.add_engagement_level()
        self.add_high_performer()
        return self.df