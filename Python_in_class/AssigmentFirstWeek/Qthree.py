# 3. Dataset Validation Checker 
# Create a program that: 
# ● Takes total rows, missing rows, and duplicate rows from user input. 
# ● Calculates clean data percentage using arithmetic operators. 
# ● Uses conditionals: 
# ○ ≥ 95% clean → “Production Ready” 
# ○ 80–94% → “Needs Cleaning” 
# ○ Below 80% → “Poor Dataset” 
# ● Use explicit type casting for calculations. 

total_rows = int(input("Enter total rows: "))
missing_rows = int(input("Enter missing rows: "))
duplicate_rows = int(input("Enter duplicate rows: "))

clear_rows = total_rows - (missing_rows + duplicate_rows)
clean_data_percentage = (clear_rows / total_rows) * 100

if clean_data_percentage >= 95:
    print("Production Ready")
elif 80 <= clean_data_percentage < 95:
    print("Needs Cleaning") 
else:    print("Poor Dataset")


type_cast = float(clean_data_percentage)
print(f"Clean Data Percentage: {type_cast:.2f}%")