import requests
import json
import time
from colorama import Fore, Style, init

def print_welcome_message():
    print(r"""
          
█▀▀ █░█ ▄▀█ █░░ █ █▄▄ █ █▀▀
█▄█ █▀█ █▀█ █▄▄ █ █▄█ █ ██▄
          """)
    print(Fore.GREEN + Style.BRIGHT + "LotteFi BOT")
    print(Fore.CYAN + Style.BRIGHT + "Update Link: https://github.com/adearman/lottefi")
    print(Fore.YELLOW + Style.BRIGHT + "Free Konsultasi Join Telegram Channel: https://t.me/ghalibie")
    print(Fore.BLUE + Style.BRIGHT + "Buy me a coffee :) 0823 2367 3487 GOPAY / DANA")
    print(Fore.RED + Style.BRIGHT + "NOT FOR SALE ! Ngotak dikit bang. Ngoding susah2 kau tinggal rename :)\n\n")

init(autoreset=True)

def collect_and_claim(user_data, index):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://tele-web.lottefi.app',
        'pragma': 'no-cache',
        'referer': 'https://tele-web.lottefi.app/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    headers['--webapp-init'] = user_data

    try:
        print(f"{Fore.CYAN+Style.BRIGHT}\n=== [ Akun {index} ] ===")
        # Collect
        print(Fore.YELLOW + Style.BRIGHT + "[ Collect ] : Trying to collect. ", end="", flush=True)
        collect_response = requests.post('https://rest.lottefi.app/api/farm/collect', headers=headers, json={"collect_onchain": False})
        if collect_response.status_code == 200:
            collect_data = collect_response.json()
            print(Fore.GREEN + Style.BRIGHT + f"\r[ Collect ] : Successfully collected {collect_data['farm_balance']} ", flush=True)
            # Claim
            print(Fore.YELLOW + Style.BRIGHT + "[ Claim ] : Trying to claim. ", end="", flush=True)
            claim_response = requests.post('https://rest.lottefi.app/api/farm/claim', headers=headers)
            if claim_response.status_code == 200:
                claim_data = claim_response.json()
                print(Fore.GREEN + Style.BRIGHT + f"\r[ Claim ] : Successfully claimed {claim_data['claim_amount']} ", flush=True)
            elif claim_response.status_code == 404:
                print(Fore.RED + Style.BRIGHT + f"\r[ Claim ] : Failed to claim. {claim_response.json()['message']}", flush=True)
        elif collect_response.status_code == 404:
            print(Fore.RED + Style.BRIGHT + f"\r[ Collect ] : Failed to collect. {collect_response.json()['message']}", flush=True)
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"\r[ Collect ] : Failed to collect. {e}", flush=True)

# Baca data user dari file
with open('tgwebapplottefi.txt', 'r') as file:
    users = file.readlines()
  

def auto_complete_start_quest(user_data):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://tele-web.lottefi.app',
        'pragma': 'no-cache',
        'referer': 'https://tele-web.lottefi.app/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    headers['--webapp-init'] = user_data
    actions = [
        {"quest_id": "starter_quest", "action": "join_telegram_channel"},
        {"quest_id": "starter_quest", "action": "follow_twitter"},
        {"quest_id": "starter_quest", "action": "like_twitter"},
        {"quest_id": "starter_quest", "action": "reply_twitter"}
    ]
    for action in actions:
        response = requests.post('https://rest.lottefi.app/api/quest/set', headers=headers, json=action)
        if response.status_code != 200:
            if response.json().get('message') == "Internal server error":
                print(f"{Fore.RED+Style.BRIGHT}\r[ Start Quest ] : Already Completed", flush=True)
            else:
                print(f"{Fore.RED+Style.BRIGHT}\r[ Start Quest ] : Failed to complete action {action['action']}: {response.text}", flush=True)
            return
    # Menandai quest sebagai selesai
    response = requests.post('https://rest.lottefi.app/api/quest/done', headers=headers, json={"quest_id": "starter_quest"})
    if response.status_code == 200:
        print(f"{Fore.GREEN+Style.BRIGHT}\r[ Start Quest ] : Successfully completed quest", flush=True)
    else:
        print(f"{Fore.RED+Style.BRIGHT}\r[ Start Quest ] : Failed to complete quest: {response.text}", flush=True)


def auto_clear_task(user_data):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://tele-web.lottefi.app',
        'pragma': 'no-cache',
        'referer': 'https://tele-web.lottefi.app/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    headers['--webapp-init'] = user_data
    actions = [
        {"quest_id": "testnet_air1", "action": "like_twitter"},
        {"quest_id": "testnet_air1", "action": "join_telegram_channel"},
        {"quest_id": "testnet_air1", "action": "reply_twitter"}
    ]
    for action in actions:
        response = requests.post('https://rest.lottefi.app/api/quest/set', headers=headers, json=action)
        if response.status_code != 200:
            if response.json().get('message') == "Internal server error":
                print(f"{Fore.RED+Style.BRIGHT}\r[ Task ] : Already Completed", flush=True)
            else:
                print(f"{Fore.RED+Style.BRIGHT}\r[ Task ] : Failed to complete action {action['action']}: {response.text}", flush=True)
            return
    # Menandai quest sebagai selesai
    response = requests.post('https://rest.lottefi.app/api/quest/done', headers=headers, json={"quest_id": "testnet_air1"})
    if response.status_code == 200:
        print(f"{Fore.GREEN+Style.BRIGHT}\r[ Task ] : Successfully completed quest",  flush=True)
    else:
        print(f"{Fore.RED+Style.BRIGHT}\r[ Task ] : Failed to complete quest: {response.text}",  flush=True)


import argparse
def parse_arguments():
    parser = argparse.ArgumentParser(description='Blum BOT')
    parser.add_argument('--start', type=str, choices=['y', 'n'], help='Auto Finish Start Quest (y/n)')
    parser.add_argument('--task', type=str, choices=['y', 'n'], help='Auto Clear Task (y/n)')
    args = parser.parse_args()

    if args.start is None:
        # Jika parameter --task tidak diberikan, minta input dari pengguna
        start_input = input("Apakah ingin auto finish start quest? (y/n, default n): ").strip().lower()
        # Jika pengguna hanya menekan enter, gunakan 'n' sebagai default
        args.start = start_input if start_input in ['y', 'n'] else 'n'

    if args.task is None:
        # Jika parameter --claim_ref tidak diberikan, minta input dari pengguna
        task_input = input("Apakah ingin auto clear task? (y/n, default n): ").strip().lower()
        # Jika pengguna hanya menekan enter, gunakan 'n' sebagai default
        args.task = task_input if task_input in ['y', 'n'] else 'n'

    return args
args = parse_arguments()
start_enable = args.start
task_enable = args.task
while True:
    print_welcome_message()
    try:
        for index, user_data in enumerate(users, start=1):
            user_data_clean = user_data.strip()
            collect_and_claim(user_data_clean, index)
            time.sleep(2)
            # cleaned_user_data = clean_user_data(user_data)
            # Contoh pemanggilan fungsi
            if start_enable == 'y':
                print(f"{Fore.GREEN+Style.BRIGHT}\r[ Start Quest ] : Checking..",end="", flush=True)
                auto_complete_start_quest(user_data_clean)
            if task_enable == 'y':
                print(f"{Fore.GREEN+Style.BRIGHT}\r[ Task ] : Checking..",end="", flush=True)
                auto_clear_task(user_data_clean)
        print(f"\n{Fore.GREEN+Style.BRIGHT}========={Fore.WHITE+Style.BRIGHT}Semua akun berhasil di proses{Fore.GREEN+Style.BRIGHT}=========", end="", flush=True)
        import sys
        waktu_tunggu = 100  #  dalam detik
        for detik in range(waktu_tunggu, 0, -1):
            sys.stdout.write(f"\r{Fore.CYAN}Menunggu waktu claim berikutnya dalam {Fore.CYAN}{Fore.WHITE}{detik // 60} menit {Fore.WHITE}{detik % 60} detik")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\rWaktu claim berikutnya telah tiba!                                                          \n")

 
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        time.sleep(10)
        continue

