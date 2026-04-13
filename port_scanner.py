import socket
import sys
from datetime import datetime
import concurrent.futures

# The function the each thread will execute
def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"[+] Port {port} is  OPEN")

        s.close()

    except:
        # We use blank except ('pass') here so if one thread throws a random
        # network error, it doesn't crash the whole multi-threaded scan
        pass

def main():
    target = input("Enter Target IP or Hostname: ")
    start_port = int(input("Enter Start Port: "))
    end_port = int(input("Enter End Port: "))

    print("-" * 50)
    print(f"Scanning target: {target}")
    time_start = datetime.now()
    print(f"Time started: {time_start.strftime('%H:%M:%S')}")
    print("-" * 50)

    try:
        # Threading
        # max_workers is how many threads run at the exact same time
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            for port in range(start_port, end_port+1):
                # We submit the function (scan_port) and its arguments to the manager
                executor.submit(scan_port, target, port)

    # If user use Ctrl + c
    except KeyboardInterrupt:
        print("\nScan canceled by user.")
        sys.exit()

    # If host name not correct
    except socket.gaierror:
        print("\nHostname could not be resolved.")
        sys.exit()

    # If general network error
    except socket.error:
        print("\nConnection could not be established.")
        sys.exit()

    print("-" * 50)
    time_stop = datetime.now()
    print(f"Time started: {time_stop.strftime('%H:%M:%S')}")

    # Calculate the total time taken
    total_time = time_stop - time_start
    print(f"Total time: {total_time.seconds}s")

    print("Scan completed.")

    if __name__ == "__main__":
        main()

main()


