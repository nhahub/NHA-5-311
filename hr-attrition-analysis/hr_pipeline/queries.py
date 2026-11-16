# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:53:16 2026

@author: Admin
"""

"""SQL Server (T-SQL) queries used in the project, grouped by topic."""

BASIC_QUERIES = {
    "1) First 5 rows (chosen columns)": """
        SELECT TOP 5 EmployeeID, Department, JobRole, MonthlySalary, Attrition
        FROM employees
    """,
    "2) Unique departments": """
        SELECT DISTINCT Department
        FROM employees
        ORDER BY Department
    """,
    "3) Employees in HR who left the company": """
        SELECT TOP 5 EmployeeID, JobRole, Location, MonthlySalary
        FROM employees
        WHERE Department = 'HR' AND Attrition = 'Yes'
        ORDER BY MonthlySalary DESC
    """,
    "4) Top 5 highest salaries": """
        SELECT TOP 5 EmployeeID, Department, JobRole, MonthlySalary
        FROM employees
        ORDER BY MonthlySalary DESC
    """,
    "5) How many employees earn more than 100,000?": """
        SELECT COUNT(*) AS high_earners
        FROM employees
        WHERE MonthlySalary > 100000
    """,
}


AGGREGATE_QUERIES = {
    "1) Company KPIs (no grouping)": """
        SELECT COUNT(*) AS total_employees,
               SUM(AttritionFlag) AS leavers,
               CAST(100.0 * SUM(AttritionFlag) / COUNT(*) AS DECIMAL(5,2)) AS attrition_rate_pct,
               ROUND(AVG(CAST(MonthlySalary AS FLOAT)), 0) AS avg_salary,
               MIN(MonthlySalary) AS min_salary,
               MAX(MonthlySalary) AS max_salary
        FROM employees
    """,
    "2) Headcount per department": """
        SELECT Department, COUNT(*) AS headcount
        FROM employees
        GROUP BY Department
        ORDER BY headcount DESC
    """,
    "3) Attrition rate per department": """
        SELECT Department,
               COUNT(*) AS headcount,
               SUM(AttritionFlag) AS leavers,
               CAST(100.0 * SUM(AttritionFlag) / COUNT(*) AS DECIMAL(5,2)) AS attrition_rate_pct
        FROM employees
        GROUP BY Department
        ORDER BY attrition_rate_pct DESC
    """,
    "4) Salary and performance per department": """
        SELECT Department,
               ROUND(AVG(CAST(MonthlySalary AS FLOAT)), 0) AS avg_salary,
               ROUND(AVG(CAST(PerformanceRating AS FLOAT)), 2) AS avg_rating,
               ROUND(AVG(CAST(EngagementScore AS FLOAT)), 1) AS avg_engagement
        FROM employees
        GROUP BY Department
        ORDER BY avg_salary DESC
    """,
    "5) Attrition rate per tenure group": """
        SELECT TenureGroup,
               COUNT(*) AS headcount,
               CAST(100.0 * SUM(AttritionFlag) / COUNT(*) AS DECIMAL(5,2)) AS attrition_rate_pct
        FROM employees
        GROUP BY TenureGroup
        ORDER BY attrition_rate_pct DESC
    """,
    "6) Locations with attrition above 10% (HAVING)": """
        SELECT Location,
               COUNT(*) AS headcount,
               CAST(100.0 * SUM(AttritionFlag) / COUNT(*) AS DECIMAL(5,2)) AS attrition_rate_pct
        FROM employees
        GROUP BY Location
        HAVING 100.0 * SUM(AttritionFlag) / COUNT(*) > 10
        ORDER BY attrition_rate_pct DESC
    """,
}