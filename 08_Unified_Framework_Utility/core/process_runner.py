import os
import sys
import time
import subprocess
from pathlib import Path


class SystemProcessManager:
    """Manages URL network checks and subprocess triggers."""

    @staticmethod
    def compare_filesystem_tools(base_dir: Path):
        """Section 4: Pathlib vs OS vs Subprocess directory creation."""
        # Task A: Get CWD using all 3 tools
        cwd_pathlib = Path.cwd()
        cwd_os = os.getcwd()
        cwd_sub = subprocess.check_output(
            ["cmd", "/c", "cd"] if os.name == "nt" else ["pwd"], text=True
        ).strip()

        # Task B: Create test output directories
        (base_dir / "dir_pathlib").mkdir(parents=True, exist_ok=True)
        
        os_dir = base_dir / "dir_os"
        if not os_dir.exists():
            os.mkdir(os_dir)

        sub_dir = base_dir / "dir_sub"
        cmd = ["cmd", "/c", "mkdir", str(sub_dir)] if os.name == "nt" else ["mkdir", "-p", str(sub_dir)]
        subprocess.run(cmd)

    def probe_url_basic(self, url: str):
        """Section 5: Core Subprocess Execution (subprocess.run)."""
        print(f"\n--- Section 5: Ping/Curl URL Probe for {url} ---")
        command = ["curl", "-I", url] if os.name != "nt" else ["cmd", "/c", f"curl -I {url}"]
        
        result = subprocess.run(command, capture_output=True, text=True)
        print(f"Subprocess Exit Code: {result.returncode}")
        print(f"Header Response (First 150 chars):\n{result.stdout[:150]}")

    def run_legacy_wrappers(self, url: str):
        """Section 6: Legacy Subprocess Wrappers (.call, .check_call, .check_output)."""
        echo_cmd = ["cmd", "/c", "echo", f"Checking {url}"] if os.name == "nt" else ["echo", f"Checking {url}"]

        # 1. call()
        code = subprocess.call(echo_cmd)
        print(f"call() Exit Code: {code}")

        # 2. check_call()
        try:
            subprocess.check_call(echo_cmd)
        except subprocess.CalledProcessError as err:
            sys.stderr.write(f"check_call failed: {err}\n")

        # 3. check_output()
        output = subprocess.check_output(echo_cmd, text=True)
        print(f"check_output(): {output.strip()}")

        # 4. Byte decoding
        raw_bytes = subprocess.run(echo_cmd, capture_output=True)
        print(f"Decoded Output: {raw_bytes.stdout.decode().strip()}")

    def run_async_url_check(self, url: str):
        """Section 7: Asynchronous Background Process (.Popen, .poll, .communicate)."""
        print("\n--- Section 7: Async Ping Background Check ---")
        async_cmd = ["cmd", "/c", "ping -n 3 google.com"] if os.name == "nt" else ["ping", "-c", "3", "google.com"]
        
        process = subprocess.Popen(async_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Background network check started with Popen...")

        time.sleep(1)
        if process.poll() is None:
            print("Ping is STILL RUNNING in the background...")

        stdout, _ = process.communicate()
        print("Background network check completed!")

    def run_advanced_management(self, url: str):
        """Section 8: Advanced Subprocess Management (env, check=True)."""
        custom_env = os.environ.copy()
        custom_env["ACTIVE_URL"] = url
        
        command = ["cmd", "/c", "echo Target: %ACTIVE_URL%"] if os.name == "nt" else ["sh", "-c", "echo Target: $ACTIVE_URL"]

        try:
            sub_proc = subprocess.run(
                command,
                capture_output=True,
                text=True,
                env=custom_env,
                check=True
            )
            print(f"Advanced Exec Output: {sub_proc.stdout.strip()}")
        except subprocess.CalledProcessError as err:
            print(f"Process crashed with code {err.returncode}")