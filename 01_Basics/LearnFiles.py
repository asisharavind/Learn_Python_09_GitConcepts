"""
PYTHON FILE & DIRECTORY MANAGEMENT FOR TEST AUTOMATION
======================================================
1. Environment Variables & System Paths (os.environ)
2. Modern Path Resolution (pathlib.Path)
3. Reading, Writing & Appending Text Files
4. Legacy OS Directory & File Operations (os)
5. Modern Pathlib File Manipulation
6. Working with CSV Data (Lists & Dictionaries)
"""

import csv
import os
import time
from pathlib import Path

# =====================================================================
# SECTION 1: ENVIRONMENT VARIABLES & SYSTEM PATHS (os.environ)
# =====================================================================
# Read external configuration flags (e.g., passed from Jenkins/CI or terminal)
# os.getenv("KEY", "default") prevents KeyError crashes if variable is missing
browser = os.getenv("BROWSER", "chrome")  # Target browser
env_name = os.getenv("EXEC_ENV", "QA")   # Target environment (QA, Staging, Dev)

print(f"Browser: {browser}")
print(f"Environment: {env_name}")

# Map environment flag to target endpoint
ENV_URLS = {
    "QA": "https://qa.demoqa.com",
    "STAGING": "https://staging.demoqa.com",
    "DEV": "https://dev.demoqa.com"
}
target_url = ENV_URLS.get(env_name, "https://qa.demoqa.com")
print("target url is: " + target_url)

# Read OS-level directories
user_home = os.getenv("USERPROFILE") or os.getenv("HOME")  # Windows / Unix fallback
temp_dir = os.getenv("TEMP")
print(f"User Home: {user_home}")
print(f"Temp Directory: {temp_dir}")

# Set global environment variable for the current execution process
os.environ["HEADLESS"] = "true"  # Enables headless browser execution


# =====================================================================
# SECTION 2: MODERN PATH RESOLUTION (pathlib.Path)
# =====================================================================
# Never hardcode paths like "C:/Users/...". Always use relative project paths.
THIS_FILE = Path(__file__).resolve()        # Absolute path to this .py script
CURRENT_DIR = THIS_FILE.parent              # Folder containing this script (01_Basics)
PROJECT_ROOT = THIS_FILE.parents[1]         # Project root directory

print(f"Script Path: {THIS_FILE}")
print(f"Current Directory: {CURRENT_DIR}")
print(f"Project Root: {PROJECT_ROOT}")

# Construct framework subdirectories dynamically
LOGS_DIR = PROJECT_ROOT / "logs"
CONFIG_FILE = PROJECT_ROOT / "config" / "env_config.json"
SCREENSHOTS_DIR = PROJECT_ROOT / "reports" / "screenshots"

# Ensure directories exist prior to writing files
LOGS_DIR.mkdir(parents=True, exist_ok=True)
CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)  # Create parent folder for file
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)


# =====================================================================
# SECTION 3: READING, WRITING & APPENDING TEXT FILES
# =====================================================================
SPIDER_FILE = CURRENT_DIR / "spider.txt"
LOG_FILE = CURRENT_DIR / "app_logs.txt"

# 1. Write mode ("w"): Creates file or completely overwrites existing content
with open(SPIDER_FILE, "w", encoding="utf-8") as file:
    file.write("The itsy bitsy spider climbed up the waterspout.\n")

with open(LOG_FILE, "w", encoding="utf-8") as file:
    file.write("[INFO] Application started successfully.\n")
    file.write("[INFO] Navigated to login page.\n")
    file.write("[SUCCESS] User authentication completed.\n")

# 2. Read mode ("r"): Read line-by-line
print("\n=== READING SPIDER.TXT ===")
with open(SPIDER_FILE, "r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line.strip())

print("\n=== READING APP_LOGS.TXT ===")
with open(LOG_FILE, "r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line.strip())

# 3. Append mode ("a"): Adds new lines to the end of the file
with open(LOG_FILE, "a", encoding="utf-8") as file:
    file.write("[WARNING] Memory usage exceeded 80%.\n")

# 4. Safe Prepend Pattern: Read into memory, add header, then overwrite
with open(LOG_FILE, "r", encoding="utf-8") as file:
    existing_content = file.read()

with open(LOG_FILE, "w", encoding="utf-8") as file:
    file.write("[HEADER] Execution Audit Log\n" + existing_content)


# =====================================================================
# SECTION 4: LEGACY OS DIRECTORY & FILE OPERATIONS (os)
# =====================================================================
sample_file = CURRENT_DIR / "audit_trail.log"

# Create log file for inspection
with open(sample_file, "w", encoding="utf-8") as f:
    f.write("2026-08-29 10:00:00 - TEST PASSED: Login Verification\n")

# Metadata Inspection
print(f"\nFile Size: {os.path.getsize(sample_file)} bytes")
mod_timestamp = os.path.getmtime(sample_file)
print(f"Last Modified: {time.ctime(mod_timestamp)}")
print(f"Absolute Path: {os.path.abspath(sample_file)}")

# Working directory & paths
print(f"Current Directory: {os.getcwd()}")
combined_path = os.path.join(os.getcwd(), "01_Basics", "execution_report.json")
print(f"Joined Path: {combined_path}")

# Folder Operations
evidence_folder = CURRENT_DIR / "test_evidence"
os.mkdir(evidence_folder)
print(f"Contents of 01_Basics: {os.listdir(CURRENT_DIR)}")
os.rmdir(evidence_folder)

# File Manipulation (Create, Rename, Delete)
temp_log = CURRENT_DIR / "temp_run.tmp"
renamed_log = CURRENT_DIR / "archived_run.tmp"

with open(temp_log, "w", encoding="utf-8") as file:
    pass  # Touch file empty

os.rename(temp_log, renamed_log)
os.remove(renamed_log)
os.remove(sample_file)


# =====================================================================
# SECTION 5: MODERN PATHLIB EQUIVALENTS (Recommended)
# =====================================================================
artifact_file = CURRENT_DIR / "suite_metrics.csv"

# Touch creates an empty file instantly
artifact_file.touch()

print("Pathlib Size Check:", artifact_file.stat().st_size)
print("File Exists?:", artifact_file.exists())

# Rename file via Path object
new_artifact_file = artifact_file.with_name("suite_metrics_v2.csv")
artifact_file.rename(new_artifact_file)

# Delete file safely
new_artifact_file.unlink(missing_ok=True)


# =====================================================================
# SECTION 6: WORKING WITH CSV DATA (Lists & Dictionaries)
# =====================================================================
CSV_FILE = CURRENT_DIR / "test_execution_data.csv"
DICT_CSV_FILE = CURRENT_DIR / "user_credentials.csv"

# 1. Write Standard CSV (Using Lists)
header = ["Test_ID", "Suite_Name", "Status"]
rows = [
    ["TC001", "Login_Suite", "PASS"],
    ["TC002", "Checkout_Suite", "FAIL"],
    ["TC003", "Payment_Suite", "SKIP"],
]

with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

# 2. Read Standard CSV
print("\n--- READING STANDARD CSV ---")
with open(CSV_FILE, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"Row: {row}")

# 3. Write Dictionary CSV (DictWriter - Preferred for QE)
fieldnames = ["user_id", "username", "role"]
dict_data = [
    {"user_id": 101, "username": "qa_tester_1", "role": "Admin"},
    {"user_id": 102, "username": "qa_tester_2", "role": "Standard"},
]

with open(DICT_CSV_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dict_data)

# 4. Read Dictionary CSV (DictReader - Preferred for QE)
print("\n--- READING CSV WITH DICTREADER ---")
with open(DICT_CSV_FILE, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"User: {row['username']} | Role: {row['role']}")