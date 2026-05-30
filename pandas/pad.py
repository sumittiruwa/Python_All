"""
=========================================================
  PANDAS PRACTICE FILE — uses large_dataset.xlsx
  Run each section one at a time to learn each command.
  File needed: large_dataset.xlsx (in the same folder)
=========================================================
"""

import pandas as pd
import numpy as np

FILE = "large_dataset.xlsx"   # adjust path if needed

# ─────────────────────────────────────────────────────────────
# SECTION 1 — LOADING DATA
# ─────────────────────────────────────────────────────────────
print("\n===== SECTION 1 : LOADING DATA =====")

# Load one sheet
emp = pd.read_excel(FILE, sheet_name="Employee Database", header=1)
sales = pd.read_excel(FILE, sheet_name="Monthly Sales",    header=1)
students = pd.read_excel(FILE, sheet_name="Student Records", header=1)
inventory = pd.read_excel(FILE, sheet_name="Inventory",    header=1)

# Load all sheets at once into a dict
all_sheets = pd.read_excel(FILE, sheet_name=None, header=1)
print("Sheets loaded:", list(all_sheets.keys()))

# Load only specific columns (saves memory on huge files)
emp_light = pd.read_excel(FILE, sheet_name="Employee Database",
                          header=1,
                          usecols=["Emp ID", "Full Name", "Department",
                                   "Base Salary (NPR)", "Performance Score"])
print("Light load shape:", emp_light.shape)


# ─────────────────────────────────────────────────────────────
# SECTION 2 — VIEWING & INSPECTING
# ─────────────────────────────────────────────────────────────
print("\n===== SECTION 2 : VIEWING & INSPECTING =====")

print(emp.head())            # first 5 rows
print(emp.tail(3))           # last 3 rows
print(emp.shape)             # (rows, cols)
print(emp.columns.tolist())  # column names
print(emp.dtypes)            # data types per column
emp.info()                   # non-null counts + types
print(emp.describe())        # stats for numeric columns
print(emp.describe(include="object"))  # stats for string columns
print(emp.isnull().sum())    # missing values per column
print(emp.nunique())         # unique values per column
print(emp.sample(5))         # 5 random rows


# ─────────────────────────────────────────────────────────────
# SECTION 3 — SELECTING & FILTERING
# ─────────────────────────────────────────────────────────────
print("\n===== SECTION 3 : SELECTING & FILTERING =====")

# Single column → Series
print(emp["Department"].head())

# Multiple columns → DataFrame
print(emp[["Full Name", "Department", "Base Salary (NPR)"]].head())

# loc  — label-based
print(emp.loc[0:4, "Full Name":"Department"])

# iloc — position-based (0-indexed)
print(emp.iloc[0:5, 0:4])

# Boolean filter — salary > 100,000
high_earners = emp[emp["Base Salary (NPR)"] > 100_000]
print("High earners:", len(high_earners))

# Multiple conditions (AND)
eng_senior = emp[
    (emp["Department"] == "Engineering") &
    (emp["Job Grade"] == "Senior")
]
print("Senior Engineers:", len(eng_senior))

# Multiple conditions (OR)
leave_or_resigned = emp[
    (emp["Status"] == "On Leave") |
    (emp["Status"] == "Resigned")
]
print("Not active:", len(leave_or_resigned))

# isin — filter multiple values at once
ktm_pok = emp[emp["Location"].isin(["Kathmandu", "Pokhara"])]
print("KTM + Pokhara employees:", len(ktm_pok))

# NOT isin
other_cities = emp[~emp["Location"].isin(["Kathmandu", "Pokhara"])]
print("Other cities:", len(other_cities))

# query — SQL-like readable syntax
result = emp.query('`Base Salary (NPR)` > 80000 and Department == "Finance"')
print("Finance salary > 80k:", len(result))

# Get a single scalar value fast
first_salary = emp.at[0, "Base Salary (NPR)"]
print("First employee salary:", first_salary)


# ─────────────────────────────────────────────────────────────
# SECTION 4 — CLEANING DATA
# ─────────────────────────────────────────────────────────────
print("\n===== SECTION 4 : CLEANING DATA =====")

# Drop rows with any NaN
clean = emp.dropna()
print("Rows after dropna:", len(clean))

# Drop columns with any NaN
clean_cols = emp.dropna(axis=1)
print("Cols after dropna axis=1:", len(clean_cols.columns))

# Fill NaN with a value
filled = emp["Performance Score"].fillna(emp["Performance Score"].mean())

# Forward fill (useful in time-series)
sales_ffill = sales.copy()
sales_ffill["Discount %"] = sales_ffill["Discount %"].ffill()

# Remove duplicates
dedup = emp.drop_duplicates(subset=["Full Name"])
print("After dedup:", len(dedup))

# Rename columns
emp2 = emp.rename(columns={
    "Base Salary (NPR)": "Salary",
    "Performance Score": "PerfScore"
})
print(emp2[["Salary", "PerfScore"]].head(2))

# Change data types
emp["Experience (Yrs)"] = emp["Experience (Yrs)"].astype(float)

# String cleaning
emp["Department_clean"] = emp["Department"].str.strip().str.upper()
print(emp["Department_clean"].value_counts())

# Reset index after filtering
filtered = emp[emp["Status"] == "Active"].reset_index(drop=True)
print("Active employees reset index:", filtered.index[:5].tolist())


# ─────────────────────────────────────────────────────────────
# SECTION 5 — ADDING & MODIFYING COLUMNS
# ─────────────────────────────────────────────────────────────
print("\n===== SECTION 5 : ADDING & MODIFYING COLUMNS =====")

# Arithmetic new column
emp["Monthly Salary"] = emp["Base Salary (NPR)"] / 12

# Apply a lambda function
emp["Salary Band"] = emp["Base Salary (NPR)"].apply(
    lambda x: "High" if x > 100_000 else ("Mid" if x > 50_000 else "Low")
)
print(emp["Salary Band"].value_counts())

# assign() — chainable, non-mutating
emp = emp.assign(
    Tax = emp["Base Salary (NPR)"] * 0.10,
    Net_Salary = lambda d: d["Base Salary (NPR)"] - d["Tax"]
)
print(emp[["Base Salary (NPR)", "Tax", "Net_Salary"]].head(3))

# pd.cut — bin continuous values into categories
emp["Exp Group"] = pd.cut(
    emp["Experience (Yrs)"],
    bins=[0, 2, 5, 10, 50],
    labels=["Fresher", "Junior", "Mid", "Senior"]
)
print(emp["Exp Group"].value_counts())

# pd.get_dummies — one-hot encoding
dept_dummies = pd.get_dummies(emp["Department"], prefix="Dept")
print(dept_dummies.head(3))

# Drop a column
emp_nodrop = emp.drop("Department_clean", axis=1)


# ─────────────────────────────────────────────────────────────
# SECTION 6 — SORTING & RANKING
# ─────────────────────────────────────────────────────────────
print("\n===== SECTION 6 : SORTING & RANKING =====")

# Sort by one column
top_earners = emp.sort_values("Base Salary (NPR)", ascending=False).head(10)
print(top_earners[["Full Name", "Department", "Base Salary (NPR)"]])

# Sort by multiple columns
emp_sorted = emp.sort_values(
    ["Department", "Base Salary (NPR)"],
    ascending=[True, False]
)

# nlargest / nsmallest — faster than sort + head
print(emp.nlargest(5, "Performance Score")[["Full Name", "Performance Score"]])
print(emp.nsmallest(5, "Attendance %")[["Full Name", "Attendance %"]])

# Rank
emp["Salary Rank"] = emp["Base Salary (NPR)"].rank(ascending=False, method="dense")
print(emp[["Full Name", "Base Salary (NPR)", "Salary Rank"]].head(5))


# ─────────────────────────────────────────────────────────────
# SECTION 7 — GROUPBY & AGGREGATION
# ─────────────────────────────────────────────────────────────
print("\n===== SECTION 7 : GROUPBY & AGGREGATION =====")

# Simple groupby + aggregate
dept_salary = emp.groupby("Department")["Base Salary (NPR)"].sum()
print(dept_salary.sort_values(ascending=False))

# Multiple aggregations
dept_stats = emp.groupby("Department").agg(
    headcount=("Emp ID", "count"),
    avg_salary=("Base Salary (NPR)", "mean"),
    max_salary=("Base Salary (NPR)", "max"),
    avg_perf=("Performance Score", "mean")
).round(2)
print(dept_stats)

# Group by multiple columns
loc_dept = emp.groupby(["Location", "Department"])["Base Salary (NPR)"].mean().unstack()
print(loc_dept.head())

# transform — keeps original shape (useful for normalising per group)
emp["Dept Avg Salary"] = emp.groupby("Department")["Base Salary (NPR)"].transform("mean")
emp["Salary vs Dept Avg"] = emp["Base Salary (NPR)"] - emp["Dept Avg Salary"]

# size() — count rows per group
print(emp.groupby("Status").size())

# Sales groupby
monthly_rev = sales.groupby(["Year", "Month"])["Revenue (NPR)"].sum().reset_index()
print(monthly_rev.head(12))

# Pivot table
pivot = sales.pivot_table(
    values="Revenue (NPR)",
    index="Region",
    columns="Year",
    aggfunc="sum",
    fill_value=0
)
print(pivot)

# Rolling mean (needs numeric index)
sales_sorted = sales.sort_values(["Year", "Month"]).reset_index(drop=True)
sales_sorted["Rolling 7 Avg Rev"] = sales_sorted["Revenue (NPR)"].rolling(7).mean()

# Cumulative sum
sales_sorted["Cumulative Revenue"] = sales_sorted["Revenue (NPR)"].cumsum()
print(sales_sorted[["Revenue (NPR)", "Rolling 7 Avg Rev", "Cumulative Revenue"]].tail(10))


# ─────────────────────────────────────────────────────────────
# SECTION 8 — MERGING & JOINING
# ─────────────────────────────────────────────────────────────
print("\n===== SECTION 8 : MERGING & JOINING =====")

# Create a lookup table to merge
dept_budget = pd.DataFrame({
    "Department": ["Engineering","Sales","Marketing","HR","Finance",
                   "Operations","Legal","Product","Design","Support"],
    "Budget (NPR)": [5_000_000, 3_500_000, 2_000_000, 1_500_000, 2_500_000,
                     3_000_000, 1_200_000, 2_800_000, 1_800_000, 1_600_000]
})

# Inner join (only rows matching in both)
emp_budget = pd.merge(emp, dept_budget, on="Department", how="inner")
print("After merge:", emp_budget.shape)
print(emp_budget[["Full Name", "Department", "Base Salary (NPR)", "Budget (NPR)"]].head(5))

# Left join — keep all emp rows
emp_budget_left = pd.merge(emp, dept_budget, on="Department", how="left")

# Concat — stack DataFrames vertically
emp_half1 = emp.iloc[:250].copy()
emp_half2 = emp.iloc[250:].copy()
emp_rejoined = pd.concat([emp_half1, emp_half2], ignore_index=True)
print("Rejoined shape:", emp_rejoined.shape)

# Concat horizontally (axis=1)
bonus_df = emp[["Emp ID", "Bonus %"]].copy()
salary_df = emp[["Emp ID", "Base Salary (NPR)"]].copy()
combined = pd.concat([salary_df, bonus_df.drop("Emp ID", axis=1)], axis=1)
print(combined.head(3))


# ─────────────────────────────────────────────────────────────
# SECTION 9 — RESHAPING
# ─────────────────────────────────────────────────────────────
print("\n===== SECTION 9 : RESHAPING =====")

# melt — wide to long
score_wide = students[["Student ID", "Sub1 Score", "Sub2 Score", "Sub3 Score"]].head(10)
score_long = score_wide.melt(
    id_vars=["Student ID"],
    value_vars=["Sub1 Score", "Sub2 Score", "Sub3 Score"],
    var_name="Subject Slot",
    value_name="Score"
)
print(score_long.head(10))

# pivot — long back to wide
score_back = score_long.pivot(
    index="Student ID", columns="Subject Slot", values="Score"
)
print(score_back.head(5))

# Transpose
sample = emp[["Department","Base Salary (NPR)","Performance Score"]].head(4)
print(sample.T)


# ─────────────────────────────────────────────────────────────
# SECTION 10 — DATETIME OPERATIONS
# ─────────────────────────────────────────────────────────────
print("\n===== SECTION 10 : DATETIME =====")

# Convert to datetime
emp["Join Date"] = pd.to_datetime(emp["Join Date"])
emp["Date of Birth"] = pd.to_datetime(emp["Date of Birth"])

# Extract components
emp["Join Year"]  = emp["Join Date"].dt.year
emp["Join Month"] = emp["Join Date"].dt.month
emp["Join Day"]   = emp["Join Date"].dt.day_name()
emp["Join Quarter"] = emp["Join Date"].dt.quarter

# Duration (tenure)
today = pd.Timestamp("2024-12-31")
emp["Tenure (days)"] = (today - emp["Join Date"]).dt.days
emp["Tenure (years)"] = (emp["Tenure (days)"] / 365.25).round(1)

print(emp[["Full Name", "Join Date", "Join Year", "Join Day", "Tenure (years)"]].head(5))

# Age from DOB
emp["Age"] = ((today - emp["Date of Birth"]).dt.days / 365.25).fillna(0).astype(int)
print(emp[["Full Name", "Date of Birth", "Age"]].head(5))

# Employees who joined in Q1
q1_joiners = emp[emp["Join Quarter"] == 1]
print("Q1 joiners:", len(q1_joiners))

# Add days to a date
emp["Review Date"] = emp["Join Date"] + pd.Timedelta(days=365)


# ─────────────────────────────────────────────────────────────
# SECTION 11 — STRING OPERATIONS
# ─────────────────────────────────────────────────────────────
print("\n===== SECTION 11 : STRING OPERATIONS =====")

# Uppercase / lowercase
emp["Dept Upper"] = emp["Department"].str.upper()
emp["Name Lower"] = emp["Full Name"].str.lower()

# String length
emp["Name Length"] = emp["Full Name"].str.len()

# Contains (regex by default)
has_ai = inventory["Product Name"].str.contains("SSD", case=False, na=False)
print("SSD products:", inventory[has_ai]["Product Name"].tolist())

# Starts / ends with
dr_names = emp[emp["Full Name"].str.startswith("D")]
print("Names starting with D:", len(dr_names))

# Split into parts
emp["First Name"] = emp["Full Name"].str.split(" ").str[0]
emp["Last Name"]  = emp["Full Name"].str.split(" ").str[-1]

# Extract digits with regex
emp["Emp Number"] = emp["Emp ID"].str.extract(r"(\d+)")[0].fillna(0).astype(int)

# Replace
sales["Channel Clean"] = sales["Channel"].str.replace("Store", "Shop", regex=False)

# Strip whitespace
emp["Email Clean"] = emp["Email"].str.strip().str.lower()


# ─────────────────────────────────────────────────────────────
# SECTION 12 — STATISTICS & MATH
# ─────────────────────────────────────────────────────────────
print("\n===== SECTION 12 : STATISTICS =====")

# Basic stats
print("Mean salary:", emp["Base Salary (NPR)"].mean().round(0))
print("Median salary:", emp["Base Salary (NPR)"].median())
print("Std salary:", emp["Base Salary (NPR)"].std().round(0))

# Correlation between salary and performance
corr = emp["Base Salary (NPR)"].corr(emp["Performance Score"])
print(f"Salary ↔ Performance correlation: {corr:.3f}")

# Full correlation matrix
num_cols = emp.select_dtypes(include="number")
print(num_cols.corr().round(2))

# Percentiles
print(emp["Base Salary (NPR)"].quantile([0.25, 0.5, 0.75]))

# Clip outliers — cap salary between 5th and 95th percentile
p5  = emp["Base Salary (NPR)"].quantile(0.05)
p95 = emp["Base Salary (NPR)"].quantile(0.95)
emp["Salary Clipped"] = emp["Base Salary (NPR)"].clip(lower=p5, upper=p95)

# % change in sales revenue row-by-row
sales_sorted["Rev % Change"] = sales_sorted["Revenue (NPR)"].pct_change().round(4)
print(sales_sorted[["Revenue (NPR)", "Rev % Change"]].head(10))

# Absolute value (useful for differences)
emp["Diff from Avg"] = (emp["Base Salary (NPR)"] - emp["Base Salary (NPR)"].mean()).abs()


# ─────────────────────────────────────────────────────────────
# SECTION 13 — EXPORTING
# ─────────────────────────────────────────────────────────────
print("\n===== SECTION 13 : EXPORTING =====")

# Save to CSV
emp[["Emp ID", "Full Name", "Department", "Base Salary (NPR)", "Status"]].to_csv(
    "emp_export.csv", index=False
)
print("Saved emp_export.csv")

# Save filtered data to Excel
with pd.ExcelWriter("filtered_output.xlsx", engine="openpyxl") as writer:
    emp[emp["Status"] == "Active"].to_excel(writer, sheet_name="Active Employees", index=False)
    sales[sales["Year"] == 2024].to_excel(writer, sheet_name="Sales 2024", index=False)
    students[students["Pass/Fail"] == "Pass"].to_excel(writer, sheet_name="Passed Students", index=False)
print("Saved filtered_output.xlsx")

# Convert to dict (list of records — useful for APIs/JSON)
sample_dict = emp.head(3)[["Emp ID", "Full Name", "Department"]].to_dict("records")
print(sample_dict)

# Markdown table (useful for README / reports)
print(emp.head(3)[["Emp ID", "Full Name", "Department"]].to_markdown(index=False))


# ─────────────────────────────────────────────────────────────
# SECTION 14 — PERFORMANCE TIPS
# ─────────────────────────────────────────────────────────────
print("\n===== SECTION 14 : PERFORMANCE TIPS =====")

# Check memory usage before
print("Memory before:\n", emp.memory_usage(deep=True))

# Convert string columns to 'category' — saves memory
for col in ["Department", "Job Grade", "Location", "Gender", "Status"]:
    emp[col] = emp[col].astype("category")

print("Memory after category conversion:\n", emp.memory_usage(deep=True))

# Select only numeric columns
numeric_only = emp.select_dtypes(include="number")
print("Numeric columns:", numeric_only.columns.tolist())

# pipe() — chain operations cleanly
def add_tax(df, rate=0.10):
    return df.assign(Tax=df["Base Salary (NPR)"] * rate)

def flag_high_earner(df, threshold=100_000):
    return df.assign(HighEarner=df["Base Salary (NPR)"] > threshold)

result = (
    emp
    .pipe(add_tax, rate=0.10)
    .pipe(flag_high_earner, threshold=100_000)
)
print(result[["Full Name", "Base Salary (NPR)", "Tax", "HighEarner"]].head(5))

# eval() — fast expression evaluation
emp = emp.assign(**{"Base Salary (NPR)": emp["Base Salary (NPR)"].astype(float)})
emp["Quick Net"] = emp.eval("`Base Salary (NPR)` * 0.9")
print(emp[["Full Name", "Base Salary (NPR)", "Quick Net"]].head(3))


# ─────────────────────────────────────────────────────────────
# BONUS — MINI ANALYSIS PROJECT
# ─────────────────────────────────────────────────────────────
print("\n===== BONUS : MINI ANALYSIS =====")

# Q1: Which department has the highest average salary?
best_dept = (
    emp.groupby("Department")["Base Salary (NPR)"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)
best_dept.columns = ["Department", "Avg Salary"]
print("Dept with highest avg salary:", best_dept.iloc[0].to_dict())

# Q2: Top 5 products by total revenue
top_products = (
    sales.groupby("Product")["Revenue (NPR)"]
    .sum()
    .nlargest(5)
    .reset_index()
)
print("\nTop 5 products by revenue:\n", top_products)

# Q3: Students with GPA > 3.5
top_students = students[students["GPA"] > 3.5][["Student ID","Full Name","Program","GPA"]]
print(f"\nStudents with GPA > 3.5: {len(top_students)}")
print(top_students.head())

# Q4: Inventory items that need restocking (stock < reorder level)
restock_needed = inventory[
    inventory["Stock Qty"] < inventory["Reorder Level"]
][["SKU", "Product Name", "Stock Qty", "Reorder Level", "Status"]]
print(f"\nItems needing restock: {len(restock_needed)}")
print(restock_needed.head())

# Q5: Year-over-year sales growth
yoy = (
    sales.groupby("Year")["Revenue (NPR)"]
    .sum()
    .reset_index()
)
yoy["YoY Growth %"] = yoy["Revenue (NPR)"].pct_change() * 100
print("\nYear-over-Year Revenue:\n", yoy)

print("\n✅ All sections complete! Check emp_export.csv and filtered_output.xlsx.")