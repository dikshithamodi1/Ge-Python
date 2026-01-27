import re

def log_file_analyzer(log_data):
    # Regex pattern for timestamp and IP
    pattern = r'(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s-\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    for line in log_data.split('\n'):
        try:
            match = re.search(pattern, line)
            if match:
                timestamp, ip = match.groups()
                print(f"Timestamp: {timestamp} | IP: {ip}")
        except Exception:
            # Skip corrupted or unexpected lines
            continue


# Input Example
log_data = """2025-01-01 10:30:00 - 192.168.0.10
Invalid data line
2025-01-02 11:00:00 - 10.0.0.5"""

log_file_analyzer(log_data)
