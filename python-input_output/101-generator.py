#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

def generate_log_line():
    ip_address = ".".join(str(random.randint(1, 255)) for _ in range(4))
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    file_size = random.randint(1, 1024)
    return f"{ip_address} - [{date_time}] \"GET /projects/260 HTTP/1.1\" {status_code} {file_size}\n"

def main():
    try:
        for i in range(10000):
            sleep(random.random())
            log_line = generate_log_line()
            sys.stdout.write(log_line)
            sys.stdout.flush()
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
