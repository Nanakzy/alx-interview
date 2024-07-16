#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys
import signal


# Initialize metrics
total_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}


def print_stats():
    """Prints the current statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handles the interrupt signal to print stats before exiting"""
    print_stats()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = parts[-1]

            try:
                total_size += int(file_size)
            except ValueError:
                pass

            if status_code in status_codes:
                status_codes[status_code] += 1

        line_count += 1
        if line_count == 10:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

# Print final stats after reading all input
print_stats()
