"""
MODULE 4: MANAGING DATA AND PROCESSES (COMPLETE MASTER CHEATSHEET)
===================================================================
1. Data Streams & Interactive Input (sys.stdin, sys.stdout, sys.stderr)
2. Command-Line Arguments & Exit Status (sys.argv, sys.exit)
3. Environment Variables (os.environ, os.getenv)
4. Tool Comparison: Pathlib vs OS vs Subprocess
5. Core Subprocess Execution (subprocess.run)
6. Legacy & Specialized Subprocess Wrappers (.call, .check_call, .check_output)
7. Advanced & Asynchronous Processes (.Popen, .poll, .communicate)
8. Advanced Subprocess Management (capture_output, env, check=True)
9. Processing Log Files with Regular Expressions
"""

import sys
import os
import subprocess
import time
import re
from pathlib import Path

# =====================================================================
# SECTION 1: DATA STREAMS & INTERACTIVE INPUT
# =====================================================================
user_name = input("Enter tester name: ")
print(f"Hello, {user_name}!")

# Standard Streams (sys.stdout vs sys.stderr)
sys.stdout.write("Standard Output: Test execution starting...\n")
sys.stderr.write("Standard Error:  [WARNING] High CPU usage detected!\n")


# =====================================================================
# SECTION 2: COMMAND-LINE ARGUMENTS & EXIT STATUS
# =====================================================================
script_name = sys.argv[0]
print(f"Executing Script: {script_name}")

if len(sys.argv) > 1:
    print(f"Command-line arguments received: {sys.argv[1:]}")
else:
    print("No CLI arguments passed.")

# Exit Status Code (0 = Success, Non-Zero = Error)
# sys.exit(0)  # Terminates script cleanly


# =====================================================================
# SECTION 3: ENVIRONMENT VARIABLES
# =====================================================================
execution_env = os.getenv("EXEC_ENV", "DEVELOPMENT")
print(f"Current Execution Environment: {execution_env}")

os.environ["QA_SUITE_READY"] = "TRUE"


# =====================================================================
# SECTION 4: TOOL COMPARISON (PATHLIB vs OS vs SUBPROCESS)
# =====================================================================
# Task A: Get Current Working Directory
cwd_pathlib = Path.cwd()                          # Object-oriented & modern (Best)
cwd_os = os.getcwd()                              # Legacy OS module
cwd_sub = subprocess.check_output(["pwd"] if os.name != "nt" else ["cmd", "/c", "cd"], text=True).strip()

# Task B: Create a Directory
dir_name = "demo_folder"
Path(f"{dir_name}_pathlib").mkdir(exist_ok=True)  # Pathlib
os.mkdir(f"{dir_name}_os")                         # OS
subprocess.run(["cmd", "/c", "mkdir", f"{dir_name}_sub"] if os.name == "nt" else ["mkdir", f"{dir_name}_sub"])


# =====================================================================
# SECTION 5: CORE SUBPROCESS EXECUTION (subprocess.run)
# =====================================================================
command = ["cmd", "/c", "dir"] if os.name == "nt" else ["ls", "-l"]

result = subprocess.run(command, capture_output=True, text=True)

print(f"\nSubprocess Exit Code: {result.returncode}")
print("--- Command Standard Output ---")
print(result.stdout[0:200])


# =====================================================================
# SECTION 6: LEGACY & SPECIALIZED WRAPPERS
# =====================================================================
echo_cmd = ["cmd", "/c", "echo", "Hello Automation"] if os.name == "nt" else ["echo", "Hello Automation"]

# 1. call(): Returns ONLY the return code (0 = Success)
code = subprocess.call(echo_cmd)
print(f"call() Exit Code: {code}")

# 2. check_call(): Returns code 0, but RAISES CalledProcessError if process fails
try:
    subprocess.check_call(echo_cmd)
except subprocess.CalledProcessError as err:
    print(f"check_call failed with code: {err.returncode}")

# 3. check_output(): Directly returns the output text (Raises CalledProcessError on fail)
output = subprocess.check_output(echo_cmd, text=True)
print(f"check_output(): {output.strip()}")

# 4. Decoding raw bytes manually (when text=True is omitted)
raw_bytes = subprocess.run(echo_cmd, capture_output=True)
decoded_text = raw_bytes.stdout.decode().strip()
print(f"Decoded Output: {decoded_text}")


# =====================================================================
# SECTION 7: ADVANCED & ASYNCHRONOUS PROCESSES (Popen)
# =====================================================================
# .Popen() runs in the background while Python continues executing

async_cmd = ["cmd", "/c", "timeout /t 3"] if os.name == "nt" else ["sleep", "3"]
process = subprocess.Popen(async_cmd)

print("Background process started...")

# Check status without pausing execution using .poll()
time.sleep(1)
if process.poll() is None:
    print("Process is STILL RUNNING in the background...")
else:
    print("Process HAS FINISHED!")

# Wait for completion & retrieve output using .communicate()
output_popen, _ = process.communicate()
print("Background process finished execution.")


# =====================================================================
# SECTION 8: ADVANCED SUBPROCESS MANAGEMENT
# =====================================================================
custom_env = os.environ.copy()
custom_env["BROWSER"] = "firefox"

try:
    sub_proc = subprocess.run(
        command,
        capture_output=True,
        text=True,
        env=custom_env,
        check=True
    )
    print("Subprocess executed successfully with custom env!")
except subprocess.CalledProcessError as err:
    print(f"Process crashed with error code {err.returncode}")


# =====================================================================
# SECTION 9: PROCESSING LOG FILES WITH REGULAR EXPRESSIONS
# =====================================================================
CURRENT_DIR = Path(__file__).parent
LOG_FILE = CURRENT_DIR / "system_audit.log"

log_contents = """
2026-08-29 10:00:01 [INFO] User admin logged in successfully.
2026-08-29 10:02:15 [ERROR] Failed to connect to DB server at 192.168.1.50.
2026-08-29 10:05:30 [WARNING] Disk space above 85% threshold.
2026-08-29 10:10:42 [ERROR] Payment gateway timeout for Order_9921.
"""

with open(LOG_FILE, "w", encoding="utf-8") as f:
    f.write(log_contents.strip())

print("\n=== FILTERING LOG FILE FOR ALL LOG LEVELS ===")

# Captures timestamp, log level (INFO/WARNING/ERROR), and message
log_pattern = re.compile(r"(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s\[(\w+)\]\s(.+)")
log_summary = []

with open(LOG_FILE, "r", encoding="utf-8") as file:
    for line in file:
        match = log_pattern.search(line)
        if match:
            log_summary.append({
                "time": match.group(1),
                "level": match.group(2),
                "message": match.group(3)
            })

for idx, log in enumerate(log_summary, 1):
    print(f"Log #{idx} | [{log['level']}] | {log['time']} | {log['message']}")