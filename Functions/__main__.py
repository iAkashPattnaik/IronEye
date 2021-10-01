r"""
  ____              _
 / ___| _   _  ___ | |_   ___   _ __ ___
| |    | | | |/ __|| __| / _ \ | '_ ` _ \
| |___ | |_| |\__ \| |_ | (_) || | | | | |
 \____| \__,_||___/ \__| \___/ |_| |_| |_|

      ____                 __  _
    / ___|  ___   _ __   / _|(_)  __ _  ___
   | |     / _ \ | '_ \ | |_ | | / _` |/ __|
   | |___ | (_) || | | ||  _|| || (_| |\__ \
   \____| \___/ |_| |_||_|  |_| \__, ||___/
                                |___/

A Better Way Of Cracking Or DDOS Attacks,
With CustomConfigs, AnyThing Will be Vulnerable.

"""
# In-Built
import time
import datetime
from json import loads, dumps, JSONDecodeError
import os

# Site-Packages
from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup

# IronEye
# from IronEye import functionsLogger


__all__ = (
    "CurrentUnixTime",
    "UnixTimeToDate",
    "URLEncode",
    "Length",
    "JSON",
    "JsonToString",
    "StringToJson",
    "requestGet",
    "requestPost",
    "HitSaver",
    "GetRandomUA",
    "BeautifulSoup",
    "functionsLogger",
)


class Logger(object):
    def __init__(self):
        fileName = str(datetime.datetime.now()).split(" ")[0]
        if os.path.exists(f'./Logs/{fileName}.txt'):
            self.functionsLogger = open(f'./Logs/{fileName}.txt', mode='a')
        else:
            self.functionsLogger = open(f'./Logs/{fileName}.txt', mode='x')
        self.functionsLogger.write(f'\n\n[{str(datetime.datetime.now()).split(" ")[1].split(".")[0]}]\n')

    def info(self, area, log):
        if not self.functionsLogger.closed:
            self.functionsLogger.write(
                f'[INFO] [{area}]\n\t{log}\n'
            )
            return True

    def warn(self, area, log):
        if not self.functionsLogger.closed:
            self.functionsLogger.write(
                f'[WARN] [{area}]\n\t{log}\n'
            )
            return True

    def error(self, area, log):
        if not self.functionsLogger.closed:
            self.functionsLogger.write(
                f'[ERROR] [{area}]\n\t{log}\n'
            )
            return True

    def close(self):
        if not self.functionsLogger.closed:
            self.functionsLogger.close()
            return True


functionsLogger = Logger()


if __name__ == '__main__':
    pass

def CurrentUnixTime():
    return time.time()


def UnixTimeToDate(unixTime: int):
    return str(datetime.datetime.fromtimestamp(unixTime))


def URLEncode(String):
    try:
        return quote_plus(String)
    except Exception as error:
        functionsLogger.error(area='Functions.URLEncode', log=str(error))
        return String


def Length(Content):
    return len(Content)


def JSON(Content, Key):
    try:
        return loads(Content)[Key]
    except Exception as error:
        functionsLogger.error(area='Functions.JSON', log=str(error))
        return None


def JsonToString(Content):
    try:
        return dumps(Content)
    except JSONDecodeError as error:
        functionsLogger.error(area='Functions.JsonToString', log=str(error))
        return None


def StringToJson(Content):
    try:
        return loads(Content)
    except JSONDecodeError as error:
        functionsLogger.error(area='Functions.StringToJson', log=str(error))
        return None


def requestGet(url: str, headers=None):
    """Makes A GET Request To A Specified Url Address

    :param url: str url address. e.g. https://github.com/BLUE-DEVIL1134/
    :param headers: dictionary or json basically, e.g. { "refer": "https://github.com/", }
    :return: :class:`Functions.requestGet.returnData <Functions.requestGet.returnData>` object
    :rtype: Functions.requestGet.returnData
    """

    class returnData:
        def __init__(self, text, status_code, responseHeaders, json):
            self.text = text
            self.statusCode = status_code
            self.headers = responseHeaders
            self.json = json

    if headers is None:
        headers = {}
    try:
        req = requests.get(url=url, headers=headers)
        return returnData(text=req.text, status_code=req.status_code, responseHeaders=headers, json=req.json())
    except Exception as error:
        functionsLogger.error(area='Functions.requestGet', log=str(error))
        return False


def requestPost(url: str, content, headers=None):
    """Makes A GET Request To A Specified Url Address

    :param url: str url address. e.g. https://github.com/BLUE-DEVIL1134/
    :param content: Either Url EncodedString Or Dictionary, e.g. "login=xyz@xyz.com&secret=xyz"
    :param headers: dictionary or json basically, e.g. { "refer": "https://github.com/" }
    :return: :class:`Functions.requestPost.returnData <Functions.requestPost.returnData>` object
    :rtype: Functions.requestPost.returnData
    """

    class returnData:
        def __init__(self, text, status_code, responseHeaders):
            self.text = text
            self.statusCode = status_code
            self.headers = responseHeaders

    if headers is None:
        headers = {}
    if isinstance(content, str):
        # For Less Bugs
        content = quote_plus(content)
    try:
        req = requests.post(url=url, data=content, headers=headers)
        return returnData(text=req.text, status_code=req, responseHeaders=headers)
    except Exception as error:
        functionsLogger.error(area='Functions.requestPost', log=str(error))


def HitSaver(fileName: str, hit: str, extraContent: str = ''):
    """Saves Hits To A Specified File

    :param fileName: The Hits File Name, e.g. `CustomConfigHits`
                     Note:- The Extension Is Fixed To `.ir` So No Need To Add Anything,
                            All Will Be Saved In `root:/IronEye/HitsDB/`, Don't Add The Prefix `IronEye/HitsDB/`.
    :param hit: The Combo Only. e.g. xyz@xyz.com:xyz
    :param extraContent: Info Like TimeLeft, PlatName, Balance ...etc.
    :return: bool, True on Success And False On Error
    """
    for i in ['/', '\\', '"', "'", ":", ">", "<", "*", "?", "|"]:
        if i in fileName:
            functionsLogger.error(area='Functions.HitSaver', log=f'{i} in {fileName}')
            return exit(7)
    with open(file=f'./HitsDB/{fileName}.ir', mode='a', encoding="utf-8") as file:
        try:
            file.write(
                str(
                    f'\n⫸⫘⫘⫘⫘⫘⫘IronEye⫘⫘⫘⫘⫘⫘⫷\n'
                    f'Combo - {hit}\n'
                    f'Login - {hit.split(":")[0]}\n'
                    f'Secret - {hit.split(":")[1]}\n'
                    f'AdditionalInfo - {extraContent}\n'
                )
            )
            file.close()
            return True
        except Exception as error:
            file.close()
            functionsLogger.error(area='Functions.HitSaver', log=str(error))
            return False


def GetRandomUA():
    pass
