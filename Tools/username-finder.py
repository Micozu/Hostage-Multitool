import requests
import re
import bs4
import time

# Define necessary constants for formatting (red and black design)
BEFORE = "\033[1;31m"  # Red
AFTER = "\033[0m"  # Reset
INFO = "\033[1;37m"  # White
GEN_VALID = "\033[1;32m"  # Green
ADD = "\033[1;34m"  # Blue
INPUT = "\033[1;33m"  # Yellow
WHITE = "\033[1;37m"  # White

# Username filters
filtered_usernames = ["micozu", "mico", "micoz", "micozuyt"]

def Error(message):
    print(f"{BEFORE}ERROR: {message}{AFTER}")

def Slow(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def current_time_hour():
    return time.strftime("%H:%M:%S", time.gmtime())

def Censored(username):
    # Check if the username is in the filtered list
    if username.lower() in filtered_usernames:
        Error("This username is restricted!")
        exit()

def Title(name):
    print(f"{BEFORE}{name}{AFTER}")

def Continue():
    input(f"{BEFORE}Press Enter to continue...{AFTER}")

def Reset():
    # Functionality to reset or clean up if necessary
    pass

# Websites to check for username availability
sites = {
    "YouTube": "https://www.youtube.com/{}",
    "Roblox Trade": "https://rblx.trade/p/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Instagram": "https://www.instagram.com/{}",
    "Paypal": "https://www.paypal.com/paypalme/{}",
    "GitHub": "https://github.com/{}",
    "Pinterest": "https://www.pinterest.com/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Telegram": "https://t.me/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Twitter": "https://twitter.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    # 20 New Websites added below:
    "Reddit": "https://www.reddit.com/user/{}",
    "Etsy": "https://www.etsy.com/shop/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Discord": "https://discord.com/users/{}",
    "Medium": "https://medium.com/@{}",
    "WordPress": "https://{}.wordpress.com",
    "Dribbble": "https://dribbble.com/{}",
    "Behance": "https://www.behance.net/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "Goodreads": "https://www.goodreads.com/user/show/{}",
    "Fiverr": "https://www.fiverr.com/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "Patreon": "https://www.patreon.com/{}",
    "ProductHunt": "https://www.producthunt.com/@{}",
    "Strava": "https://www.strava.com/athletes/{}",
    "Meetup": "https://www.meetup.com/members/{}",
    "HackerRank": "https://www.hackerrank.com/{}",
    "Trello": "https://trello.com/{}",
    "VK": "https://vk.com/{}",
}

def site_exception(username, site, page_content):
    if site == "Paypal":
        page_content = page_content.replace(f'slug_name={username}', '').replace(f'"slug":"{username}"', '')
    elif site == "TikTok":
        page_content = page_content.replace(f'\\u002f@{username}"', '')
    return page_content

# Main program to track the username across websites
Title("Username Tracker")

try:
    number_site = 0
    number_found = 0
    sites_and_urls_found = []

    # Input the username
    username = input(f"\n{BEFORE}Enter Username: {AFTER}")
    Censored(username)
    username = username.lower()

    # Now display the scanning message
    Slow("Scanning for username...")

    print(f"{BEFORE}Scanning..{AFTER}")

    for site, url_template in sites.items():
        try:
            number_site += 1
            url = url_template.format(username)
            try:
                response = requests.get(url, timeout=5)  # Increased timeout for reliability

                if response.status_code == 200:
                    page_content = re.sub(r'<[^>]*>', '', response.text.lower().replace(url, "").replace(f"/{username}", ""))
                    page_content = site_exception(username, site, page_content)
                    page_text = bs4.BeautifulSoup(response.text, 'html.parser').get_text().lower().replace(url, "")
                    page_title = bs4.BeautifulSoup(response.content, 'html.parser').title.string.lower()

                    if username in page_title or username in page_content or username in page_text:
                        number_found += 1
                        sites_and_urls_found.append(f"{site}: {WHITE}{url}{AFTER}")
                        print(f"{GEN_VALID}Found at {site}: {WHITE}{url}{AFTER}")

            except requests.exceptions.Timeout:
                pass  # Skip timeout messages
            except Exception as e:
                pass  # Skip exception messages

        except Exception as e:
            pass  # Skip exception messages

    # Display results summary
    print(f"\n{INFO}Total Sites Checked: {number_site}")
    print(f"{INFO}Total Found: {number_found}\n")

    if sites_and_urls_found:
        print(f"{INFO}Sites Found:")
        for site_and_url_found in sites_and_urls_found:
            time.sleep(0.5)
            print(f"{ADD}{site_and_url_found}")

    Continue()
    Reset()

except Exception as e:
    Error(e)

# Return to the main menu after finishing
import subprocess
subprocess.run(['python', r'C:\Users\Mico\Desktop\Revenge\Hostage.py'])
