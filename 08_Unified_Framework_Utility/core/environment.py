import sys
import os
from pathlib import Path


class BaseConfig:
    """Parent class demonstrating OOP constructor inheritance."""
    def __init__(self, project_name: str):
        self.project_name = project_name
        self._created_at = Path(__file__).stat().st_mtime


class EnvironmentManager(BaseConfig):
    """Manages CLI arguments, streams, and target URL environments."""

    def __init__(self, project_name: str):
        super().__init__(project_name)
        self._target_url = "https://practicetestautomation.com"

    # Property Getter
    @property
    def target_url(self) -> str:
        return self._target_url

    # Property Setter with Encapsulation
    @target_url.setter
    def target_url(self, value: str):
        allowed_urls = [
            "https://practicetestautomation.com",
            "https://www.saucedemo.com"
        ]
        if value in allowed_urls:
            self._target_url = value
            os.environ["TARGET_URL"] = value
        else:
            raise ValueError(f"Invalid URL: {value}. Must be one of {allowed_urls}")

    @staticmethod
    def prompt_tester_name() -> str:
        """Section 1: Data Streams & Interactive Input."""
        user_name = input("Enter tester name: ")
        sys.stdout.write(f"Standard Output: Execution initiated by {user_name}\n")
        sys.stderr.write("Standard Error: [NOTICE] Target URL health check active.\n")
        return user_name

    def parse_cli_args(self):
        """Section 2: CLI Arguments."""
        script_name = sys.argv[0]
        sys.stdout.write(f"Running script: {script_name}\n")
        args = sys.argv[1:]
        if args:
            print(f"Command-line arguments received: {args}")
        else:
            print("No CLI arguments passed. Using default settings.")
        return args

    def setup_environment_variables(self):
        """Section 3: Environment Variables."""
        os.environ["QA_SUITE_READY"] = "TRUE"
        print(f"Current Target URL Set: {self.target_url}")