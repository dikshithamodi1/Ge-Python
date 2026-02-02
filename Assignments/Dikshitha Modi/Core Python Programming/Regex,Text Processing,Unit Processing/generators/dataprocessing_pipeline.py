import re
def read_lines(filename):
    """Yields lines from a file one by one."""
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()
def parse_logs(lines):
    """
    Takes a line iterator, extracts timestamp, log level, and message,
    yields a dictionary for each line.
    Example log format: "2026-01-28 10:00:00 [ERROR] Something failed"
    """
    pattern = r'^(?P<timestamp>\S+ \S+) \[(?P<level>\w+)\] (?P<message>.+)$'
    for line in lines:
        match = re.match(pattern, line)
        if match:
            yield match.groupdict()
def filter_errors(logs):
    """Yields only log entries where level is ERROR."""
    for log in logs:
        if log['level'] == 'ERROR':
            yield log

if __name__ == "__main__":
    filename = "system.log"  # Replace with your log file

    # Chain the generators
    lines = read_lines(filename)
    parsed_logs = parse_logs(lines)
    error_logs = filter_errors(parsed_logs)

    # Process and print only ERROR logs
    for error in error_logs:
        print(error)
