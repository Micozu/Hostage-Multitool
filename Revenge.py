import os
import subprocess
import json

# Define color class for formatting
class Fuckcolors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    bold = '\033[1m'
    reset = '\033[0m'

# Function to clear the console based on the operating system
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to center text horizontally and add vertical offset
def center_text(text, width, vertical_offset=2):
    lines = text.split("\n")
    horizontal_padding = (width - max(len(line) for line in lines)) // 2

    # Create padded lines
    padded_lines = [' ' * horizontal_padding + line for line in lines]
    return "\n" * vertical_offset + "\n".join(padded_lines)

# Function to display the logo
def logo():
    clear()
    logo_text = f"""{Fuckcolors.red}
    ┬ ┬┌─┐┌┼┐┌┬┐┌─┐┌─┐┌─┐
    ├─┤│ │└┼┐ │ ├─┤│ ┬├┤ 
    ┴ ┴└─┘└┼┘ ┴ ┴ ┴└─┘└─┘
    {Fuckcolors.reset}"""
    
    # Get terminal width and set offset for centering the logo
    width, _ = os.get_terminal_size()
    centered_logo = center_text(logo_text, width, vertical_offset=4)

    # Display the logo
    print(centered_logo)

# Function to load user data from JSON file
def load_user_data():
    user_file_path = os.path.expanduser(r'~/Desktop/Revenge/user_info.json')
    
    # Check if the file exists
    if os.path.exists(user_file_path):
        with open(user_file_path, 'r') as file:
            user_data = json.load(file)
        return user_data.get("username")
    return None

# Function to save user data to JSON file
def save_user_data(username):
    user_file_path = os.path.expanduser(r'~/Desktop/Revenge/user_info.json')
    user_data = {"username": username}
    
    with open(user_file_path, 'w') as file:
        json.dump(user_data, file)

# Function to get the username from the user or load from the file
def get_username():
    username = load_user_data()  # Try to load username from JSON
    if username:
        # If a username exists in the file, log in automatically
        print(f"\n{Fuckcolors.red}Logged in as PREMIUM user: {username}{Fuckcolors.reset}")
        # Change terminal prompt to show the username
        os.environ['PROMPT'] = f"{username} → "
    else:
        # If no username found, prompt the user to enter their username with a stylish prompt
        username = input(f"\n{Fuckcolors.red}{Fuckcolors.bold}Enter Your Username: {Fuckcolors.reset}")
        save_user_data(username)  # Save the username to JSON
        print(f"\n{Fuckcolors.red}Logged in as PREMIUM user: {username}{Fuckcolors.reset}")
        os.environ['PROMPT'] = f"{username} → "
    return username

# Function to display the tools menu
def display_tools_menu():
    menu_text = f"""{Fuckcolors.red}
    ╔════════════════════════════════════════════════╗
    ║  1. IP Lookup      = Looks up an IP            ║
    ║  2. IP Port Scanner = Scan a specific IP/Port  ║
    ║  3. Username Scanner = Scan for a username     ║
    ║  4. Token Login     = Login with Discord token ║
    ║  5. Nitro Generator = Generate Discord Nitro   ║
    ║  6. Phone Number Lookup = Lookup phone number  ║
    ║  7. Website Info Scanner = Scan website info   ║
    ║  8. Roblox User Info = Lookup Roblox username  ║
    ║  9. Exit           = Exit the tool             ║
    ╚════════════════════════════════════════════════╝
    """

    # Get terminal size for centering
    width, _ = os.get_terminal_size()

    # Center the menu
    centered_menu = center_text(menu_text, width, vertical_offset=2)

    # Display the centered menu
    print(centered_menu)

# Function to run the Roblox User Info tool
def roblox_user_info():
    clear()
    print(f"{Fuckcolors.red}Roblox User Info tool selected{Fuckcolors.reset}")
    
    # Build the path dynamically for any user
    roblox_user_info_path = os.path.expanduser(r'~/Desktop/Revenge/Tools/roblox-user-info.py')

    # Run the external script located at the dynamic path
    subprocess.run(['python', roblox_user_info_path])
    
    # Wait for the user to press Enter to return to the main menu
    input(f"\n{Fuckcolors.red}Press Enter to return to the Hostage menu...{Fuckcolors.reset}")

# Function to run the IP lookup tool
def ip_lookup():
    clear()
    print(f"{Fuckcolors.red}IP Lookup tool selected{Fuckcolors.reset}")
    
    # Build the path dynamically for any user
    ip_lookup_path = os.path.expanduser(r'~/Desktop/Revenge/Tools/ip-lookup.py')

    # Run the external script located at the dynamic path
    subprocess.run(['python', ip_lookup_path])
    
    # Wait for the user to press Enter to return to the main menu
    input(f"\n{Fuckcolors.red}Press Enter to return to the Hostage menu...{Fuckcolors.reset}")

# Function to run the IP Port Scanner tool
def ip_port_scanner():
    clear()
    print(f"{Fuckcolors.red}IP Port Scanner tool selected{Fuckcolors.reset}")
    
    # Build the path dynamically for any user
    ip_port_scanner_path = os.path.expanduser(r'~/Desktop/Revenge/Tools/IP-port-scanner.py')

    # Run the external script located at the dynamic path
    subprocess.run(['python', ip_port_scanner_path])
    
    # Wait for the user to press Enter to return to the main menu
    input(f"\n{Fuckcolors.red}Press Enter to return to the Hostage menu...{Fuckcolors.reset}")

# Function to run the Username Scanner tool
def username_scanner():
    clear()
    print(f"{Fuckcolors.red}Username Scanner tool selected{Fuckcolors.reset}")
    
    # Build the path dynamically for any user
    username_finder_path = os.path.expanduser(r'~/Desktop/Revenge/Tools/username-finder.py')

    # Run the external script located at the dynamic path
    subprocess.run(['python', username_finder_path])
    
    # Wait for the user to press Enter to return to the main menu
    input(f"\n{Fuckcolors.red}Press Enter to return to the Hostage menu...{Fuckcolors.reset}")

# Function to run the Token Login tool
def token_login():
    clear()
    print(f"{Fuckcolors.red}Token Login tool selected{Fuckcolors.reset}")
    
    # Build the path dynamically for any user
    token_login_path = os.path.expanduser(r'~/Desktop/Revenge/Tools/token-login.py')

    # Run the external script located at the dynamic path
    subprocess.run(['python', token_login_path])
    
    # Wait for the user to press Enter to return to the main menu
    input(f"\n{Fuckcolors.red}Press Enter to return to the Hostage menu...{Fuckcolors.reset}")

# Function to run the Nitro Generator tool
def nitro_generator():
    clear()
    print(f"{Fuckcolors.red}Discord Nitro Generator tool selected{Fuckcolors.reset}")
    
    # Build the path dynamically for any user
    nitro_generator_path = os.path.expanduser(r'~/Desktop/Revenge/Tools/discord-nitro-generator.py')

    # Run the external script located at the dynamic path
    subprocess.run(['python', nitro_generator_path])
    
    # Wait for the user to press Enter to return to the main menu
    input(f"\n{Fuckcolors.red}Press Enter to return to the Hostage menu...{Fuckcolors.reset}")

# Function to run the Phone Number Lookup tool
def phone_number_lookup():
    clear()
    print(f"{Fuckcolors.red}Phone Number Lookup tool selected{Fuckcolors.reset}")
    
    # Build the path dynamically for any user
    phone_number_lookup_path = os.path.expanduser(r'~/Desktop/Revenge/Tools/phone-number-lookup.py')

    # Run the external script located at the dynamic path
    subprocess.run(['python', phone_number_lookup_path])
    
    # Wait for the user to press Enter to return to the main menu
    input(f"\n{Fuckcolors.red}Press Enter to return to the Hostage menu...{Fuckcolors.reset}")

# Function to run the Website Info Scanner tool
def website_info_scanner():
    clear()
    print(f"{Fuckcolors.red}Website Info Scanner tool selected{Fuckcolors.reset}")
    
    # Build the path dynamically for any user
    website_info_scanner_path = os.path.expanduser(r'~/Desktop/Revenge/Tools/website-info-scanner.py')

    # Run the external script located at the dynamic path
    subprocess.run(['python', website_info_scanner_path])
    
    # Wait for the user to press Enter to return to the main menu
    input(f"\n{Fuckcolors.red}Press Enter to return to the Hostage menu...{Fuckcolors.reset}")

# Main menu to handle input and tool execution
def main_menu():
    username = get_username()  # Get the username and log in
    while True:
        logo()  # Display the logo
        display_tools_menu()  # Display menu options

        try:
            # Handle user input and direct to the appropriate function
            choice = int(input(f"\n{Fuckcolors.red}C:/Hostage/{username} → {Fuckcolors.reset}"))
            if choice == 1:
                ip_lookup()  # Call the IP lookup tool
            elif choice == 2:
                ip_port_scanner()  # Call the IP Port Scanner tool
            elif choice == 3:
                username_scanner()  # Call the Username Scanner tool
            elif choice == 4:
                token_login()  # Call the Token Login tool
            elif choice == 5:
                nitro_generator()  # Call the Discord Nitro Generator tool
            elif choice == 6:
                phone_number_lookup()  # Call the Phone Number Lookup tool
            elif choice == 7:
                website_info_scanner()  # Call the Website Info Scanner tool
            elif choice == 8:
                roblox_user_info()  # Call the Roblox User Info tool
            elif choice == 9:
                print(f"{Fuckcolors.red}Exiting the tool...{Fuckcolors.reset}")
                break  # Exit the loop and program
            else:
                print(f"{Fuckcolors.red}Invalid selection. Please choose a valid number.{Fuckcolors.reset}")
        except ValueError:
            print(f"{Fuckcolors.red}Please enter a valid number!{Fuckcolors.reset}")

if __name__ == "__main__":
    main_menu()