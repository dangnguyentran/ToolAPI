import requests
import time
from colorama import init, Fore, Style
import sys
import os
import argparse

init(autoreset=True)

def print_welcome_message():
    print(r"""
          
█▀▀ █░█ ▄▀█ █░░ █ █▄▄ █ █▀▀
█▄█ █▀█ █▀█ █▄▄ █ █▄█ █ ██▄
          """)
    print(Fore.GREEN + Style.BRIGHT + "Dotcoin BOT")
    print(Fore.GREEN + Style.BRIGHT + "Update Link: https://github.com/adearman/dotcoin")
    print(Fore.GREEN + Style.BRIGHT + "Free Konsultasi Join Telegram Channel: https://t.me/ghalibie\n")
    print(Fore.GREEN + Style.BRIGHT + "Buy me a coffee :) 0823 2367 3487 GOPAY / DANA")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_credentials():
    try:
        with open('tokensdotcoin.txt', 'r') as file:
            credentials_list = file.readlines()
        credentials = [cred.strip().split('|') for cred in credentials_list]
        return credentials
    except FileNotFoundError:
        print("File 'tokens.txt' tidak ditemukan. Pastikan file tersebut ada di direktori yang sama dengan script.")
        return []

def add_attempts(lvl, apikey, authorization, current_level):
    url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/add_attempts'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'x-client-info': 'postgrest-js/1.9.2'
    }
    while True:  
        print(f"\r{Fore.CYAN+Style.BRIGHT}[ Upgrade ] : Mencoba upgrade ke level {lvl}", end="" , flush=True)
        sys.stdout.flush()
        try:
            data = {'lvl': lvl}
            response = requests.post(url, headers=headers, json=data)
            response_data = response.json()
            if lvl > current_level:
                return False
            if response_data.get('success', False):
                return True
            else:
                lvl += 1
        except Exception as e:
            sys.stdout.write(f"Error while adding attempts: {e}\n")

def auto_clear_task(apikey, authorization):
    task_ids = [1, 2, 57, 40, 41, 39, 36, 42]
    base_url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/complete_task'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
        'x-client-info': 'postgrest-js/1.9.2',
        'x-telegram-user-id': '7003565657'
    }
    for task_id in task_ids:
        data = {'oid': str(task_id)}
        response = requests.post(base_url, headers=headers, json=data)
        if response.status_code == 200:
            print(f"{Fore.GREEN+Style.BRIGHT}[ Task {task_id} ] : Sukses")
        else:
            print(f"{Fore.RED+Style.BRIGHT}[ Task {task_id} ] {task_id}. Status code: {response.status_code} : Gagal")

def save_coins(coins, apikey, authorization):
    url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/save_coins'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'x-client-info': 'postgrest-js/1.9.2'
    }
    data = {'coins': coins}
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error saat menyimpan coins: {e}")
        return False

def get_user_info(apikey, authorization):
    url = 'https://jjvnmoyncmcewnuykyid.supabase.co/rest/v1/rpc/get_user_info'
    headers = {
        'accept': '*/*',
        'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
        'apikey': apikey,
        'authorization': f'Bearer {authorization}',
        'content-profile': 'public',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://dot.dapplab.xyz',
        'priority': 'u=1, i',
        'referer': 'https://dot.dapplab.xyz/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 125.0.0.0 Safari/537.36',
        'x-client-info': 'postgrest-js/1.9.2'
    }
    data = {}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def main():
    parser = argparse.ArgumentParser(description="Dotcoin BOT")
    parser.add_argument('--auto-upgrade', type=str, choices=['y', 'n'], default='n', help='Auto upgrade daily attempt? (y/n)')
    parser.add_argument('--clear-task', type=str, choices=['y', 'n'], default='n', help='Auto Clear Task? (default n) (y/n)')
    parser.add_argument('--upgrade-count', type=int, default=0, help='Mau upgrade berapa kali?')
    args = parser.parse_args()

    print_welcome_message()
    clear_task = args.clear_task
    credentials = load_credentials()
    jumlah_upgrade = args.upgrade_count if args.auto_upgrade == 'y' else 0
    upgrade_success = {}

    while True:
        for index, (apikey, authorization) in enumerate(credentials):
            info = get_user_info(apikey, authorization)
            print(f"{Fore.CYAN+Style.BRIGHT}============== [ Akun | {info['first_name']} ] ==============")
            if upgrade_success.get(apikey, False):
                if jumlah_upgrade > 0 and not upgrade_success.get(apikey, False):
                    for _ in range(jumlah_upgrade):
                        current_level = info['daily_attempts']
                        success = add_attempts(0, apikey, authorization, current_level)
                        if success:
                            upgrade_success[apikey] = True
                            print(f"{Fore.GREEN+Style.BRIGHT}[ Upgrade ] : Sukses                   ", flush=True)
                            break
                        else:
                            print(f"{Fore.RED+Style.BRIGHT}[ Upgrade ] : Gagal                  ", flush=True)
            if info:
                if clear_task == 'y':
                    auto_clear_task(apikey, authorization)
                print(f"{Fore.YELLOW+Style.BRIGHT}[ Level ] : {info['level']}")
                print(f"{Fore.YELLOW+Style.BRIGHT}[ Saldo ] : {info['balance']}")
                print(f"{Fore.BLUE+Style.BRIGHT}[ Energi ] : {info['daily_attempts']}")
                print(f"{Fore.BLUE+Style.BRIGHT}[ Limit Energi ] : {info['limit_attempts']}")
                print(f"{Fore.BLUE+Style.BRIGHT}[ Multiple Click Level ] : {info['multiple_clicks']}")
                energy = info['daily_attempts']
                if energy > 0:
                    for _ in range(energy):
                        print(f"{Fore.BLUE+Style.BRIGHT}\r[ Tap ] : Tapping..", end="", flush=True)
                        time.sleep(3)
                        save_coins(20000, apikey, authorization)
                        print(f"{Fore.GREEN+Style.BRIGHT}\r[ Tap ] : Sukses         ", flush=True)
                else:
                    print(f"{Fore.RED+Style.BRIGHT}Energi Anda habis. Menunggu pengisian ulang energi...")
            else:
                print("\r{Fore.RED+Style.BRIGHT}Token akses tidak valid, lanjut ke akun berikutnya.")
        print(f"{Fore.CYAN+Style.BRIGHT}==============Semua akun telah diproses=================")
        for i in range(300, 0, -1):
            sys.stdout.write(f"\rMemproses ulang semua akun dalam {i} detik...")
            sys.stdout.flush()
            time.sleep(1)
        print()
        clear_console()

if __name__ == "__main__":
    main()
