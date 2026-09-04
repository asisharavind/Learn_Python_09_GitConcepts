
# practice: re.search() with all groups, re.match(), re.sub(), re.split(), re.IGNORECASE, re.DOTALL
# \d = digit (0-9)            \D = non-digit
# \w = word char (a-z,0-9,_)  \W = non-word char (punctuation/spaces)
# \s = whitespace (space/tab) \S = non-whitespace
# +  = 1 or more              *  = 0 or more           ? = optional (0 or 1)

# Pattern with 4 distinct capturing groups:
# Group 1: (\d{4}-\d{2}-\d{2})  -> Date (YYYY-MM-DD)
# Group 2: \[(PASS|FAIL)\]      -> Test Result Status
# Group 3: (GET|POST|PUT|DELETE)-> HTTP Method
# Group 4: (\d+ms)              -> Execution Latency
"""
PYTHON REGULAR EXPRESSIONS (re) FOR TEST AUTOMATION
====================================================
1. Basic Matching & Searching (search, match, findall)
2. Essential Metacharacters & Special Sequences
3. Extracting Dynamic Data Using Groups ()
4. Cleaning & Formatting Logs (sub, split)
5. Performance Optimization (re.compile & Flags)
"""

import re

# =====================================================================
# SECTION 1: BASIC MATCHING FUNCTIONS
# =====================================================================
text = "Error Code 404: Page Not Found on server QA-01"

# 1. re.search() -> Finds FIRST occurrence anywhere in the string
match_obj = re.search(r"404", text)
if match_obj:
    print(f"Found match: {match_obj.group()}")  # Output: 404

log_entry = "2026-09-01 [PASS] POST /api/v1/users ExecutionTime: 124ms"
# Pattern with 4 distinct capturing groups:
# Group 1: (\d{4}-\d{2}-\d{2})  -> Date (YYYY-MM-DD)
# Group 2: \[(PASS|FAIL)\]      -> Test Result Status
# Group 3: (GET|POST|PUT|DELETE)-> HTTP Method
# Group 4: (\d+ms)              -> Execution Latency
pattern = r"(\d{4}-\d{2}-\d{2})\s\[(PASS|FAIL)\]\s(GET|POST|PUT|DELETE)\s\S+\sExecutionTime:\s(\d+ms)"

match = re.search(pattern, log_entry)

if match:
    print(f"Group 0 (Full Match) : {match.group(0)}")
    print(f"Group 1 (Date)       : {match.group(1)}")
    print(f"Group 2 (Status)     : {match.group(2)}")
    print(f"Group 3 (HTTP Method): {match.group(3)}")
    print(f"Group 4 (Latency)    : {match.group(4)}")

# 2. re.match() -> Checks if string STARTS with the pattern (Strict!)
start_match = re.match(r"Error", text)
print(f"Starts with 'Error'?: {bool(start_match)}")  # Output: True

# 3. re.findall() -> Extracts ALL matching occurrences into a list
numbers = re.findall(r"\d+", text)  # \d+ matches 1 or more digits
print(f"All numbers found: {numbers}")  # Output: ['404', '01']


# =====================================================================
# SECTION 2: ESSENTIAL PATTERNS & METACHARACTERS
# =====================================================================
# \d = digit (0-9)            \D = non-digit
# \w = word char (a-z,0-9,_)  \W = non-word char (punctuation/spaces)
# \s = whitespace (space/tab) \S = non-whitespace
# +  = 1 or more              *  = 0 or more           ? = optional (0 or 1)

log_entry = "User admin_01 logged in at 10:45:30 AM"

# Pattern: Match username format (word chars ending with digits)
username = re.search(r"\w+_\d+", log_entry)
print(f"Username extracted: {username.group()}")  # Output: admin_01

# Pattern: Match Timestamp (HH:MM:SS format)
timestamp = re.search(r"\d{2}:\d{2}:\d{2}", log_entry)
print(f"Timestamp extracted: {timestamp.group()}")  # Output: 10:45:30


# =====================================================================
# SECTION 3: EXTRACTING DATA USING GROUPS ()
# =====================================================================
# Parentheses () capture specific sub-parts of a pattern for easy extraction
api_response = "Response: status=200 OK, latency=145ms, env=STAGING"

pattern = r"status=(\d+)\s\w+,\slatency=(\d+ms)"
match = re.search(pattern, api_response)

if match:
    print(f"Full Match: {match.group(0)}")   # status=200 OK, latency=145ms
    print(f"Status Code: {match.group(1)}")  # 200
    print(f"Latency:     {match.group(2)}")  # 145ms


# =====================================================================
# SECTION 4: CLEANING LOGS & TEXT MANIPULATION
# =====================================================================
# 1. re.sub() -> Replace patterns (e.g., mask sensitive data or clean spaces)
text = "Payment failed for User 102 using card 4111-2222-3333-4444 on checkout page."
pattern = r"\d{4}-\d{4}-\d{4}-\d{4}"
reg_text = re.sub(pattern, "XXXX-XXXX-XXXX-XXXX", text)
print(f"Cleaned Log: {reg_text}")

text = "Status: SUCCESS | Execution ID: EXEC-994821 | Retry ID: EXEC-4"
pattern = r"EXEC-\d+"
reg_text = re.sub(pattern, "EXEC-VARIABLE", text)
print(f"Cleaned Log: {reg_text}")

import re

text = "User created on 12/25/2026 and verified on 01/05/2027"
# Group 1 = Month (\1), Group 2 = Day (\2), Group 3 = Year (\3)
pattern = r"(\d{2})/(\d{2})/(\d{4})"
# Rearrange to Year-Month-Day: \3-\1-\2
reg_text = re.sub(pattern, r"\3-\1-\2", text)
print(f"Cleaned Log: {reg_text}")

# 2. re.split() -> Split strings by flexible delimiters (comma, semicolon, spaces)
csv_line = "TC001 ;  Login_Suite , PASS  | Chrome"
fields = re.split(r"\s*[,;|]\s*", csv_line)
print(f"Split Fields: {fields}")  # ['TC001', 'Login_Suite', 'PASS', 'Chrome']


# =====================================================================
# SECTION 5: PATTERN REUSE & FLAGS (re.compile)
# =====================================================================
# Use re.compile() for patterns used repeatedly inside loops or test suites
# Common Flags:
# re.IGNORECASE (re.I) -> Case-insensitive matching
# re.DOTALL     (re.S) -> Allows '.' to match newline characters (\n)

import re

# Compiling pattern with re.IGNORECASE (re.I)
# Matches "status:" followed by "pass" or "fail" in ANY case
input1 = "Content-Type: application/json"
input2 = "content-type: APPLICATION/JSON"

# re.IGNORECASE makes "content-type" match "Content-Type" 
# and "application/json" match "APPLICATION/JSON"
pattern = re.compile(r"content-type:\s*([\w/]+)", re.IGNORECASE)

# Test input 1
match1 = pattern.search(input1)
if match1:
    print(f"Captured 1: {match1.group(1)}")  # Output: application/json

# Test input 2
match2 = pattern.search(input2)
if match2:
    print(f"Captured 2: {match2.group(1)}")  # Output: APPLICATION/JSON

    import re

ui_errors = [
    "Error: Access Denied for user admin",
    "SUCCESS: Page loaded",
    "403 UNAUTHORIZED request",
    "Warning: Low disk space"
]

# Match "access denied" OR "unauthorized" in ANY case combination
pattern = re.compile(r"access denied|unauthorized|WARNING", re.IGNORECASE)

# Filter the list using a list comprehension
filtered_errors = [error for error in ui_errors if pattern.search(error)]

print(filtered_errors)

# Without DOTALL -> Returns None because '.' gets blocked by the '\n' after 'start'
import re

text = "start\nline 1\nline 2\nend"

# Without DOTALL -> Returns None because '.' gets blocked by the '\n' after 'start'
print(re.search(r"start(.*?)end", text))  # Output: None

# With DOTALL -> Successfully captures '\nline 1\nline 2\n'
match = re.search(r"start(.*?)end", text, flags=re.DOTALL)
print(match.group(1).strip())  # Output: line 1\nline 2
