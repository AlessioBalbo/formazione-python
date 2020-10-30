import argparse
import re

regex_status = r"\" (\d{3}) \d{3}" ## search regex '" nnn nnn'
regex_ip = r"(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}) - "
regex_date = r"(\d{2}/.../\d{4})"
regex_time = r":(\d{2}:\d{2})"
regex_request = r"] (.*)\s\d{3}\s\d{3}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="log error parser")
    parser.add_argument(
        "-s",
        "--status-code",
        type=str,
        help="status code input"
    )
    args = parser.parse_args()
    status_code = args.status_code
    print(f"status code: {args.status_code}")
    with open("bertos_access.log") as log:
        print("date, time, ip, request")
        n_matches = 0;
        for line in log.readlines():
            match = re.search(regex_status, line)
            if match:
                if match.group(1) == status_code:
                    ##print(f"match found in line:\n{line}")
                    n_matches+=1;
                    print(f"status code:{match.group(1)}")
                    print(f"date: {re.search(regex_date, line).group(1)}")
                    print(f"time: {re.search(regex_time, line).group(1)}")
                    print(f"ip: {re.search(regex_ip, line).group(1)}")
                    print(f"request: {re.search(regex_request, line).group(1)}\n")

    if n_matches == 0:
        print(f"no matches for {status_code} code found")
    else: print(n_matches)
    
