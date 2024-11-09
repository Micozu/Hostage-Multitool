import os
import requests
import time

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

# Function to handle Roblox User Info retrieval
def roblox_user_info(username_input):
    try:
        response = requests.post("https://users.roblox.com/v1/usernames/users", json={
            "usernames": [username_input],
            "excludeBannedUsers": "true"
        })

        data = response.json()

        user_id = data['data'][0]['id']

        response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        api = response.json()

        userid = api.get('id', "None")
        display_name = api.get('displayName', "None")
        username = api.get('name', "None")
        description = api.get('description', "None")
        created_at = api.get('created', "None")
        is_banned = api.get('isBanned', "None")
        external_app_display_name = api.get('externalAppDisplayName', "None")
        has_verified_badge = api.get('hasVerifiedBadge', "None")

        # Print the gathered information
        result_text = f"""
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Username       : {username}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Id             : {userid}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Display Name   : {display_name}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Description    : {description}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Created        : {created_at}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Banned         : {is_banned}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} External Name  : {external_app_display_name}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Verified Badge : {has_verified_badge}
        """
        Slow(result_text)

    except Exception as e:
        Error("Unable to retrieve Roblox user information.")
        return None

def main():
    Title("Roblox User Info")
    
    # Input for Roblox username
    username_input = input(f"\n{current_time_hour()} Enter Username -> ")

    if not username_input:
        Error("Username is required!")
        return
    
    roblox_user_info(username_input)

if __name__ == "__main__":
    main()
