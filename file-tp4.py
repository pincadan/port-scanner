import socket
import threading

# Function to scan ports
def scan_port(ip, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(1)
        # Attempt to connect to the port
        result = sock.connect_ex((ip, port))
        # If the connection was successful, print the port number
        if result == 0:
            print(f"Port {port} is open")
        # Close the socket
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Function to start the port scanner
def start_scanner(ip, start_port, end_port):
    # Iterate over the range of ports
    for port in range(start_port, end_port + 1):
        # Create a new thread for each port scan
        thread = threading.Thread(target=scan_port, args=(ip, port))
        # Start the thread
        thread.start()

# Main function
def main():
    # Get the target IP address from the user
    ip = input("Enter the target IP address: ")
    # Get the start and end ports from the user
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    # Start the port scanner
    start_scanner(ip, start_port, end_port)

# Run the main function
if __name__ == "__main__":
    main()