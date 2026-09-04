import sys
from pathlib import Path

from core import EnvironmentManager, SystemProcessManager, LogAuditProcessor


def main():
    print("=" * 60)
    print("      WEB QE SUITE & SUBPROCESS MONITOR ENGINE          ")
    print("=" * 60)

    # 1. Environment & Inputs (Sections 1, 2, 3)
    env_mgr = EnvironmentManager(project_name="Web UI Health Prober")
    tester = env_mgr.prompt_tester_name()
    cli_args = env_mgr.parse_cli_args()

    # Change active URL using OOP Property Setter
    target_site = "https://www.saucedemo.com"
    env_mgr.target_url = target_site
    env_mgr.setup_environment_variables()

    # 2. Directory & Subprocess Probing (Sections 4, 5, 6, 7, 8)
    base_output_dir = Path.cwd() / "output_reports"
    base_output_dir.mkdir(exist_ok=True)

    proc_mgr = SystemProcessManager()
    proc_mgr.compare_filesystem_tools(base_output_dir)
    proc_mgr.probe_url_basic(target_site)
    proc_mgr.run_legacy_wrappers(target_site)
    proc_mgr.run_async_url_check(target_site)
    proc_mgr.run_advanced_management(target_site)

    # 3. Regex & Log File Parsing (Section 9)
    logger = LogAuditProcessor(log_dir=base_output_dir)
    logger.generate_sample_logs()
    parsed_records = logger.parse_logs()

    print("\n=== PARSED URL LOG SUMMARY ===")
    for idx, record in enumerate(parsed_records, 1):
        print(f"Log #{idx} | [{record['level']}] | {record['time']} | {record['message']}")

    print("\nWeb QE Execution Completed Successfully!")
    sys.exit(0)


if __name__ == "__main__":
    main()