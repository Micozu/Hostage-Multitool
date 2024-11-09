import random
import string
import json
import requests
import threading
import time
import os

# Define necessary constants for formatting (red and black design)
BEFORE = "\033[1;31m"  # Red
AFTER = "\033[0m"  # Reset
INFO = "\033[1;37m"  # White
GEN_VALID = "\033[1;32m"  # Green
GEN_INVALID = "\033[1;31m"  # Red
INPUT = "\033[1;33m"  # Yellow
WHITE = "\033[1;37m"  # White

# Function to get the current time
def current_time_hour():
    return time.strftime("%H:%M:%S", time.gmtime())

# Function to display error messages
def Error(message):
    print(f"{BEFORE}ERROR: {message}{AFTER}")

# Function to display the title of the tool
def Title(title):
    print(f"{BEFORE}========== {title} =========={AFTER}")

# Function to display slow output (for banners or loading)
def Slow(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print()

# Function to check if a webhook URL is valid
def CheckWebhook(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{GEN_VALID}Webhook URL is valid{AFTER}")
        else:
            print(f"{GEN_INVALID}Webhook URL is not valid{AFTER}")
            exit()
    except Exception as e:
        Error(f"Invalid webhook URL: {e}")
        exit()

# Function to send a test message to the webhook
def test_webhook(url):
    payload = {
        'embeds': [{
            'title': f'Revenge Tool',
            'description': f"**Message:**\n```Working!```",
            'color': 0x00FF00,  # Green
            'footer': {
                "text": "Nitro Generator",
                "icon_url": "https://example.com/icon.png",  # Placeholder icon URL
            }
        }],
        'username': "Webhook Tester",
        'avatar_url': "https://example.com/avatar.png",  # Placeholder avatar URL
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        requests.post(url, data=json.dumps(payload), headers=headers)
        print(f"{GEN_VALID}Test message sent successfully to webhook: {WHITE}{url}{AFTER}")
    except Exception as e:
        Error(f"Failed to send test message to webhook: {e}")

# Function to request Discord Nitro codes and send them to the webhook
def send_webhook(url_nitro):
    payload = {
        'embeds': [{
            'title': f'Nitro Valid!',
            'description': f"**Nitro:**\n```{url_nitro}```",
            'color': 0x00FF00,  # Green
            'footer': {
                "text": "Nitro Generator",
                "icon_url": "https://example.com/icon.png",  # Placeholder icon URL
            }
        }],
        'username': "Nitro Generator",
        'avatar_url': "https://example.com/avatar.png",  # Placeholder avatar URL
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        print(f"{GEN_VALID}Sent Nitro URL to webhook: {WHITE}{url_nitro}{AFTER}")
    except Exception as e:
        Error(f"Failed to send webhook: {e}")

# Function to check Nitro code validity
def nitro_check():
    code_nitro = ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(16)])
    url_nitro = f'https://discord.gift/{code_nitro}'
    response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true', timeout=1)

    if response.status_code == 200:
        if webhook in ['y']:
            send_webhook(url_nitro)
        print(f"{GEN_VALID}Status: {WHITE}Valid{GEN_VALID}  Nitro: {WHITE}{url_nitro}{AFTER}")
    else:
        print(f"{BEFORE}{current_time_hour()}{AFTER} {GEN_INVALID}Status: {WHITE}Invalid{GEN_INVALID} Nitro: {WHITE}{url_nitro}{AFTER}")

# Function to start multiple threads to check Nitro codes
def request():
    threads = []
    try:
        for _ in range(int(threads_number)):
            t = threading.Thread(target=nitro_check)
            t.start()
            threads.append(t)
    except:
        Error("Failed to start threads.")

    for thread in threads:
        thread.join()

# Main execution
if __name__ == "__main__":
    try:
        Title("Discord Nitro Generator")

        # Ask for webhook URL and test it
        webhook = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook? (y/n) -> {AFTER}")
        if webhook in ['y', 'Y', 'Yes', 'yes', 'YES']:
            webhook_url = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook URL -> {AFTER}")
            CheckWebhook(webhook_url)

            # Test the webhook by sending a test message
            test = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Send test message to Webhook? (y/n) -> {AFTER}")
            if test in ['y', 'Y', 'Yes', 'yes', 'YES']:
                test_webhook(webhook_url)

        # Ask for number of threads
        try:
            threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Threads Number -> {AFTER}"))
        except:
            Error("Invalid number of threads. Please enter a valid number.")
            exit()

        # Start requesting Nitro codes in a loop
        while True:
            request()

    except Exception as e:
        Error(f"Unexpected Error: {e}")
