import subprocess
import sys
def check_nmap():

    try:
        # Run nmap version command
        result = subprocess.run(
            ["nmap", "-V"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            print("Nmap is installed\n")
            return True

    except FileNotFoundError:
        print("Nmap is not installed")
        return False

def run_scan(target, choice):

    # Select scan type based on user choice
    if choice == "1":
        command = ["nmap", "-sn", target]     # Host discovery (ping scan)

    elif choice == "2":
        command = ["nmap", target]            # Default port scan

    elif choice == "3":
        ports = input("Enter port range (example 20-80): ")
        command = ["nmap", "-p", ports, target]   # Custom port range scan

    elif choice == "4":
        command = ["nmap", "-sV", target]     # Service/version detection

    elif choice == "5":
        command = ["nmap", "-O", target]      # OS detection

    else:
        print("Invalid option")
        return

    try:

        print("\nScanning...")

        # Execute Nmap command
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=120     
        )

        print("\nScan Results:\n")
        print(result.stdout)

        # Option to save results
        save = input("Save results to file? (y/n): ")

        if save.lower() == "y":

            with open("nmap_results.txt", "w") as f:
                f.write(result.stdout)

            print("Results saved to nmap_results.txt")

    except subprocess.TimeoutExpired:
        print("Scan timed out")

if __name__ == "__main__":

    print("=== Nmap Scanner ===\n")

    # Ensure Nmap is available before scanning
    if not check_nmap():
        sys.exit()

    target = input("Enter target IP or network: ")

    print("""
1. Basic Host Discovery (-sn)
2. Port Scan (1-1000)
3. Custom Port Range Scan
4. Service Version Detection (-sV)
5. OS Detection (-O)
""")

    choice = input("Enter choice: ")

    run_scan(target, choice)