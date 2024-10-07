# port-scanner

This script uses Python's socket library to attempt connections to ports on the target machine. It uses threading to scan multiple ports simultaneously, which can speed up the scanning process. 

The scan_port function attempts to connect to a single port and prints a message if the port is open. 

The start_scanner function iterates over a range of ports and creates a new thread for each port scan. 

The main function gets the target IP address and port range from the user and starts the port scanner.

Please note that port scanning can be considered intrusive and may be illegal if done without permission. Always make sure you have permission to scan a target machine.

