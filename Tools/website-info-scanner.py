import socket
import concurrent.futures
import requests
from urllib.parse import urlparse
import ssl
import urllib3
from requests.exceptions import RequestException
import time
import re
import dns.resolver
from bs4 import BeautifulSoup
import whois
import os

# Define color class for formatting
class Fuckcolors:
    red = '\033[91m'
    white = '\033[97m'
    reset = '\033[0m'

# Clear the console based on OS
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
def Title(title):
    clear()
    title_text = f"{Fuckcolors.red}{'=' * 20} {title} {'=' * 20}{Fuckcolors.reset}"
    
    # Get terminal width and center the title
    width, _ = os.get_terminal_size()
    centered_title = center_text(title_text, width, vertical_offset=2)

    # Display the centered title
    print(centered_title)

# Function to show a loading message
def Slow(message):
    print(f"{Fuckcolors.red}{message}{Fuckcolors.reset}")
    time.sleep(2)

# Function to get current time in hours (customized if needed)
def current_time_hour():
    return time.strftime("%H:%M:%S")

# Function to display an error message
def Error(message):
    print(f"{Fuckcolors.red}[ERROR] {message}{Fuckcolors.reset}")

# Function to find and format the website URL
def website_found_url(url):
    if not urlparse(url).scheme:
        website_url = "https://" + url
    else:
        website_url = url
    print(f"{current_time_hour()} {Fuckcolors.white}Website:{Fuckcolors.reset} {website_url}")
    return website_url

# Function to get and print the domain of the website
def website_domain(website_url):
    parsed_url = urlparse(website_url)
    domain = parsed_url.netloc
    print(f"{current_time_hour()} {Fuckcolors.white}Domain:{Fuckcolors.reset} {domain}")
    return domain

# Function to get and print the IP address of the domain
def website_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        ip = "None"
    
    if ip != "None":
        print(f"{current_time_hour()} {Fuckcolors.white}IP:{Fuckcolors.reset} {ip}")
    return ip

# Function to determine the type of IP (IPv4 or IPv6)
def ip_type(ip):
    if ':' in ip:
        type = "ipv6" 
    elif '.' in ip:
        type = "ipv4"
    else:
        type = "Unknown"
        return
    
    print(f"{current_time_hour()} {Fuckcolors.white}IP Type:{Fuckcolors.reset} {type}")

# Function to check if the website is secure (HTTPS)
def website_secure(website_url):
    secure = website_url.startswith("https://")
    print(f"{current_time_hour()} {Fuckcolors.white}Secure:{Fuckcolors.reset} {secure}")

# Function to check the status code of the website
def website_status(website_url):
    try:
        response = requests.get(website_url, timeout=5)
        status_code = response.status_code
    except RequestException:
        status_code = 404
    print(f"{current_time_hour()} {Fuckcolors.white}Status Code:{Fuckcolors.reset} {status_code}")

# Function to fetch and print IP-related information using ipinfo.io API
def ip_info(ip):
    api_url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(api_url)
        api = response.json()
    except RequestException:
        api = {}

    host_country = api.get('country', 'None')
    if host_country != "None":
        print(f"{current_time_hour()} {Fuckcolors.white}Host Country:{Fuckcolors.reset} {host_country}")

    host_name = api.get('hostname', 'None')
    if host_name != "None":
        print(f"{current_time_hour()} {Fuckcolors.white}Host Name:{Fuckcolors.reset} {host_name}")

    host_isp = api.get('isp', 'None')
    if host_isp != "None":
        print(f"{current_time_hour()} {Fuckcolors.white}Host ISP:{Fuckcolors.reset} {host_isp}")

    host_org = api.get('org', 'None')
    if host_org != "None":
        print(f"{current_time_hour()} {Fuckcolors.white}Host Org:{Fuckcolors.reset} {host_org}")

    host_as = api.get('asn', 'None')
    if host_as != "None":
        print(f"{current_time_hour()} {Fuckcolors.white}Host AS:{Fuckcolors.reset} {host_as}")

# Function to perform DNS resolution of the IP
def ip_dns(ip):
    try:
        dns, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
    except:
        dns = "None"
    
    if dns != "None":
        print(f"{current_time_hour()} {Fuckcolors.white}Host DNS:{Fuckcolors.reset} {dns}")

# Function to scan ports and print open ones
def website_port(ip):
    port_protocol_map = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
        80: "HTTP", 110: "POP3", 123: "NTP", 143: "IMAP", 194: "IRC", 389: "LDAP",
        443: "HTTPS", 161: "SNMP", 3306: "MySQL", 5432: "PostgreSQL", 6379: "Redis",
        1521: "Oracle DB", 3389: "RDP"
    }

    port_list = [21, 22, 23, 25, 53, 69, 80, 110, 123, 143, 194, 389, 443, 161, 3306, 5432, 6379, 1521, 3389]

    def scan_port(ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                protocol = port_protocol_map.get(port, "Unknown")
                print(f"{current_time_hour()} {Fuckcolors.white}Port:{Fuckcolors.reset} {port} {Fuckcolors.white}Status:{Fuckcolors.reset} Open {Fuckcolors.white}Protocol:{Fuckcolors.reset} {protocol}")
            sock.close()
        except:
            pass

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = {executor.submit(scan_port, ip, port): port for port in port_list}
    concurrent.futures.wait(results)

# Main script
def main():
    Title("Website Info Scanner")

    url = input(f"{current_time_hour()} {Fuckcolors.white}Enter website URL -> {Fuckcolors.reset}")
    if not url:
        Error("Website URL is required!")
        return

    print(f"{current_time_hour()} {Fuckcolors.white}Scanning...{Fuckcolors.reset}")

    website_url = website_found_url(url)
    domain = website_domain(website_url)
    ip = website_ip(domain)
    ip_type(ip)
    website_secure(website_url)
    website_status(website_url)
    ip_info(ip)
    ip_dns(ip)
    website_port(ip)

if __name__ == "__main__":
    main()
