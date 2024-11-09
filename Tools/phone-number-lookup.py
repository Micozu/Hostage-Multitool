import os
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import time

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

# Function to get current time in hours
def current_time_hour():
    return time.strftime("%H:%M:%S")

# Function to display an error message
def Error(message):
    print(f"{Fuckcolors.red}[ERROR] {message}{Fuckcolors.reset}")

# Function to lookup phone number information
def phone_number_lookup(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number, None)
        
        # Check if the phone number is valid
        if phonenumbers.is_valid_number(parsed_number):
            status = "Valid"
        else:
            status = "Invalid"
        
        # Extract details
        country_code = "+" + phone_number[1:3] if phone_number.startswith("+") else "None"
        operator = carrier.name_for_number(parsed_number, "fr") if carrier.name_for_number(parsed_number, "fr") else "None"
        type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
        timezones = timezone.time_zones_for_number(parsed_number)
        timezone_info = timezones[0] if timezones else "None"
        country = phonenumbers.region_code_for_number(parsed_number)
        region = geocoder.description_for_number(parsed_number, "fr")
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)

        # Display results
        result_text = f"""
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Phone        : {Fuckcolors.white}{phone_number}{Fuckcolors.reset}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Formatted    : {Fuckcolors.white}{formatted_number}{Fuckcolors.reset}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Status       : {Fuckcolors.white}{status}{Fuckcolors.reset}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Country Code : {Fuckcolors.white}{country_code}{Fuckcolors.reset}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Country      : {Fuckcolors.white}{country}{Fuckcolors.reset}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Region       : {Fuckcolors.white}{region}{Fuckcolors.reset}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Timezone     : {Fuckcolors.white}{timezone_info}{Fuckcolors.reset}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Operator     : {Fuckcolors.white}{operator}{Fuckcolors.reset}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Type Number  : {Fuckcolors.white}{type_number}{Fuckcolors.reset}
        """

        Slow(result_text)

    except Exception as e:
        Error("Unable to retrieve phone number information.")
        print(f"{Fuckcolors.red}[ERROR] {str(e)}{Fuckcolors.reset}")

def main():
    Title("Phone Number Lookup")
    
    phone_number = input(f"\n{current_time_hour()} Enter Phone Number -> ")

    if not phone_number:
        Error("Phone number is required!")
        return
    
    phone_number_lookup(phone_number)

if __name__ == "__main__":
    main()
