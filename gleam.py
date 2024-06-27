import os
import requests
import json
import time
from tqdm import tqdm
from colorama import Fore, Style, init

init(autoreset=True)

def fetch_and_display_account_info():
    while True:
        with open('querygleam.txt', 'r') as file:
            accounts = file.readlines()
        for account_data in accounts:
            auth_url = "https://prod-api.gleam.bot/api/v1/accounts/auth"
            auth_data = json.dumps({
                "fromRefCode": "d04f891e",
                "initData": account_data.strip()
            })
            auth_headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }            
            auth_token = None
            for attempt in range(2):
                auth_response = requests.post(auth_url, headers=auth_headers, data=auth_data)
                if auth_response.status_code == 200:
                    auth_token = auth_response.json().get('token')
                    print(Fore.GREEN + "[ x ] Authentication successful !")
                    break
                else:
                    print(Fore.RED + "[ x ] Authentication failed !")
                    if attempt == 0:
                        print(Fore.YELLOW + "- Retrying...")
                        time.sleep(5)  # Delay sebelum retry
                    else:
                        continue
            if not auth_token:
                continue
            url = "https://prod-api.gleam.bot/api/v1/accounts/me"
            headers = {
                "Authorization": f"Bearer {auth_token}",
                "Accept": "application/json"
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                print(f"[ + ] Username: {data['account']['username']} | {data['account']['firstName']}")
                print(f"- Energy Amount: {data['account']['energyAmount']}")
                for balance in data['balances']:
                    print(f"- Balance: {balance['amount']} {balance['currency']}")
            else:
                print(Fore.RED + "- Failed to fetch account information !")
                continue
            claim_url = "https://prod-api.gleam.bot/api/v1/accounts/energy/refill/claim"
            claim_headers = {
                "Authorization": f"Bearer {auth_token}",
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            claim_data = json.dumps({})
            for attempt in range(2):
                claim_response = requests.post(claim_url, headers=claim_headers, data=claim_data)
                if claim_response.status_code == 200:
                    print(Fore.YELLOW + "- Claim successful !")
                    break
                else:
                    print(Fore.RED + "- Claim failed !")
                    if attempt == 0:
                        print(Fore.YELLOW + "- Retrying claim...")
                        time.sleep(5)
                    else:
                        continue
            start_farming_url = "https://prod-api.gleam.bot/api/v1/accounts/energy/refill/start"
            start_farming_headers = {
                "Authorization": f"Bearer {auth_token}",
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            start_farming_data = json.dumps({})
            for attempt in range(2):
                start_farming_response = requests.post(start_farming_url, headers=start_farming_headers, data=start_farming_data)
                if start_farming_response.status_code == 200:
                    print(Fore.CYAN + "- Start farming successful !")
                    print("")
                    break
                else:
                    print(Fore.RED + "- Start farming failed !")
                    if attempt == 0:
                        print(Fore.YELLOW + "- Retrying start farming...")
                        time.sleep(5)
                    else:
                        continue
            time.sleep(5)
        print(Fore.MAGENTA + "Completed all accounts.")
        countdown(2 * 3600 + 5 * 60)

def countdown(t):
    for i in tqdm(range(t, 0, -1), desc=f"{Fore.GREEN}Waiting for next cycle{Style.RESET_ALL}"):
        time.sleep(0.5)

if __name__ == "__main__":
    fetch_and_display_account_info()
