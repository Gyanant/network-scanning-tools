import subprocess      
import platform        
import re              
import sys             

# Function to ping a single host
def ping_host(host):

    # Detect the operating system (Windows / Linux / Mac)
    os_type = platform.system().lower()

    # -n for Windows and -c for Linux
    if os_type == "windows":
        param = "-n"
    else:
        param = "-c"

    # Create the ping command
    command = ["ping", param, "4", host]

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,   
            stderr=subprocess.PIPE,   
            text=True,                
            timeout=10                
        )

        # If return code is 0, ping was successful
        if result.returncode == 0:
            output = result.stdout   # Store the ping output

            avg_time = None

            # Windows ping output 
            if os_type == "windows":
                match = re.search(r"Average = (\d+)ms", output)
            else:
                match = re.search(r"= .*/(.*?)/", output)

            # Extract average time
            if match:
                avg_time = match.group(1)

            # Print host status
            print(f"\nHost: {host}")
            print("Status: Reachable")
            print(f"Average Time: {avg_time} ms")

        else:
            # If return code not 0, host is unreachable
            print(f"\nHost: {host}")
            print("Status: Unreachable")

    # Handle timeout if ping takes too long
    except subprocess.TimeoutExpired:
        print("Ping request timed out")

# Function to ping multiple hosts
def ping_multiple(hosts):
    for host in hosts:
        ping_host(host)

if __name__ == "__main__":

    print("=== Ping Scanner ===")

    # Select for single host or multiple hosts
    choice = input("Ping single host? (y/n): ").lower()

    if choice == "y":
        host = input("Enter hostname or IP: ")
        ping_host(host)

    # If user selects multiple hosts
    else:
        hosts = input("Enter hosts separated by space: ").split()
        ping_multiple(hosts)