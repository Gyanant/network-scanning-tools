import subprocess
import platform
import re

# Function to retrieve ARP table from the system
def get_arp_table():

    os_type = platform.system().lower()   # Detect OS

    # Different ARP commands for Windows and Linux
    if os_type == "windows":
        command = ["arp", "-a"]
    else:
        command = ["arp", "-n"]

    try:
        # Run the ARP command and capture output
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        return result.stdout   # Return ARP table output

    except Exception as e:
        print("Error retrieving ARP table:", e)
        return None


# Function to extract IP and MAC addresses using regex
def parse_arp(output):

    # Regex pattern to match IP address and MAC address
    pattern = r"(\d+\.\d+\.\d+\.\d+)[^\n]*?([0-9a-fA-F:-]{17})"

    matches = re.findall(pattern, output)  # Find all matches

    return matches


# Function to display ARP entries
def display_results(entries):

    print("\nIP Address\t\tMAC Address")
    print("---------------------------------------------")

    # Print each IP-MAC pair
    for ip, mac in entries:
        print(f"{ip}\t\t{mac}")

    print(f"\nTotal entries: {len(entries)}")   


# Function to optionally save results to a file
def save_results(entries):

    choice = input("\nSave results to file? (y/n): ")

    if choice.lower() == "y":

        # Write results to a text file
        with open("arp_results.txt", "w") as f:

            for ip, mac in entries:
                f.write(f"{ip} {mac}\n")

        print("Results saved to arp_results.txt")


# Main program
if __name__ == "__main__":

    print("=== ARP Scanner ===")

    output = get_arp_table()   

    if output:
        entries = parse_arp(output)   # Extract IP-MAC pairs
        display_results(entries)      # Display results
        save_results(entries)         # Optionally save results