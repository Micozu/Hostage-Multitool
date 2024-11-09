import os
import socket
import concurrent.futures
import time

# Define color class for formatting
class Fuckcolors:
    red = '\033[91m'
    reset = '\033[0m'

# Clear the console based on the operating system
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to center text horizontally and add vertical offset
def center_text(text, width, vertical_offset=2):
    lines = text.split("\n")
    horizontal_padding = (width - max(len(line) for line in lines)) // 2

    # Create padded lines
    padded_lines = [' ' * horizontal_padding + line for line in lines]
    return "\n" * vertical_offset + "\n".join(padded_lines)

# Function to display a title
def title(title):
    clear()
    title_text = f"{Fuckcolors.red}{'=' * 20} {title} {'=' * 20}{Fuckcolors.reset}"
    
    # Get terminal width and center the title
    width, _ = os.get_terminal_size()
    centered_title = center_text(title_text, width, vertical_offset=2)

    # Display the centered title
    print(centered_title)

# Function to show a loading message
def slow(message):
    print(f"{Fuckcolors.red}{message}{Fuckcolors.reset}")
    time.sleep(2)

# Function to get current time in hours (customized if needed)
def current_time_hour():
    return time.strftime("%H:%M:%S")

# Function to display an error message
def error(message):
    print(f"{Fuckcolors.red}[ERROR] {message}{Fuckcolors.reset}")

# Function to perform the IP Port scanning
def port_scanner(ip):
    port_protocol_map = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
        80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
        443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
        1521: "Oracle DB", 3389: "RDP"
    }

    # Function to scan individual ports
    def scan_port(ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((ip, port))
            if result == 0:  # If port is open
                protocol = identify_protocol(ip, port)
                print(f"{Fuckcolors.red}{current_time_hour()} {Fuckcolors.reset} Port: {port} {Fuckcolors.red}Status: Open{Fuckcolors.reset} Protocol: {protocol}")
            sock.close()
        except:
            pass

    # Function to identify the protocol for a port
    def identify_protocol(ip, port):
        if port in port_protocol_map:
            return port_protocol_map[port]
        else:
            return "Unknown"

    # Using ThreadPoolExecutor for concurrent scanning
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = {executor.submit(scan_port, ip, port): port for port in range(1, 65535 + 1)}
    concurrent.futures.wait(results)

# Main function to start the port scanning process
def main():
    title("IP Port Scanner")

    ip = input(f"\n{current_time_hour()} Enter IP address -> ")

    if not ip:
        error("IP address is required!")
        return
    
    slow("Scanning in progress...")
    port_scanner(ip)
    input(f"\n{Fuckcolors.red}Press Enter to return to the main menu...{Fuckcolors.reset}")

if __name__ == "__main__":
    main()
