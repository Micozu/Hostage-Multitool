import os
import requests
import time
import webbrowser

# Define color class for formatting
class Fuckcolors:
    red = '\033[91m'
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

# Function to perform the IP lookup using the APIs
def ip_lookup(ip):
    try:
        # First API attempt (ipinfo.io)
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        api = response.json()

        status = "Valid" if response.status_code == 200 else "Invalid"
        country = api.get('country', 'None')
        country_code = api.get('country', 'None')  # 'country' used for both fields
        region = api.get('region', 'None')
        region_code = api.get('region', 'None')  # 'region' used for both fields
        zip_code = api.get('postal', 'None')
        city = api.get('city', 'None')
        latitude, longitude = api.get('loc', 'None').split(',') if 'loc' in api else ('None', 'None')
        timezone = api.get('timezone', 'None')
        isp = api.get('org', 'None')  # ISP information may be stored in 'org'
        org = api.get('org', 'None')
        as_host = api.get('asn', 'None')

    except Exception as e:
        # Fallback to second API if the first fails (ip-api.com)
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}")
            api = response.json()

            status = "Valid" if api.get('status') == "success" else "Invalid"
            country = api.get('country', 'None')
            country_code = api.get('countryCode', 'None')
            region = api.get('regionName', 'None')
            region_code = api.get('region', 'None')
            zip_code = api.get('zip', 'None')
            city = api.get('city', 'None')
            latitude = api.get('lat', 'None')
            longitude = api.get('lon', 'None')
            timezone = api.get('timezone', 'None')
            isp = api.get('isp', 'None')
            org = api.get('org', 'None')
            as_host = api.get('as', 'None')

        except Exception as e:
            Error("Unable to retrieve IP information.")
            return None

    # Print the gathered information
    result_text = f"""
    {Fuckcolors.red}[INFO]{Fuckcolors.reset} Status     : {status}
    {Fuckcolors.red}[INFO]{Fuckcolors.reset} Country    : {country} ({country_code})
    {Fuckcolors.red}[INFO]{Fuckcolors.reset} Region     : {region} ({region_code})
    {Fuckcolors.red}[INFO]{Fuckcolors.reset} Zip        : {zip_code}
    {Fuckcolors.red}[INFO]{Fuckcolors.reset} City       : {city}
    {Fuckcolors.red}[INFO]{Fuckcolors.reset} Latitude   : {latitude}
    {Fuckcolors.red}[INFO]{Fuckcolors.reset} Longitude  : {longitude}
    {Fuckcolors.red}[INFO]{Fuckcolors.reset} Timezone   : {timezone}
    {Fuckcolors.red}[INFO]{Fuckcolors.reset} ISP        : {isp}
    {Fuckcolors.red}[INFO]{Fuckcolors.reset} Org        : {org}
    {Fuckcolors.red}[INFO]{Fuckcolors.reset} AS         : {as_host}
    """
    Slow(result_text)

    # Ask user if they want to view the location on Google Maps
    if latitude != 'None' and longitude != 'None':
        open_maps = input(f"\n{current_time_hour()} Open location on Google Maps? (Press Enter to open) -> ")
        if open_maps == '':
            maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
            webbrowser.open(maps_url)
            Slow(f"Opening Google Maps for the location...")

    # Return to the main menu
    input(f"\n{current_time_hour()} Press Enter to return to the main menu...")

def main():
    Title("IP Lookup")
    
    ip = input(f"\n{current_time_hour()} Enter IP address -> ")

    if not ip:
        Error("IP address is required!")
        return
    
    ip_lookup(ip)

if __name__ == "__main__":
    main()
