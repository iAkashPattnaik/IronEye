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
        apt update -y && apt upgrade -y
        apt install git -y
        apt install python -y

        git clone https://github.com/BLUE-DEVIL1134/IronEye.git
        cd IronEye
        pip install requirements.txt
        chmod +x *
        python -n IronEye
"""

__version__ = '4.0.0'
__email__ = "akashpattnaik.github@gmail.com"
__author__ = "AkashPattnaik"
__telegram__ = "https://telegram.me/AKASH_AM1"
__copyright__ = "(c) Akash Pattnaik 2020-2025"
__github__ = "https://github.com/BLUE-DEVIL1134/IronEye"
__pypi__ = "https://pypi.org/profile/AkashPattnaik"
__latest_update__ = "01/10/2021"
__all__ = (
    "logger"
)

from datetime import datetime
import os
from colorama import Fore


# Best If You Create Your Own Logger
class Logger(object):
    def __init__(self):
        if not os.path.exists('./Logs/'):
            print(f'No Logs Dir Found...\nPlease run {Fore.CYAN}"ironeye init"{Fore.RESET} First.')
        fileName = str(datetime.now()).split(" ")[0]
        if os.path.exists(f'./Logs/{fileName}.txt'):
            self.logger = open(f'./Logs/{fileName}.txt', mode='a')
        else:
            self.logger = open(f'./Logs/{fileName}.txt', mode='x')
        self.logger.write(f'\n\n[{str(datetime.now()).split(" ")[1].split(".")[0]}]\n')

    def info(self, area, log):
        self.logger.write(
            f'[INFO] [{area}]\n\t{log}\n'
        )

    def warn(self, area, log):
        self.logger.write(
            f'[WARN] [{area}]\n\t{log}\n'
        )
        return True

    def error(self, area, log):
        self.logger.write(
            f'[ERROR] [{area}]\n\t{log}\n'
        )
        return True


logger = Logger()


if __name__ == '__main__':
    logger.info(area='IronEye.__init__', log='Initiating IronEye')
