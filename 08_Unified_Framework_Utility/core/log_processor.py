import re
from pathlib import Path


class LogAuditProcessor:
    """Section 9: Processing Log Files with Regular Expressions."""

    def __init__(self, log_dir: Path):
        self.log_file = log_dir / "url_audit.log"

    def generate_sample_logs(self):
        """Writes mock web test execution log entries."""
        log_contents = """
2026-08-29 10:00:01 [INFO] Navigated to https://practicetestautomation.com
2026-08-29 10:02:15 [ERROR] 404 Page NotFound at https://www.saucedemo.com/cart
2026-08-29 10:05:30 [WARNING] Response time > 2000ms for https://practicetestautomation.com/practice-test-login/
2026-08-29 10:10:42 [ERROR] ElementNotFoundException: Login button missing.
        """.strip()
        self.log_file.write_text(log_contents, encoding="utf-8")

    def parse_logs(self) -> list:
        """Parses log file using regex capturing groups."""
        log_pattern = re.compile(
            r"(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s\[(\w+)\]\s(.+)"
        )
        log_summary = []

        with open(self.log_file, "r", encoding="utf-8") as file:
            for line in file:
                match = log_pattern.search(line)
                if match:
                    log_summary.append({
                        "time": match.group(1),
                        "level": match.group(2),
                        "message": match.group(3),
                    })
        return log_summary