from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
Reports_log = Path(BASE_DIR, "logs", "report_log.txt")
Project_Log = Path(BASE_DIR, "logs", "project_log.txt")
excel_filename = Path(BASE_DIR, 'data', 'operations.xlsx')
