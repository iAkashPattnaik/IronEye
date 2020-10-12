# /usr/root/IronEye - By AkashPattnaik

#    ___                      _____
#   |_ _| _ __   ___   _ __  | ____| _   _   ___
#    | | | '__| / _\\ | '_ \\|  _|  | | | | / _ \\
#    | | | |   | (_) || | | || |___ | |_| ||  __/
#   |___||_|   \\___/ |_| |_||_____| \\__, \\___|
#                                   |___/
#       // Created By Akash Pattnaik \\
#         // Telegram : @AKASH_AM1 \\
#   // Github : github.com/BLUE-DEVIL1134 \\
#
# Create Date : 09/10/2020
# Latest Update On : First Commit
#
# [*] The Idea -
#         The Idea Behind This Project Is That,
#         When I Came On Telegram, I Didn't Had A RDP or Computer
#         And Had To Struggle For It..
#
#         Just Not To Happen With Any Other,
#         This Project Was Made.
pkg install python3-pip -y
pkg install wget -y
pkg install openssh openssl -y
pkg install python -y
pip install -r requirements.txt

# No more Requirement
rm requirements.txt
rm IronEye_Linux.sh
python -m IronEye
