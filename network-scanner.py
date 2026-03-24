import os   
while True:

    # Display menu options
    print("""
=== Unified Network Scanner ===

1. Ping Scanner
2. ARP Scanner
3. Nmap Scanner
4. Exit
""")

    choice = input("Enter choice: ")

    # Run respective scanner scripts based on user input
    if choice == "1":
        os.system("python ping_scanner.py")   

    elif choice == "2":
        os.system("python arp_scanner.py")    

    elif choice == "3":
        os.system("python nmap_scanner.py")   

    elif choice == "4":
        break   

    else:
        print("Invalid choice")   