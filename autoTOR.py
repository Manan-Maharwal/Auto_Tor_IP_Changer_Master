#!/usr/bin/env python3

import time
import os
import subprocess
import requests

def install_required_packages():
    try:
        check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
        if b'install ok installed' not in check_pip3:
            print('[+] pip3 not installed')
            subprocess.check_output('sudo apt update', shell=True)
            subprocess.check_output('sudo apt install python3-pip -y', shell=True)
            print('[!] pip3 installed successfully')
    except subprocess.CalledProcessError:
        pass

    try:
        import requests
    except Exception:
        print('[+] python3 requests is not installed')
        subprocess.check_output('pip3 install requests', shell=True)
        subprocess.check_output('pip3 install requests[socks]', shell=True)
        print('[!] python3 requests is installed')

def install_tor():
    try:
        check_tor = subprocess.check_output('which tor', shell=True)
    except subprocess.CalledProcessError:
        print('[+] tor is not installed !')
        subprocess.check_output('sudo apt update', shell=True)
        subprocess.check_output('sudo apt install tor -y', shell=True)
        print('[!] tor is installed successfully')

def get_ip():
    url = 'https://www.myexternalip.com/raw'
    proxies = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'}
    get_ip = requests.get(url, proxies=proxies)
    return get_ip.text

def change_ip():
    os.system("service tor reload")
    print(f'[+] Your IP has been changed to: {get_ip()}')

def main():
    os.system("clear")
    print('''
                _          _______
     /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
   / /\ \| | | | __/ _ \     | |/ _ \| '__|
  / ____ \ |_| | || (_) |    | | (_) | |
 /_/    \_\__,_|\__\___/     |_|\___/|_|
                V 2.1
from mrFD
''')
    print("\033[1;40;31m https://instagram.com/mananmaharwal_26/\n")

    install_required_packages()
    install_tor()

    os.system("service tor start")

    time.sleep(3)
    print("\033[1;32;40m Change your SOCKS to 127.0.0.1:9050\n")

    x = int(input("[+] Time to change IP in seconds [type=60] >> "))
    lin = int(input("[+] How many times do you want to change your IP [type=1000] for infinite IP change type [0] >> "))

    if lin == 0:
        while True:
            try:
                time.sleep(x)
                change_ip()
            except KeyboardInterrupt:
                print('\nauto tor is closed')
                quit()
    else:
        for i in range(lin):
            time.sleep(x)
            change_ip()

if __name__ == '__main__':
    main()