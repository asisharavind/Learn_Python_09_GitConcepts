import pandas as pd

# 1. Setup the DataFrame
data = {
    "Employee": ["Alice", "Bob", "Charlie"],
    "Department": ["Engineering", "Marketing", "Sales"],
    "Salary": [85000, 62000, 71000]
}
df = pd.DataFrame(data)

# Define a budget threshold for our condition
high_salary_tier = 70000

print("--- Processing Employees with Loops and IF Conditions ---")

# 2. Iterating through rows using a FOR loop
for index, row in df.iterrows():
    # Extract row values into readable variables
    name = row["Employee"]
    dept = row["Department"]
    salary = row["Salary"]
    
    # 3. Applying IF/ELSE conditions
    if salary > high_salary_tier:
        print(f"⭐ [High Tier] {name} ({dept}) earns ${salary:,} (Above budget limit)")
    else:
        print(f"📉 [Standard Tier] {name} ({dept}) earns ${salary:,} (Within budget limit)")

print("\n--- Summary Count ---")
# Another loop example: Counting how many people are in Engineering
eng_count = 0
for index, row in df.iterrows():
    if row["Department"] == "Engineering":
        eng_count += 1

print(f"Total engineers found: {eng_count}")


# Choosing between a Pandas DataFrame and a Standard Dictionary (dict) depends on your goals: 
# use Dictionaries for simple, structural programming tasks and fast single-item lookups, 
# and use DataFrames when you need to perform calculations, filter rows, or handle large tables of structured information.