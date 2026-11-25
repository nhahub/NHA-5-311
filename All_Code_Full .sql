USE HR_Project;

-- Step 1: Check Data
SELECT * FROM employees

SELECT COUNT(*) AS TotalRows
FROM employees

SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'employees'

-- Step 2: Explore Data
SELECT Department, COUNT(*) AS EmployeeCount
FROM employees
GROUP BY Department

SELECT Location, COUNT(*) AS EmployeeCount
FROM employees
GROUP BY Location

SELECT JobRole, COUNT(*) AS EmployeeCount
FROM employees
GROUP BY JobRole

-- Step 3: Attrition Overall and by Department
SELECT AttritionFlag, COUNT(*) AS EmployeeCount
FROM employees
GROUP BY AttritionFlag

SELECT Department,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees
FROM employees
GROUP BY Department

SELECT Department,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees
GROUP BY Department
ORDER BY AttritionRate DESC

-- Step 4: Attrition by Age Group
SELECT AgeGroup,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees
GROUP BY AgeGroup
ORDER BY AttritionRate DESC

-- Step 5: Attrition by Tenure
SELECT TenureGroup,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees
GROUP BY TenureGroup
ORDER BY AttritionRate DESC

-- Step 6: Top 5 Job Roles
SELECT TOP 5 JobRole,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees
GROUP BY JobRole
ORDER BY AttritionRate DESC

-- Step 7: Salary Averages
SELECT Department,
       ROUND(AVG(MonthlySalary), 0) AS AvgSalary
FROM employees
GROUP BY Department
ORDER BY AvgSalary DESC

SELECT SalaryBand,
       COUNT(*) AS EmployeeCount,
       ROUND(AVG(MonthlySalary), 0) AS AvgSalary
FROM employees
GROUP BY SalaryBand
ORDER BY AvgSalary DESC

-- Step 8: Attrition by Salary Band
SELECT SalaryBand,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees
GROUP BY SalaryBand
ORDER BY AttritionRate DESC

-- Step 9: Performance, Engagement and Satisfaction
SELECT AttritionFlag,
       COUNT(*) AS EmployeeCount,
       ROUND(AVG(PerformanceRating), 2) AS AvgPerformance,
       ROUND(AVG(EngagementScore), 1) AS AvgEngagement,
       ROUND(AVG(CAST(JobSatisfaction AS FLOAT)), 2) AS AvgSatisfaction
FROM employees
GROUP BY AttritionFlag

-- Step 10: Engagement Level and High Performers
SELECT EngagementLevel,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees
GROUP BY EngagementLevel
ORDER BY AttritionRate DESC

SELECT HighPerformer,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees
GROUP BY HighPerformer

-- Step 11: Promotion Gap
SELECT CASE WHEN YearsSincePromotion < 2 THEN '0-2 yrs'
            WHEN YearsSincePromotion < 5 THEN '2-5 yrs'
            ELSE '5+ yrs' END AS PromotionGap,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees
GROUP BY CASE WHEN YearsSincePromotion < 2 THEN '0-2 yrs'
              WHEN YearsSincePromotion < 5 THEN '2-5 yrs'
              ELSE '5+ yrs' END
ORDER BY AttritionRate DESC

-- Step 12: Gender and Education
SELECT Gender,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees
GROUP BY Gender
ORDER BY AttritionRate DESC

SELECT Education,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees
GROUP BY Education
ORDER BY AttritionRate DESC

-- Step 13: Hire Year Trend
SELECT HireYear,
       COUNT(*) AS HiredEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees
GROUP BY HireYear
ORDER BY HireYear

-- Step 14: High Performers by Salary Band
SELECT SalaryBand,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(HighPerformer AS INT)) AS HighPerformers,
       ROUND(SUM(CAST(HighPerformer AS INT)) * 100.0 / COUNT(*), 1) AS HighPerformerRate
FROM employees
GROUP BY SalaryBand
ORDER BY HighPerformerRate DESC

-- Step 15: Salary Distribution
SELECT SalaryBand,
       COUNT(*) AS EmployeeCount,
       MIN(MonthlySalary) AS MinSalary,
       MAX(MonthlySalary) AS MaxSalary,
       ROUND(AVG(MonthlySalary), 0) AS AvgSalary
FROM employees
GROUP BY SalaryBand
ORDER BY AvgSalary DESC

-- Step 16: Job Role Full Analysis
SELECT JobRole,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees
GROUP BY JobRole
ORDER BY AttritionRate DESC

-- Step 17: Views
GO

CREATE OR ALTER VIEW vw_Attrition_By_Department AS
SELECT Department,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       CAST(ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS DECIMAL(5,1)) AS AttritionRate
FROM employees
GROUP BY Department
GO

SELECT *
FROM vw_Attrition_By_Department
ORDER BY AttritionRate DESC
GO

CREATE OR ALTER VIEW vw_Attrition_By_AgeGroup AS
SELECT AgeGroup,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       CAST(ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS DECIMAL(5,1)) AS AttritionRate
FROM employees
GROUP BY AgeGroup
GO

CREATE OR ALTER VIEW vw_Attrition_By_Tenure AS
SELECT TenureGroup,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       CAST(ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS DECIMAL(5,1)) AS AttritionRate
FROM employees
GROUP BY TenureGroup
GO

CREATE OR ALTER VIEW vw_Attrition_By_SalaryBand AS
SELECT SalaryBand,
       COUNT(*) AS TotalEmployees,
       SUM(CAST(AttritionFlag AS INT)) AS LeftEmployees,
       CAST(ROUND(SUM(CAST(AttritionFlag AS INT)) * 100.0 / COUNT(*), 1) AS DECIMAL(5,1)) AS AttritionRate
FROM employees
GROUP BY SalaryBand
GO

SELECT name AS ViewName
FROM sys.views


GO

-- =====================================================
-- Step 18: CTE بسيط - الأقسام اللي نسبة الـ Attrition فيها أعلى من متوسط الشركة
-- =====================================================
WITH DeptAttrition AS (
    SELECT Department,
           COUNT(*) AS TotalEmployees,
           SUM(AttritionFlag) AS LeftEmployees,
           ROUND(SUM(AttritionFlag) * 100.0 / COUNT(*), 1) AS AttritionRate
    FROM employees
    GROUP BY Department
),
CompanyAvg AS (
    SELECT ROUND(SUM(AttritionFlag) * 100.0 / COUNT(*), 1) AS CompanyRate
    FROM employees
)
SELECT d.Department,
       d.TotalEmployees,
       d.AttritionRate,
       c.CompanyRate,
       ROUND(d.AttritionRate - c.CompanyRate, 1) AS DiffFromCompany
FROM DeptAttrition d
CROSS JOIN CompanyAvg c
WHERE d.AttritionRate > c.CompanyRate
ORDER BY d.AttritionRate DESC;

-- =====================================================
-- Step 19: CTE - الموظفين High Performers اللي سابوا الشركة (خسارة المواهب)
-- =====================================================
WITH LostTalent AS (
    SELECT Department, JobRole, EmployeeID, MonthlySalary
    FROM employees
    WHERE HighPerformer = 1
      AND AttritionFlag = 1
)
SELECT Department,
       COUNT(*) AS LostHighPerformers,
       ROUND(AVG(MonthlySalary), 0) AS AvgSalaryOfLeavers
FROM LostTalent
GROUP BY Department
ORDER BY LostHighPerformers DESC;

-- =====================================================
-- Step 20: عمل جدول مرجعي (Lookup Table) عشان نستخدم JOIN
-- جدول فيه "الهدف المسموح" لنسبة الـ Attrition لكل قسم
-- (الأرقام دي افتراضية - ممكن تغيريها زي ما تحبي)
-- =====================================================
IF OBJECT_ID('Department_Targets', 'U') IS NOT NULL
    DROP TABLE Department_Targets;
GO

CREATE TABLE Department_Targets (
    Department VARCHAR(50) PRIMARY KEY,
    TargetAttritionRate DECIMAL(5,1)
);
GO

INSERT INTO Department_Targets (Department, TargetAttritionRate) VALUES
('Sales', 15.0),
('Marketing', 12.0),
('HR', 10.0),
('Product', 12.0),
('Legal', 8.0),
('Engineering', 12.0),
('Finance', 10.0),
('Operations', 14.0);
GO

-- =====================================================
-- Step 21: INNER JOIN - مقارنة الـ Attrition الفعلي بالهدف
-- =====================================================
WITH DeptAttrition AS (
    SELECT Department,
           COUNT(*) AS TotalEmployees,
           ROUND(SUM(AttritionFlag) * 100.0 / COUNT(*), 1) AS ActualRate
    FROM employees
    GROUP BY Department
)
SELECT d.Department,
       d.TotalEmployees,
       d.ActualRate,
       t.TargetAttritionRate,
       ROUND(d.ActualRate - t.TargetAttritionRate, 1) AS Gap,
       CASE WHEN d.ActualRate > t.TargetAttritionRate THEN 'Above Target'
            ELSE 'Within Target' END AS Status
FROM DeptAttrition d
INNER JOIN Department_Targets t
        ON d.Department = t.Department
ORDER BY Gap DESC;

-- =====================================================
-- Step 22: عمل جدول مرجعي تاني للـ Salary Band + LEFT JOIN
-- =====================================================
IF OBJECT_ID('Band_Info', 'U') IS NOT NULL
    DROP TABLE Band_Info;
GO

CREATE TABLE Band_Info (
    SalaryBand VARCHAR(50) PRIMARY KEY,
    BandLevel INT,
    BandCategory VARCHAR(20)
);
GO

INSERT INTO Band_Info (SalaryBand, BandLevel, BandCategory) VALUES
('Band 1 (Entry)', 1, 'Junior'),
('Band 2 (Mid)', 2, 'Junior'),
('Band 3 (Senior)', 3, 'Mid-Level'),
('Band 4 (Lead)', 4, 'Management'),
('Band 5 (Executive)', 5, 'Management');
GO

-- Attrition حسب فئة الـ Band
SELECT b.BandCategory,
       COUNT(*) AS TotalEmployees,
       SUM(h.AttritionFlag) AS LeftEmployees,
       ROUND(SUM(h.AttritionFlag) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees h
LEFT JOIN Band_Info b
       ON h.SalaryBand = b.SalaryBand
GROUP BY b.BandCategory
ORDER BY AttritionRate DESC;

-- =====================================================
-- Step 23: JOIN مع CTE - هل اللي مرتبه أقل من متوسط قسمه بيسيب أكتر؟
-- =====================================================
WITH DeptAvgSalary AS (
    SELECT Department,
           AVG(MonthlySalary) AS AvgDeptSalary
    FROM employees
    GROUP BY Department
)
SELECT CASE WHEN h.MonthlySalary < d.AvgDeptSalary
            THEN 'Below Dept Average'
            ELSE 'Above Dept Average' END AS SalaryPosition,
       COUNT(*) AS TotalEmployees,
       SUM(h.AttritionFlag) AS LeftEmployees,
       ROUND(SUM(h.AttritionFlag) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees h
INNER JOIN DeptAvgSalary d
        ON h.Department = d.Department
GROUP BY CASE WHEN h.MonthlySalary < d.AvgDeptSalary
              THEN 'Below Dept Average'
              ELSE 'Above Dept Average' END;

-- =====================================================
-- Step 24: CTE + RANK - أعلى Job Role في الـ Attrition جوه كل قسم
-- =====================================================
WITH RoleAttrition AS (
    SELECT Department,
           JobRole,
           COUNT(*) AS TotalEmployees,
           ROUND(SUM(AttritionFlag) * 100.0 / COUNT(*), 1) AS AttritionRate
    FROM employees
    GROUP BY Department, JobRole
),
Ranked AS (
    SELECT *,
           RANK() OVER (PARTITION BY Department ORDER BY AttritionRate DESC) AS RankInDept
    FROM RoleAttrition
)
SELECT Department, JobRole, TotalEmployees, AttritionRate, RankInDept
FROM Ranked
WHERE RankInDept = 1
ORDER BY AttritionRate DESC;

-- =====================================================
-- Step 25: Subquery - موظفين Engagement بتاعهم أقل من متوسط الشركة وسابوا
-- =====================================================
SELECT Department,
       COUNT(*) AS LowEngagementLeavers
FROM employees
WHERE AttritionFlag = 1
  AND EngagementScore < (SELECT AVG(EngagementScore) FROM employees)
GROUP BY Department
ORDER BY LowEngagementLeavers DESC;

-- =====================================================
-- Step 26: Attrition حسب Department و Location (GROUP BY على عمودين + HAVING)
-- =====================================================
SELECT Department,
       Location,
       COUNT(*) AS TotalEmployees,
       SUM(AttritionFlag) AS LeftEmployees,
       ROUND(SUM(AttritionFlag) * 100.0 / COUNT(*), 1) AS AttritionRate
FROM employees
GROUP BY Department, Location
HAVING COUNT(*) >= 20
ORDER BY AttritionRate DESC;

-- =====================================================
-- Step 27: View جديد بيستخدم JOIN (للربط مع Power BI / Tableau)
-- =====================================================
GO
CREATE OR ALTER VIEW vw_Dept_Actual_vs_Target AS
SELECT h.Department,
       COUNT(*) AS TotalEmployees,
       SUM(h.AttritionFlag) AS LeftEmployees,
       CAST(ROUND(SUM(h.AttritionFlag) * 100.0 / COUNT(*), 1) AS DECIMAL(5,1)) AS ActualRate,
       t.TargetAttritionRate
FROM employees h
INNER JOIN Department_Targets t
        ON h.Department = t.Department
GROUP BY h.Department, t.TargetAttritionRate
GO

SELECT * FROM vw_Dept_Actual_vs_Target
ORDER BY ActualRate DESC;
GO
