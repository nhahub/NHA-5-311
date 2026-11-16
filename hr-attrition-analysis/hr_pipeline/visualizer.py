# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 17:18:14 2026

@author: Admin
"""

import matplotlib.pyplot as plt
import seaborn as sns

from hr_pipeline.config import CHARTS_DIR


class HRVisualizer:
    """Draws the EDA charts and saves them as images."""

    NUMERIC_COLUMNS = [
        "Age", "TenureYears", "MonthlySalary", "BonusPercent", "PerformanceRating",
        "TargetAchievementPct", "TrainingHours", "EngagementScore", "JobSatisfaction",
        "WorkLifeBalance", "ProjectsCompleted", "RevenueContribution", "AttritionFlag",
    ]

    def __init__(self, df, output_dir=CHARTS_DIR):
        self.df = df
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.overall_rate = df["AttritionFlag"].mean() * 100
        sns.set_theme(style="whitegrid")

    def _save_and_show(self, filename):
        """Save the current figure as an image, then display it."""
        plt.tight_layout()
        plt.savefig(self.output_dir / filename, dpi=150)
        plt.show()
        plt.close()

    def plot_attrition_count(self):
        """Chart 1: how many employees stayed vs left."""
        plt.figure(figsize=(5, 4))
        sns.countplot(data=self.df, x="Attrition")
        plt.title("Employees: Stayed vs Left")
        self._save_and_show("chart1_attrition_count.png")

    def plot_attrition_by_department(self):
        """Chart 2: attrition rate for each department."""
        rate = self.df.groupby("Department")["AttritionFlag"].mean().mul(100).sort_values()
        plt.figure(figsize=(7, 4))
        rate.plot(kind="barh", color="steelblue")
        plt.axvline(self.overall_rate, color="red", linestyle="--",
                    label=f"Average {self.overall_rate:.1f}%")
        plt.xlabel("Attrition Rate %")
        plt.title("Attrition Rate by Department")
        plt.legend()
        self._save_and_show("chart2_attrition_dept.png")

    def plot_attrition_drivers(self):
        """Chart 3: attrition by tenure, engagement level and salary band."""
        columns = ["TenureGroup", "EngagementLevel", "SalaryBand"]
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        for ax, col in zip(axes, columns):
            rate = self.df.groupby(col, observed=True)["AttritionFlag"].mean().mul(100)
            rate.plot(kind="bar", ax=ax, color="indianred")
            ax.axhline(self.overall_rate, color="black", linestyle="--")
            ax.set_title(f"Attrition % by {col}")
            ax.set_ylabel("Attrition Rate %")
            ax.set_xlabel("")
            ax.tick_params(axis="x", rotation=30)
        self._save_and_show("chart3_attrition_drivers.png")

    def plot_engagement_boxplot(self):
        """Chart 4: engagement score for employees who stayed vs left."""
        plt.figure(figsize=(6, 4))
        sns.boxplot(data=self.df, x="Attrition", y="EngagementScore")
        plt.title("Engagement Score: Stayed vs Left")
        self._save_and_show("chart4_engagement_box.png")

    def plot_correlation_heatmap(self):
        """Chart 5: correlation between the numeric columns."""
        plt.figure(figsize=(11, 8))
        sns.heatmap(self.df[self.NUMERIC_COLUMNS].corr(), annot=True, fmt=".2f",
                    cmap="coolwarm", center=0)
        plt.title("Correlation Heatmap")
        self._save_and_show("chart5_correlation.png")

    def plot_all(self):
        """Draw and save all charts."""
        self.plot_attrition_count()
        self.plot_attrition_by_department()
        self.plot_attrition_drivers()
        self.plot_engagement_boxplot()
        self.plot_correlation_heatmap()