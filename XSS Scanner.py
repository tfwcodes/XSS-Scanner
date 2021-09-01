try:
    import requests
except ModuleNotFoundError:
    print("You do not have requests install ")
from time import sleep

count = 0

def check_url_xss(url):
    try:
        s2 = requests.session()
        response = s2.get(url)
        if response.status_code == 200:
            print("[INFO] The url is valid")
        elif response.status_code == 404:
            print("[INFO] The url is invalid")
            sleep(1)
            exit()
    except KeyboardInterrupt:
        exit()

def do_req(url):
    global count
    payload = open("payloads", "r")
    for word in payload:
        data = {
            'rcr_authenticate': '1',
            'rcr_user': 'sfds',
            'rcr_pass': word,
            'rcr_submit': 'Conectare'
        }

        s = requests.session()
        response = s.post(url, data=data)
        count +=1

        content_length = response.headers['content-length']
        print("-"*50)
        print(f"[ATTACK] Content-length: {content_length}, Request number: {count}, with the payload {word}")
        print("-"*50)

print(
    """
    
    __  ______ ____    ____                                  
    \ \/ / ___/ ___|  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
     \  /\___ \___ \  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
     /  \ ___) |__) |  ___) | (_| (_| | | | | | | |  __/ |    ~>XSS Scanner<~
    /_/\_\____/____/  |____/ \___\__,_|_| |_|_| |_|\___|_|  ~~>Made by tfwcodes(github)<~~ 
                                                         
    """
)

url = input("[+] Enter the target url: ")
check_url_xss(url)
sleep(1)
do_req(url)