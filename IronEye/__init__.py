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
Latest Update On : First Commit

[*] The Idea -
        The Idea Behind This Project Is That,
        When I Came On Telegram, I Didn't Had A RDP or Computer
        And Had To Struggle For It..

        Just Not To Happen With Any Other,
        This Project Was Made.
"""

__version__ = 1.1
__email__ = "akashpattnaik.github@gmail.com"
__author__ = "Akash Pattnaik"
__telegram__ = "https://telegram.me/AKASH_AM1"
__copyright__ = "(c) Akash Pattnaik 2020-2025"
__github__ = "https://github.com/BLUE-DEVIL1134/IronEye"
__Pypi__ = "https://pypi.org/user/AkashPattnaik/"
__latest_update__ = "15-10-2020"

class PersonalException(ConnectionError):
    def __init__(self):
        print("Seems That You Have Some Internet Problems.\n"
              "Retrying..")
        pass
