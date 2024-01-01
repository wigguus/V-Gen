import requests
import random
import string
import json
import os
from colorama import *
import time

just_fix_windows_console()

generated = 0
def randomStr(h):
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(h)))
    return result_str
    

os.system("cls")
print(Fore.MAGENTA + "=======================================================\n")
print(Fore.MAGENTA + "       ██╗░░░██╗░░░░░░░██████╗░███████╗███╗░░██╗")
print(Fore.MAGENTA + "       ██║░░░██║░░░░░░██╔════╝░██╔════╝████╗░██║")
print(Fore.MAGENTA + "       ╚██╗░██╔╝█████╗██║░░██╗░█████╗░░██╔██╗██║")
print(Fore.MAGENTA + "       ░╚████╔╝░╚════╝██║░░╚██╗██╔══╝░░██║╚████║")
print(Fore.MAGENTA + "       ░░╚██╔╝░░░░░░░░╚██████╔╝███████╗██║░╚███║")
print(Fore.MAGENTA + "       ░░░╚═╝░░░░░░░░░░╚═════╝░╚══════╝╚═╝░░╚══╝")
print(Fore.MAGENTA + "                \nDEVELOPED BY WIGGUS")
print(Fore.MAGENTA + "\n=======================================================\n")

try:
    howmuch = int(input(Fore.MAGENTA + "How many codes You need to generate?\n- "))
    
except Exception as e:
    print("\nYou Gave Wrong Data try again!")
    pass
print("")

while True:
    if int(generated) <= (howmuch-1):
        url = "https://api.discord.gx.games/v1/direct-fulfillment"
        headers = {
                    'authority': 'api.discord.gx.games',
                    'accept': '*/*',
                    'accept-language': 'en-USen;q=0.9',
                    'content-type': 'application/json',
                    'origin': 'https://www.opera.com',
                    'referer': 'https://www.opera.com/',
                    'sec-ch-ua': '"Opera GX";v="105" "Chromium";v="119" "Not?A_Brand";v="24"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': "Windows",
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'cross-site',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        }
        data = "{\"partnerUserId\":\"" + randomStr(64) + "\"}"
        try:
            time.sleep(1)
            r = requests.post(url, data=data, headers=headers)
            if r.status_code == 200:
                jsondata = json.loads(r.text)
                if jsondata['token']:
                    generated = generated + 1
                    link = "https://discord.com/billing/partner-promotions/1180231712274387115/" + jsondata['token']
                    print(Fore.WHITE + str(generated) + ".   " + link[:90] + "..." + " [" + Fore.GREEN + "VALID, SAVED" +  Fore.WHITE + "]")
                    with open('codes.txt', 'a') as file:
                            file.write(link + "\n")
        except Exception as e:
            print(e)
    else:
        input("\nSuccessfuly generated " + str(howmuch) + " codes!\nAll are saved in codes.txt\n\nClick enter to close program!")
        break
        
           
