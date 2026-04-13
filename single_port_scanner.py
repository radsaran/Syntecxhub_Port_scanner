import socket
def scan_single_port(target_ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # here we create the socket object
    #AF_INET : IPv4, SOCK_STREAM : TCP

    s.settimeout(1.0)
    # If we don't do this, a filtered port will make the script hang for a long time waiting for a response.

    try:
        result = s.connect_ex((target_ip, port))
        # Attempt to connect
        # connect_x() returns an integer. 0 means success (port open)
        # any number means failure (port close / filtered)

        if result == 0:
            print(f"Port {port} on {target_ip} is OPEN")
        else:
            print(f"Port {port} on {target_ip} is CLOSED or FILTERED")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        s.close()

#-----------Target the script-----------------
target = input("Enter Target IP: ")
test_port = int(input("Enter Target Port: "))

print(f"Scanning for {target}...")
scan_single_port(target, test_port)
