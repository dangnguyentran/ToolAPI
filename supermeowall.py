import requests
import time
import random
import threading

def claim_reward(param_claim, thread_id):
    headers = {
        'accept': 'application/json; indent=2',
        'accept-language': 'id-ID,id;q=0.9,en-ID;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://lfg.supermeow.vip',
        'priority': 'u=1, i',
        'referer': 'https://lfg.supermeow.vip/',
        'sec-ch-ua': '""',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '""',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; Redmi Note 8 Build/TQ3A.230901.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36',
    }
    url_claim = 'https://api.supermeow.vip/meow/claim?' + param_claim
    while True:
        response = requests.post(url_claim, headers=headers).json()
        balance = response.get('balance', 'N/A')
        print(f'Account: {thread_id} | Your Balance: {balance}')
        rand_delay = random.randint(3700, 4000)
        delay = rand_delay
        for i in range(delay, 0, -1):
            minutes, seconds = divmod(i, 60)
            hours, minutes = divmod(minutes, 60)
            print(f"Account: {thread_id} | Next Claim In : {hours:02d}:{minutes:02d}:{seconds:02d}", end='\r')
            time.sleep(1)
        print("\n")

if __name__ == "__main__":
    # Danh sách các tham số
    param_claims = [
        "telegram=5302906337&auth_data=%7B%22query_id%22:%22AAHh7RM8AgAAAOHtEzyPk7yh%22,%22user%22:%22%7B%5C%22id%5C%22:5302906337,%5C%22first_name%5C%22:%5C%22Tran%5C%22,%5C%22last_name%5C%22:%5C%22Nguy%C3%AAn+W-coin%5C%22,%5C%22username%5C%22:%5C%22dncrpto99%5C%22,%5C%22language_code%5C%22:%5C%22vi%5C%22,%5C%22allows_write_to_pm%5C%22:true%7D%22,%22auth_date%22:%221719132175%22,%22hash%22:%22790d8cf22aeaaf885770037f5f4eb9c02271ccfbcf929b7c3492a5b3da63d7e8%22%7D",
        "telegram=7417790564&auth_data=%7B%22query_id%22:%22AAFkgCI6AwAAAGSAIjp0V4-6%22,%22user%22:%22%7B%5C%22id%5C%22:7417790564,%5C%22first_name%5C%22:%5C%22Big%5C%22,%5C%22last_name%5C%22:%5C%22Nose%5C%22,%5C%22language_code%5C%22:%5C%22vi%5C%22,%5C%22allows_write_to_pm%5C%22:true%7D%22,%22auth_date%22:%221719132948%22,%22hash%22:%228c261f71dba326cd450843817edbef8200ed184a54268dd780deccfcb7087771%22%7D",
        "telegram=6908621475&auth_data=%7B%22query_id%22:%22AAGjMskbAwAAAKMyyRtvFQaZ%22,%22user%22:%22%7B%5C%22id%5C%22:6908621475,%5C%22first_name%5C%22:%5C%22BIG%5C%22,%5C%22last_name%5C%22:%5C%22Mouth+W-coin%5C%22,%5C%22username%5C%22:%5C%22Bigmouth97%5C%22,%5C%22language_code%5C%22:%5C%22vi%5C%22,%5C%22allows_write_to_pm%5C%22:true%7D%22,%22auth_date%22:%221719133157%22,%22hash%22:%22107a6175d41c2bba79768fb2f1e28673bf74d84e3d037f115ac2b3d735af1eea%22%7D",
    ]

    # Số lượng thread mặc định là số lượng tham số
    num_threads = len(param_claims)

    threads = []
    for i in range(num_threads):
        param_claim = param_claims[i]
        thread = threading.Thread(target=claim_reward, args=(param_claim, i+1))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
