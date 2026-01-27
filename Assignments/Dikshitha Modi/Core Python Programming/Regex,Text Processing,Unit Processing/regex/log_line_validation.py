import re
def log_line_validation(formats):
    pattern=r'^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] (ERROR|INFO|WARN): .+$'
    if re.match(pattern,formats):
        print("valid log entry")
    else:
        print("invalid log entry")
log_line_validation("[2025-11-05 14:33:21] ERROR: Disk full ")
