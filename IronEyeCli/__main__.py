# Build-In
import shutil
import sys
import time
from datetime import datetime
from platform import python_version, system
import os
from threading import Thread

# Site-Packages
from colorama import Fore, init, Back
from requests import get

# IronEye
from Functions import functionsLogger
from IronEye import __version__


def versionCheck():
    try:
        latestVersion = get('https://raw.githubusercontent.com/BLUE-DEVIL1134/IronEye/main/version.txt').text
        if __version__ != latestVersion:
            r = Fore.RESET
            c = Fore.CYAN
            re = Fore.RED
            print(
                f"  {c}╔══════════════════════════════════════════════════════════════════════════╗{r}\n"
                f"  {c}║{r} A new version of IronEye is available!                                   {c}║{r}\n"
                f"  {c}║{r}                                                                          {c}║{r}\n"
                f"  {c}║{r} To upgrade to the latest version, run \"{re}ironeye upgrade{r}\".                 {c}║{r}\n"
                f"  {c}╚══════════════════════════════════════════════════════════════════════════╝{r}\n"
            )
    except Exception as error:
        functionsLogger.error(area='IronEyeCli.versionCheck', log=str(error))
        pass


class Upgrade:
    def __init__(self):
        self.start = time.time()
        self.p1 = Thread(target=self.loading)
        self.p2 = Thread(target=self._upgrade)
        self.p2.start()
        self.p2.join()

    def loading(self):
        while self.p2.is_alive():
            for _ in ['-', '\\', '|', '/']:
                print(f"{Fore.RESET}Running IronEye task 'Upgrade'...         ", end=f'{_}\r')
                time.sleep(0.1)
        print(f"{Fore.RESET}Running IronEye task 'Upgrade'...         {Fore.GREEN}Done.{Fore.RESET}")
        time.sleep(4)
        print(f"Running IronEye task 'Upgrade'...         {Fore.GREEN}{time.time() - self.start:.2f}s{Fore.RESET}")

    def _upgrade(self):
        self.p1.start()
        try:
            os.system('git pull origin main --force')
            try:
                confirmation = input(f'{Fore.GREEN}Install Latest Dependencies (Y/N)? {Fore.RESET}').lower()
                if confirmation == 'y':
                    if system() == 'Windows':
                        os.system("pip install -r requirements.txt --quiet --no-python-version-warning --no-color")
                    else:
                        os.system("python3 -m pip install -r "
                                  "requirements.txt --quiet --no-python-version-warning --no-color")
                else:
                    if os.path.exists('.ironeye/'):
                        try:
                            shutil.rmtree('./.ironeye/')
                        except Exception as error:
                            functionsLogger.error(area="IronEyeCli.del.ironeye/", log=str(error))
            except KeyboardInterrupt:
                exit(3)
        except Exception as error:
            functionsLogger.error(area="IronEyeCli.Upgrade", log=str(error))


if __name__ == '__main__':
    init()
    versionCheck()

try:
    query = sys.argv[1].lower()
except IndexError:
    query = 'help'

if query not in [
    'help', '-h', '--help', '-v', 'version', '-l', 'logs', '-c', 'clogs', 'run', 'upgrade', '-r', 'reset', 'init'
]:
    query = 'help'

if query == 'help' or query == '-h' or query == '--help':
    print(
        f"Manage your IronEye with IronEyeCli\n"
        f"\n"
        f"Common commands:\n"
        f"  {Fore.CYAN}ironeye run{Fore.RESET}\n"
        f"    Run IronEye Instantly.\n"
        f"  {Fore.CYAN}ironeye upgrade{Fore.RESET}\n"
        f"    Upgrade IronEye Without Starting It.\n"
        f"\n"
        f"Usage: ironeye <command> [optional-arguments]\n"
        f"Global options:\n"
        f"    {Fore.CYAN}-h, --help      Print this usage information.{Fore.RESET}\n"
        f"    {Fore.CYAN}-v, --version   Print the required and current Python version.{Fore.RESET}\n"
        f"\n"
        f"Available commands:\n"
        f"    {Fore.CYAN}run        :   {Fore.RESET}Run IronEye instantly.\n"
        f"    {Fore.CYAN}upgrade    :   {Fore.RESET}Upgrade IronEye to latest version.\n"
        f"    {Fore.CYAN}-h, help   :   {Fore.RESET}Print this usage information.\n"
        f"    {Fore.CYAN}-v, version:   {Fore.RESET}Print the required and current Python version.\n"
        f"    {Fore.CYAN}-l, logs   :   {Fore.RESET}Print recent IronEye logs.\n"
        f"    {Fore.CYAN}-c, clogs  :   {Fore.RESET}Clear recent IronEye logs.\n"
        f"    {Fore.CYAN}reset      :   {Fore.RESET}Reset IronEye as initial clone copy.\n"
        f"\n"
        f"{Back.RED}{Fore.GREEN}[Warning]{Fore.RESET}{Back.RESET}\n"
        f"Run \"{Fore.RED}ironeye reset{Fore.RESET}\" only when advised by \"t.me/AKASH_AM1\"\n"
    )
elif query == '-v' or query == 'version':
    print(
        f"Current version • {Fore.CYAN}Python {python_version()}{Fore.RESET}\n"
        f"Required version • {Fore.GREEN}Python 3.9.1{Fore.RESET}\n"
        f"IronEye • {Fore.YELLOW}{__version__} [Release] • https://github.com/BLUE-DEVIL1134/IronEye.git{Fore.RESET}\n"
        f"Platform • {Fore.BLUE}{system()}{Fore.RESET}\n"
    )
    print(
        f'You are {Fore.CYAN}good to run{Fore.RESET} IronEye' if python_version() == '3.9.7'
        else f'Please {Fore.RED}Upgrade{Fore.RESET} to Python 3.9.7 to use IronEye'
    )
elif query == '-l' or query == 'logs':
    if not os.path.exists('./Logs'):
        print(f'{Fore.RED}No logs file found.{Fore.RESET}')
        exit(2)
    fileName = str(datetime.now()).split(" ")[0]
    if not os.path.exists(f'./Logs/{fileName}.txt'):
        print(f'{Fore.RED}No logs file found.{Fore.RESET}')
        exit(2)
    os.system('cls' if system() == 'Windows' else 'clear')
    file = open(file=f'./Logs/{fileName}.txt', mode='r')
    logs = file.read()
    file.close()
    print(f"{Fore.YELLOW}{logs}{Fore.RESET}\n")
    x = input(f'{Fore.GREEN}Press enter to clear screen (q/Q to Quit) \\? {Fore.RESET}')
    if x == '':
        os.system('cls' if system() == 'Windows' else 'clear')
    else:
        quit(3)
elif query == '-c' or query == 'clogs':
    start = time.time()
    if not os.path.exists('./Logs'):
        print(f'{Fore.RED}No logs file found.{Fore.RESET}')
        exit(2)
    print(
        f'{Back.RED}{Fore.GREEN}[Warning]{Fore.RESET}{Back.RESET}\n'
        f'{Fore.RED}  Deleting IronEye Log Files{Fore.RESET}'
    )
    fileName = str(datetime.now()).split(" ")[0]
    functionsLogger.close()
    for i in os.listdir('./Logs/'):
        try:
            os.remove(f'./Logs/{i}')
            print(f'    ./Logs/{Fore.CYAN}{i}{Fore.RESET}:    (deleted)')
        except PermissionError:
            pass
    shutil.rmtree('./Logs/')
    print(f'    {Fore.CYAN}./Logs/              {Fore.RESET}:    (deleted)')
    print(f'{Fore.RESET}Running IronEye task \'clearLogs\'.    {Fore.GREEN}Done {time.time() - start:.2f}s{Fore.RESET}')
elif query == 'run':
    sys.exit(
        os.system('python -m IronEye')
    )
elif query == 'upgrade':
    Upgrade()
elif query == 'init':
    logsDir = os.path.exists('./Logs/')
    functionsDir = os.path.exists('./Functions/')
    ironeyeDir = os.path.exists('./IronEye/')
    if logsDir and functionsDir and ironeyeDir:
        print(f"{Fore.CYAN}IronEye Initialise Successful !{Fore.RESET}\n"
              f"Run \"{Fore.GREEN}ironeye run{Fore.RESET}\" To Start IronEye.")
    else:
        if not logsDir:
            functionsLogger.info(area='IronEyeCli.init', log="Making Logs Dir")
            os.mkdir('./Logs/')
        if not functionsDir:
            functionsLogger.warn(area='IronEyeCli.init', log="Git Clone Was Not Successful")
            os.mkdir('./Functions/')
            # Git Clone Was Not Successful
            Upgrade()
        if not ironeyeDir:
            functionsLogger.warn(area='IronEyeCli.init', log="Git Clone Was Not Successful")
            os.mkdir('./IronEye/')
            # Git Clone Was Not Successful
            Upgrade()

# TODO - -r, reset
