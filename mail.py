import requests
import re
import random
from fake_useragent import UserAgent
import threading

def gen():
    ua = UserAgent()

    while True:
        id = str(random.randrange(10000000, 99999999999))
        #id = 7754347353
        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'user-agent': ua.random,
        }

        data = {
            'variables': f'{{"id":"{id}","render_surface":"PROFILE"}}',
            'doc_id': '8557171251032559',
        }

        try:
            response = requests.post('https://www.instagram.com/graphql/query', headers=headers, data=data)
            response.raise_for_status()
            json_response = response.json()
            #print(json_response)

            if "data" in json_response and "user" in json_response["data"]:
                bio = json_response["data"]["user"]["biography"]
                username = json_response["data"]["user"]["username"]
                follower_count = json_response["data"]["user"]["follower_count"]
                print(bio)
                emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', bio)

                if emails:
                    with open('email_found.txt', 'a') as f:
                        for email in emails:
                            infoo = f"{email}:{username}:{follower_count}"
                            print(f"\033[92m{infoo}\033[0m")
                            f.write(infoo +'\n')
        except:
            pass

threads = []
for _ in range(1000):
    thread = threading.Thread(target=gen)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
