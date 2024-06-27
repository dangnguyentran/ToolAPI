import websockets
import json
import time
import asyncio
from colorama import init, Fore, Style
init(autoreset=True)
import requests  # Tambahkan ini di bagian import
import time
import datetime
import argparse


async def process_subprotocol(subprotocol, uri, headers):
    try:
        async with websockets.connect(uri, extra_headers=headers, subprotocols=[subprotocol]) as ws:
            try:
                print(f"{Fore.GREEN+Style.BRIGHT}\rConnecting...", end="", flush=True)
                message = await ws.recv()
                data = json.loads(message)
                if data.get("action") == "user":
                    # Proses data pengguna
                    print(f"{Fore.GREEN+Style.BRIGHT}\rConnected           ", end="", flush=True)
                    time.sleep(2)
                    user_data = data.get("data", {})
                    username = user_data.get("username", "Username ga diset")
                    nama = f"{user_data.get('firstName', '')} {user_data.get('lastName', '')}".strip()
                    energy = user_data.get("energy", 0)
                    free_turbo = user_data.get("freeTurbo", 0)
                    free_energy_regeneration = user_data.get("freeEnergyRegeneration", 0)
                    balance = user_data.get("balance", 0)
                    print(f"{Fore.BLUE+Style.BRIGHT}\r=========[ {Fore.WHITE+Style.BRIGHT}{nama} - {username}{Fore.BLUE+Style.BRIGHT} ]=========", flush=True)  
                    formatted_balance = f"{balance:,}".replace(",", ".")
                    print(f"{Fore.CYAN+Style.BRIGHT}[ Balance ] : {formatted_balance}")
                    print(f"{Fore.YELLOW+Style.BRIGHT}[ Energy ] : {energy}")
                    print(f"{Fore.YELLOW+Style.BRIGHT}[ Free Turbo ] : {free_turbo}")
                    print(f"{Fore.YELLOW+Style.BRIGHT}[ Free Energy ] : {free_energy_regeneration}")

                    if cek_boost == 'y':
                    # Cek energi dan energi gratis
                        if energy < 50 and free_energy_regeneration > 0:
                            response = requests.put(
                                'https://api.prick.lol/v1/boost/energy-regeneration',
                                headers={
                                    'Authorization': f'Bearer {subprotocol}',  # asumsi subprotocol adalah token
                                    'Content-Length': '0',
                                    'User-Agent': headers['User-Agent'],
                                    'Origin': headers['Origin']
                                }
                            )
                            if response.status_code == 200:
                                print(f"{Fore.GREEN+Style.BRIGHT}\r[ Energy Boost ] : Active", flush=True)
                            else:
                                print(f"{Fore.RED+Style.BRIGHT}\r[ Energy Boost ] : Failed", flush=True)

                            # Aktifkan turbo jika energi berhasil diperbarui
                            if response.json().get("result", {}).get("energy", 0) > 0:
                                turbo_response = requests.put(
                                    'https://api.prick.lol/v1/boost/turbo',
                                    headers={
                                        'Authorization': f'Bearer {subprotocol}',
                                        'Content-Length': '0',
                                        'User-Agent': headers['User-Agent'],
                                        'Origin': headers['Origin']
                                    }
                                )
                                if turbo_response.status_code == 200:
                                    print(f"{Fore.GREEN+Style.BRIGHT}\r[ Turbo Boost ] : Active", flush=True)
                                else:
                                    print(f"{Fore.RED+Style.BRIGHT}\r[ Turbo Boost ] : Failed", flush=True)

                    # Mengirim pesan tap
                    waktu_sekarang = int(time.time() * 1000)
                    taps = [waktu_sekarang + i * 139 for i in range(200)]
                    tap_message = {
                        "action": "tap",
                        "data": taps
                    }
                    await ws.send(json.dumps(tap_message))
                    print(f"{Fore.CYAN+Style.BRIGHT}\r[ Tap ] : Taping...", end="", flush=True)
           
                    try:
                        response_message = await asyncio.wait_for(ws.recv(), timeout=20)  # Meningkatkan timeout menjadi 20 detik
                        response_data = json.loads(response_message)
                        if 'userClicks' in response_data and 'energy' in response_data and 'balance' in response_data:
                            formatted_balance = f"{response_data['balance']:,}".replace(",", ".")
                            print(f"{Fore.GREEN+Style.BRIGHT}\r[ Tap ] : Total Tap {response_data['userClicks']} | {response_data['energy']} Energy | {formatted_balance} Balance", flush=True)
                        else:
                            print(f"{Fore.RED+Style.BRIGHT}\r[ Tap ] : {response_data}", flush=True)
                    except asyncio.TimeoutError:
                        print(f"{Fore.RED+Style.BRIGHT}\r[ Tap ] : Timeout / Akun Belum Aktif", flush=True)
                    except json.JSONDecodeError:
                        print(f"{Fore.RED+Style.BRIGHT}\r[ Tap ] : Gagal respons JSON", flush=True)
                    except Exception as e:
                        print(f"{Fore.RED+Style.BRIGHT}\r[ Tap ] : {e}", flush=True)

            except Exception as e:
                print(f"{Fore.RED+Style.BRIGHT}[ Error ] : {e}")
            finally:
                await ws.close()
                print(f"{Fore.BLUE+Style.BRIGHT}========= [ {Fore.WHITE+Style.BRIGHT}Done{Fore.BLUE+Style.BRIGHT} ] =========\n")
    except Exception as e:
        print(f"{Fore.RED+Style.BRIGHT}[ Error ] : {e}")

def parse_arguments():
    parser = argparse.ArgumentParser(description='Prick BOT')
    parser.add_argument('--boost', type=str, choices=['y', 'n'], help='use Booster (y/n)')
    args = parser.parse_args()
    if args.boost is None:
        # Jika parameter --boost tidak diberikan, minta input dari pengguna
        boost_input = input("Aktifkan Booster? (y/n, default n): ").strip().lower()
        # Jika pengguna hanya menekan enter, gunakan 'n' sebagai default
        args.boost = boost_input if boost_input in ['y', 'n'] else 'n'

    return args

args = parse_arguments()
cek_boost = args.boost

def start_subprotocol_thread(subprotocol, uri, headers):
    asyncio.new_event_loop().run_until_complete(process_subprotocol(subprotocol, uri, headers))
start_time = datetime.datetime.now() 
def print_welcome_message():
    print(r"""
          
█▀▀ █░█ ▄▀█ █░░ █ █▄▄ █ █▀▀
█▄█ █▀█ █▀█ █▄▄ █ █▄█ █ ██▄
          """)
    print(Fore.GREEN + Style.BRIGHT + "Prick BOT")
    print(Fore.GREEN + Style.BRIGHT + "Update Link: https://github.com/adearman/prick")
    print(Fore.YELLOW + Style.BRIGHT + "Free Konsultasi Join Telegram Channel: https://t.me/ghalibie")
    print(Fore.BLUE + Style.BRIGHT + "Buy me a coffee :) 0823 2367 3487 GOPAY / DANA")
    print(Fore.RED + Style.BRIGHT + "NOT FOR SALE ! Ngotak dikit bang. Ngoding susah2 kau tinggal rename :)\n\n")
    current_time = datetime.datetime.now()
    up_time = current_time - start_time
    days, remainder = divmod(up_time.total_seconds(), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(Fore.CYAN + Style.BRIGHT + f"Up time bot: {int(days)} hari, {int(hours)} jam, {int(minutes)} menit, {int(seconds)} detik")

def animated_loading(duration):
    frames = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        for frame in frames:
            print(f"\rMenunggu waktu claim berikutnya {frame} - Tersisa {remaining_time} detik         ", end="", flush=True)
            time.sleep(0.25)
    print("\rMenunggu waktu claim berikutnya selesai.                            ", flush=True)     

    
def main():
    uri = "wss://api.prick.lol/ws"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Origin": "https://app.prick.lol",
    }
    
    while True:
        print_welcome_message()
    # Membaca subprotocols dari file
        with open('idteleprick.txt', 'r') as file:
            subprotocols = [line.strip() for line in file.readlines()]

        for subprotocol in subprotocols:
            asyncio.new_event_loop().run_until_complete(process_subprotocol(subprotocol, uri, headers))
        
        print(f"{Fore.BLUE+Style.BRIGHT}========= [ {Fore.WHITE+Style.BRIGHT}ALL DONE{Fore.BLUE+Style.BRIGHT} ] =========\n")
        animated_loading(300)
if __name__ == "__main__":
    main()