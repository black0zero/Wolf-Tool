#####################################################
#####################################################
##                      		           ##
##              			      	   ##
##              code by: black0zero   	           ##
##                                		   ##
##                              		   ##
#####################################################
#####################################################
import os
import sys
import time
from random import choice
from time import sleep as timeout

#####################################################
time.sleep(1)
os.system("clear")
#####################################################


def banner():
    print(
        " \033[1;34m             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@@@@@@@@@@@@@@@'~~~     ~~~`@@@@@@@@@@@@@@@@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@@@@@@@@@@'                     `@@@@@@@@@@@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@@@@@@@'                           `@@@@@@@@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@@@@@'                              \033[1;34m `@@@@@@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@@@'              \033[1;33mWolf Tool         \033[1;34m   `@@@@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@@'                                 \033[1;34m    `@@@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@'                                  \033[1;34m     `@@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@                                   \033[1;34m      @@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@'        \033[1;31m              n,           \033[1;34m      `@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@         \033[1;31m            _/ | _         \033[1;34m       @@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@         \033[1;31m           /'  `'/         \033[1;34m       @@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@a        \033[1;31m         <~    .'          \033[1;34m      a@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@        \033[1;31m         .'    |           \033[1;34m      @@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@a       \033[1;31m       _/      |           \033[1;34m     a@@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@@a      \033[1;31m     _/      `.`.          \033[1;34m    a@@@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@@@a     \033[1;31m____/ '   \__ | |______    \033[1;34m   a@@@@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@@@@@a\033[1;31m__/___/      /__\ \ \     \___\033[1;34m.a@@@@@@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@@@@@\033[1;31m/  (___.'\_______)\_|_|        \ \033[1;34m@@@@@@@@@@@@@@@ "
    )
    timeout(0.1)
    print(
        " \033[1;34m             @@@@@@@@@@@@|\033[1;31m\________     \033[1;33mWolf Tool        \033[1;34m ~~~~~\@@@@@@@@@@ "
    )
    timeout(0.1)


# --------------------------------------------------------#
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


# --------------------------------------------------------#
def main():
    print(
        """
"""
    )
    print(
        " \033[1;33m  ------------------------------------------------------------------------------------▪"
    )
    print(
        " \033[1;33m |\033[1;34m[01] \033[1;31mTermux Basics          \033[1;33m| \033[1;34m[02] \033[1;31mTermux Style         \033[1;33m| \033[1;34m[03] \033[1;31mMetaSploit           \033[1;33m|"
    )
    timeout(0.09)
    print(
        " \033[1;33m |----------------------------|---------------------------|---------------------------|"
    )
    print(
        " \033[1;33m |\033[1;34m[04] \033[1;31mA-Rat                  \033[1;33m| \033[1;34m[05] \033[1;31mLedear Hacker        \033[1;33m| \033[1;34m[06] \033[1;31mRoutersploit         \033[1;33m|"
    )
    timeout(0.09)
    print(
        " \033[1;33m |----------------------------|---------------------------|---------------------------|"
    )
    print(
        " \033[1;33m |\033[1;34m[07] \033[1;31mSqlmap                 \033[1;33m| \033[1;34m[08] \033[1;31mNmap                 \033[1;33m| \033[1;34m[09] \033[1;31mRed Hawk             \033[1;33m|"
    )
    timeout(0.09)
    print(
        " \033[1;33m |----------------------------|---------------------------|---------------------------|"
    )
    print(
        " \033[1;33m |\033[1;34m[10] \033[1;31mWOscan                 \033[1;33m| \033[1;34m[11] \033[1;31mWeb Sploit           \033[1;33m| \033[1;34m[12] \033[1;31mXshell               \033[1;33m|"
    )
    timeout(0.09)
    print(
        " \033[1;33m |----------------------------|---------------------------|---------------------------|"
    )
    print(
        " \033[1;33m |\033[1;34m[13] \033[1;31mWPScan                 \033[1;33m| \033[1;34m[14] \033[1;31mXAttacker            \033[1;33m| \033[1;34m[15] \033[1;31mSqldump              \033[1;33m|"
    )
    timeout(0.09)
    print(
        " \033[1;33m |----------------------------|---------------------------|---------------------------|"
    )
    print(
        " \033[1;33m |\033[1;34m[16] \033[1;31mXadmin                 \033[1;33m| \033[1;34m[17] \033[1;31mXSStrike             \033[1;33m| \033[1;34m[18] \033[1;31mNikto                \033[1;33m|"
    )
    timeout(0.09)
    print(
        " \033[1;33m |----------------------------|---------------------------|---------------------------|"
    )
    print(
        " \033[1;33m |\033[1;34m[19] \033[1;31mHammer                 \033[1;33m| \033[1;34m[20] \033[1;31mb0mbr3               \033[1;33m| \033[1;34m[21] \033[1;31mWeeman               \033[1;33m|"
    )
    timeout(0.09)
    print(
        " \033[1;33m |----------------------------|---------------------------|---------------------------|"
    )
    print(
        " \033[1;33m |\033[1;34m[22] \033[1;31mHash Buster            \033[1;33m| \033[1;34m[23] \033[1;31mHasher               \033[1;33m| \033[1;34m[24] \033[1;31mFedora               \033[1;33m|"
    )
    timeout(0.09)
    print(
        " \033[1;33m |----------------------------|---------------------------|---------------------------|"
    )
    print(
        " \033[1;33m |\033[1;34m[25] \033[1;31mWifite                 \033[1;33m| \033[1;34m[26] \033[1;31mCam-Hacker           \033[1;33m| \033[1;34m[27] \033[1;31mSaycheese            \033[1;33m|"
    )
    timeout(0.09)
    print(
        " \033[1;33m |----------------------------|---------------------------|---------------------------|"
    )
    print(
        " \033[1;33m |\033[1;34m[28] \033[1;31mULtimate-Dork          \033[1;33m| \033[1;34m[29] \033[1;31mDestroyer-framework  \033[1;33m| \033[1;34m[00]  \033[1;36mExit tool...!!       \033[1;33m|"
    )
    timeout(0.09)
    print(
        " \033[1;33m ▪----------------------------▪---------------------------▪---------------------------▪"
    )
    print(
        """

"""
    )
    timeout(0.09)


###########################################################################

banner()

if __name__ == "__main__":
    timeout(1)
    main()

    #################### Install Termux Basics ##############
    choice_tool = input("\033[1;35mSet Install Tool >>\033[1;36m ")
    if choice_tool == "1" or choice_tool == "01":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print(
            " \033[1;32m  _____                                ____            _           "
        )
        print(
            " \033[1;32m |_   _|__ _ __ _ __ ___  _   ___  __ | __ )  __ _ ___(_) ___ ___  "
        )
        print(
            " \033[1;32m   | |/ _ \ '__| '_ ` _ \| | | \ \/ / |  _ \ / _` / __| |/ __/ __| "
        )
        print(
            " \033[1;32m   | |  __/ |  | | | | | | |_| |>  <  | |_) | (_| \__ \ | (__\__ \ "
        )
        print(
            " \033[1;32m   |_|\___|_|  |_| |_| |_|\__,_/_/\_\ |____/ \__,_|___/_|\___|___/ "
        )
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system(
            " apt update; apt upgrade; apt list upgradable; apt upgrade -y; termux-setup-storage; apt-get update; apt-get upgrade -y; apt install php -y; apt install python -y; apt install python2 -y; apt install git -y; apt install golang -y; apt install cmatrix -y; apt install figlet -y; apt install wget -y; apt install cowsay -y; apt install fish -y "
        )
        os.system(
            " apt install toilet -y; apt install ruby -y; gem install lolcat; apt install curl -y; apt install wgetrc -y; apt install unzip y; apt install openssh -y; apt install tor -y; apt install net-tools -y; apt install unrar -y; apt install clang -y; apt install w3m -y; apt install proot -y;apt install wget -y; pip install --upgrade pip; apt update && apt upgrade"
        )
        timeout(1)
        print(
            """

"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00] \033[1;31mExit ...! ")
        print("""
"""
              )
        install_tool = input("\033[1;35mSet Install >> \033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()
    #################### Termux Style #######################

    if choice_tool == "2" or choice_tool == "02":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print(
            " \033[1;32m _____                                ____  _         _       "
        )
        print(
            " \033[1;32m|_   _|__ _ __ _ __ ___  _   ___  __ / ___|| |_ _   _| | ___  "
        )
        print(
            " \033[1;32m  | |/ _ \ '__| '_ ` _ \| | | \ \/ / \___ \| __| | | | |/ _ \ "
        )
        print(
            " \033[1;32m  | |  __/ |  | | | | | | |_| |>  <   ___) | |_| |_| | |  __/ "
        )
        print(
            " \033[1;32m  |_|\___|_|  |_| |_| |_|\__,_/_/\_\ |____/ \__|\__, |_|\___| "
        )
        print(
            " \033[1;32m                                                |___/         "
        )
        print(
            """ \033[1;33m

"""
        )
        timeout(1)
        os.system("git clone https://github.com/B4N954N2-ID/termux-style")
        os.system("mv termux-style Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """

"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00] \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()
    #################### MetaSploit_In_Termux ###############

    if choice_tool == "3" or choice_tool == "03":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m __  __      _        ____        _       _ _    ")
        print("\033[1;32m|  \/  | ___| |_ __ _/ ___| _ __ | | ___ (_) |_  ")
        print("\033[1;32m| |\/| |/ _ \ __/ _` \___ \| '_ \| |/ _ \| | __| ")
        print("\033[1;32m| |  | |  __/ || (_| |___) | |_) | | (_) | | |_  ")
        print("\033[1;32m|_|  |_|\___|\__\__,_|____/| .__/|_|\___/|_|\__| ")
        print("\033[1;32m                           |_|                   ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("apt s://github.com/gushmazuko/metasploit_in_termux")
        os.system(
            "mv metasploit_inupdate; apt upgrade -y; apt install git -y; apt install ruby -y; apt install unstable-repo"
        )
        os.system("git clone http_termux $HOME")
        os.system(
            "cd && cd metasploit_in_termux && chmod +x metasploit.sh && ./metasploit.sh"
        )
        os.system("cd && rm -rf metasploit_in_termux")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00] \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### A-Rat ##############################

    if choice_tool == "4" or choice_tool == "04":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m    _         ____       _    ")
        print("\033[1;32m   / \       |  _ \ __ _| |_  ")
        print("\033[1;32m  / _ \ _____| |_) / _` | __| ")
        print("\033[1;32m / ___ \_____|  _ < (_| | |_  ")
        print("\033[1;32m/_/   \_\    |_| \_\__,_|\__| ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("git clone https://github.com/RexTheGod/A-Rat")
        os.system("mv A-Rat Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Ledear Hacker ######################

    if choice_tool == "5" or choice_tool == "05":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print(
            "\033[1;32m  _             _                   _   _            _              "
        )
        print(
            "\033[1;32m | |    ___  __| | ___  __ _ _ __  | | | | __ _  ___| | _____ _ __  "
        )
        print(
            "\033[1;32m | |   / _ \/ _` |/ _ \/ _` | '__| | |_| |/ _` |/ __| |/ / _ \ '__| "
        )
        print(
            "\033[1;32m | |__|  __/ (_| |  __/ (_| | |    |  _  | (_| | (__|   <  __/ |    "
        )
        print(
            "\033[1;32m |_____\___|\__,_|\___|\__,_|_|    |_| |_|\__,_|\___|_|\_\___|_|    "
        )
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("apt install python2 -y")
        os.system("git clone https://github.com/Ledear-Hacker/LEDEAR_HACKING ")
        os.system("mv LEDEAR_HACKING Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### RouterSploit #######################

    if choice_tool == "6" or choice_tool == "06":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print(
            "\033[1;32m  ____             _            ____        _       _ _    ")
        print(
            "\033[1;32m |  _ \ ___  _   _| |_ ___ _ __/ ___| _ __ | | ___ (_) |_  ")
        print(
            "\033[1;32m | |_) / _ \| | | | __/ _ \ '__\___ \| '_ \| |/ _ \| | __| ")
        print(
            "\033[1;32m |  _ < (_) | |_| | ||  __/ |   ___) | |_) | | (_) | | |_  ")
        print(
            "\033[1;32m |_| \_\___/ \__,_|\__\___|_|  |____/| .__/|_|\___/|_|\__| ")
        print(
            "\033[1;32m                                     |_|                   ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("pip install future")
        os.system("git clone https://github.com/threat9/routersploit ")
        os.system("mv routersploit Tools")
        os.system(
            "cd Tools && cd routersploit; python2 -m pip install -r requirements.txt"
        )
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Sqlmap #############################

    if choice_tool == "7" or choice_tool == "07":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m  ____        _                       ")
        print("\033[1;32m / ___|  __ _| |_ __ ___   __ _ _ __  ")
        print("\033[1;32m \___ \ / _` | | '_ ` _ \ / _` | '_ \ ")
        print("\033[1;32m  ___) | (_| | | | | | | | (_| | |_) |")
        print("\033[1;32m |____/ \__, |_|_| |_| |_|\__,_| .__/ ")
        print("\033[1;32m           |_|                 |_|    ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("apt install python -y")
        os.system("git clone https://github.com/sqlmapproject/sqlmap ")
        os.system("mv sqlmap Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Namp ###############################

    if choice_tool == "8" or choice_tool == "08":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m  _   _                       ")
        print("\033[1;32m | \ | |_ __ ___   __ _ _ __  ")
        print("\033[1;32m |  \| | '_ ` _ \ / _` | '_ \ ")
        print("\033[1;32m | |\  | | | | | | (_| | |_) |")
        print("\033[1;32m |_| \_|_| |_| |_|\__,_| .__/ ")
        print("\033[1;32m                       |_|    ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("apt update; apt upgrade -y")
        os.system("apt install nmap -y ")
        print("|---------------------------------------------------------------|")
        print("|------------------------ Download Done ------------------------|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Red Hawk ###########################

    if choice_tool == "9" or choice_tool == "09":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m  ____          _   _   _                _      ")
        print("\033[1;32m |  _ \ ___  __| | | | | | __ ___      _| | __  ")
        print("\033[1;32m | |_) / _ \/ _` | | |_| |/ _` \ \ /\ / / |/ /  ")
        print("\033[1;32m |  _ <  __/ (_| | |  _  | (_| |\ V  V /|   <   ")
        print("\033[1;32m |_| \_\___|\__,_| |_| |_|\__,_| \_/\_/ |_|\_\  ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("apt install php -y ")
        os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK ")
        os.system("mv RED_HAWK Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### WOscan #############################

    if choice_tool == "10":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m __        _____                       ")
        print("\033[1;32m \ \      / / _ \ ___  ___ __ _ _ __   ")
        print("\033[1;32m  \ \ /\ / / | | / __|/ __/ _` | '_ \  ")
        print("\033[1;32m   \ V  V /| |_| \__ \ (_| (_| | | | | ")
        print("\033[1;32m    \_/\_/  \___/|___/\___\__,_|_| |_| ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("git clone https://github.com/Gameye98/OWScan ")
        os.system("mv OWScan Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Web Sploit #########################

    if choice_tool == "11":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m __        __   _       ____        _       _ _    ")
        print("\033[1;32m \ \      / /__| |__   / ___| _ __ | | ___ (_) |_  ")
        print("\033[1;32m  \ \ /\ / / _ \ '_ \  \___ \| '_ \| |/ _ \| | __| ")
        print("\033[1;32m   \ V  V /  __/ |_) |  ___) | |_) | | (_) | | |_  ")
        print("\033[1;32m    \_/\_/ \___|_.__/  |____/| .__/|_|\___/|_|\__| ")
        print("\033[1;32m                             |_|                   ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("git clone https://github.com/The404Hacking/websploit ")
        os.system("mv websploit Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Xshell #############################

    if choice_tool == "12":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m __  __        _              _   _  ")
        print("\033[1;32m \ \/ /  ___  | |__     ___  | | | | ")
        print("\033[1;32m  \  /  / __| | '_ \   / _ \ | | | | ")
        print("\033[1;32m  /  \  \__ \ | | | | |  __/ | | | | ")
        print("\033[1;32m /_/\_\ |___/ |_| |_|  \___| |_| |_| ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("git clone https://github.com/Ubaii/Xshell ")
        os.system("mv Xshell Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### WPScan #############################

    if choice_tool == "13":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m __        ______  ____                   ")
        print("\033[1;32m \ \      / /  _ \/ ___|  ___ __ _ _ __   ")
        print("\033[1;32m  \ \ /\ / /| |_) \___ \ / __/ _` | '_ \  ")
        print("\033[1;32m   \ V  V / |  __/ ___) | (_| (_| | | | | ")
        print("\033[1;32m    \_/\_/  |_|   |____/ \___\__,_|_| |_| ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("git glone https://github.com/wpscanteam/wpscan ")
        os.system("mv wpscan Tools")
        os.system("cd Tools && cd wpscan")
        os.system(
            "gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update"
        )
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()
    #################### XAttacker ##########################

    if choice_tool == "14":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m __  __     _   _   _             _              ")
        print("\033[1;32m \ \/ /    / \ | |_| |_ __ _  ___| | _____ _ __  ")
        print("\033[1;32m  \  /    / _ \| __| __/ _` |/ __| |/ / _ \ '__| ")
        print("\033[1;32m  /  \   / ___ \ |_| || (_| | (__|   <  __/ |    ")
        print("\033[1;32m /_/\_\ /_/   \_\__|\__\__,_|\___|_|\_\___|_|    ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("git clone https://github.com/Moham3dRiahi/XAttacker")
        os.system("mv XAttacker Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Sqldump ############################

    if choice_tool == "15":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m  ____        _     _                        ")
        print("\033[1;32m / ___|  __ _| | __| |_   _ _ __ ___  _ __   ")
        print("\033[1;32m \___ \ / _` | |/ _` | | | | '_ ` _ \| '_ \  ")
        print("\033[1;32m  ___) | (_| | | (_| | |_| | | | | | | |_) | ")
        print("\033[1;32m |____/ \__, |_|\__,_|\__,_|_| |_| |_| .__/  ")
        print("\033[1;32m           |_|                       |_|     ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("apt install curl -y")
        os.system("pip install --upgrade pip; python2 -m pip install google")
        os.system(
            "curl -k -O https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py"
        )
        os.system("mkdir sqldump && chmod +x sqldump.py && mv sqldump.py sqldump")
        os.system("mv sqldump Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Xadmin #############################

    if choice_tool == "16":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m __  __            _           _        ")
        print("\033[1;32m \ \/ /   __ _  __| |_ __ ___ (_)_ __   ")
        print("\033[1;32m  \  /   / _` |/ _` | '_ ` _ \| | '_ \  ")
        print("\033[1;32m  /  \  | (_| | (_| | | | | | | | | | | ")
        print("\033[1;32m /_/\_\  \__,_|\__,_|_| |_| |_|_|_| |_| ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("git clone https://github.com/Manisso/Xadmin ")
        os.system("mv Xadmin Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### XSStrike ###########################

    if choice_tool == "17":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m __  __  ____    ____    _            _   _            ")
        print("\033[1;32m \ \/ / / ___|  / ___|  | |_   _ __  (_) | | __   ___  ")
        print("\033[1;32m  \  /  \___ \  \___ \  | __| | '__| | | | |/ /  / _ \ ")
        print("\033[1;32m  /  \   ___) |  ___) | | |_  | |    | | |   <  |  __/ ")
        print("\033[1;32m /_/\_\ |____/  |____/   \__| |_|    |_| |_|\_\  \___| ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("git clone https://github.com/s0md3v/Striker ")
        os.system("mv Striker Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Nikto ##############################

    if choice_tool == "18":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m  _   _   _   _      _            ")
        print("\033[1;32m | \ | | (_) | | __ | |_    ___   ")
        print("\033[1;32m |  \| | | | | |/ / | __|  / _ \  ")
        print("\033[1;32m | |\  | | | |   <  | |_  | (_) | ")
        print("\033[1;32m |_| \_| |_| |_|\_\  \__|  \___/  ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("git clone https://github.com/sullo/nikto ")
        os.system("mv nikto Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Hammer #############################

    if choice_tool == "19":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m  _   _                                      ")
        print("\033[1;32m | | | | __ _ _ __ ___  _ __ ___   ___ _ __  ")
        print("\033[1;32m | |_| |/ _` | '_ ` _ \| '_ ` _ \ / _ \ '__| ")
        print("\033[1;32m |  _  | (_| | | | | | | | | | | |  __/ |    ")
        print("\033[1;32m |_| |_|\__,_|_| |_| |_|_| |_| |_|\___|_|    ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("apt install python -y")
        os.system("git clone https://github.com/CruzTed/hammer")
        os.system("mv hammer Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### b0mbr3 #############################

    if choice_tool == "20":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m  _      ___            _         _____  ")
        print("\033[1;32m | |__  / _ \ _ __ ___ | |__  _ _|___ /  ")
        print("\033[1;32m | '_ \| | | | '_ ` _ \| '_ \| '__||_ \  ")
        print("\033[1;32m | |_) | |_| | | | | | | |_) | |  ___) | ")
        print("\033[1;32m |_.__/ \___/|_| |_| |_|_.__/|_| |____/  ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system(
            "apt update; apt upgrade -y; apt install git -y; apt install clang make openssl -y; pip install --upgrade pip"
        )
        os.system("git clone https://github.com/Tr3blef/b0mb3r")
        os.system("mv b0mb3r Tools")
        os.system("cd Tools && cd b0mb3r && pip3 install b0mb3r-master.zip")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Weeman #############################

    if choice_tool == "21":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m __        __                               ")
        print("\033[1;32m \ \      / /__  ___ _ __ ___   __ _ _ __   ")
        print("\033[1;32m  \ \ /\ / / _ \/ _ \ '_ ` _ \ / _` | '_ \  ")
        print("\033[1;32m   \ V  V /  __/  __/ | | | | | (_| | | | | ")
        print("\033[1;32m    \_/\_/ \___|\___|_| |_| |_|\__,_|_| |_| ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("git clone https://github.com/evait-security/weeman ")
        os.system("mv weeman Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Hash Buster ########################

    if choice_tool == "22":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m  _   _           _       ____            _             ")
        print("\033[1;32m | | | | __ _ ___| |__   | __ ) _   _ ___| |_ ___ _ __  ")
        print("\033[1;32m | |_| |/ _` / __| '_ \  |  _ \| | | / __| __/ _ \ '__| ")
        print("\033[1;32m |  _  | (_| \__ \ | | | | |_) | |_| \__ \ ||  __/ |    ")
        print("\033[1;32m |_| |_|\__,_|___/_| |_| |____/ \__,_|___/\__\___|_|    ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("git clone https://github.com/s0md3v/Hash-Buster ")
        os.system("mv Hash-Buster Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Hasher #############################

    if choice_tool == "23":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m  _   _           _                ")
        print("\033[1;32m | | | | __ _ ___| |__   ___ _ __  ")
        print("\033[1;32m | |_| |/ _` / __| '_ \ / _ \ '__| ")
        print("\033[1;32m |  _  | (_| \__ \ | | |  __/ |    ")
        print("\033[1;32m |_| |_|\__,_|___/_| |_|\___|_|    ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system(
            "pip install --upgarade pip; python2 -m pip install passlib binascii progressbar"
        )
        os.system("git clone https://github.com/CiKu370/hasher ")
        os.system("mv hasher Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if install_tool == "99":
            timeout(1)
            restart_program()
        if install_tool == "0" or install_tool == "00" or install_tool == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Fedora #############################

    if choice_tool == "24":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m  _____        _                  ")
        print("\033[1;32m |  ___|__  __| | ___  _ __ __ _  ")
        print("\033[1;32m | |_ / _ \/ _` |/ _ \| '__/ _` | ")
        print("\033[1;32m |  _|  __/ (_| | (_) | | | (_| | ")
        print("\033[1;32m |_|  \___|\__,_|\___/|_|  \__,_| ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("apt install wget -y")
        os.system(
            "wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh "
        )
        os.system("mkdir fedora")
        os.system("mv termux-fedora.sh fedora")
        os.system("mv fedora Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if choose == "99":
            timeout(1)
            restart_program()
        if choose == "0" or choose == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Wifite #############################

    elif choice_tool == "25":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m __        __  _    __   _   _           ")
        print("\033[1;32m \ \      / / (_)  / _| (_) | |_    ___  ")
        print("\033[1;32m  \ \ /\ / /  | | | |_  | | | __|  / _ \ ")
        print("\033[1;32m   \ V  V /   | | |  _| | | | |_  |  __/ ")
        print("\033[1;32m    \_/\_/    |_| |_|   |_|  \__|  \___| ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("git clone https://github.com/derv82/wifite ")
        os.system("mv wifite Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if choose == "99":
            timeout(1)
            restart_program()
        if choose == "0" or choose == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Cam-Hackers ########################

    elif choice_tool == "26":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print(
            "\033[1;32m   ____                      _   _            _                  "
        )
        print(
            "\033[1;32m  / ___|__ _ _ __ ___       | | | | __ _  ___| | _____ _ __ ___  "
        )
        print(
            "\033[1;32m | |   / _` | '_ ` _ \ _____| |_| |/ _` |/ __| |/ / _ \ '__/ __| "
        )
        print(
            "\033[1;32m | |__| (_| | | | | | |_____|  _  | (_| | (__|   <  __/ |  \__ \ "
        )
        print(
            "\033[1;32m  \____\__,_|_| |_| |_|     |_| |_|\__,_|\___|_|\_\___|_|  |___/ "
        )
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("apt install python -y ")
        os.system("git clone https://github.com/AngelSecurityTeam/Cam-Hackers")
        os.system("mv Cam-Hackers Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if choose == "99":
            timeout(1)
            restart_program()
        elif choose == "0" or choose == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Saycheese ##########################

    elif choice_tool == "27":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print("\033[1;32m  ____                   _                          ")
        print("\033[1;32m / ___|  __ _ _   _  ___| |__   ___  ___  ___  ___  ")
        print("\033[1;32m \___ \ / _` | | | |/ __| '_ \ / _ \/ _ \/ __|/ _ \ ")
        print("\033[1;32m  ___) | (_| | |_| | (__| | | |  __/  __/\__ \  __/ ")
        print("\033[1;32m |____/ \__,_|\__, |\___|_| |_|\___|\___||___/\___| ")
        print("\033[1;32m              |___/                                 ")
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("apt install python -y")
        os.system("git clone https://github.com/thelinuxchoice/saycheese ")
        os.system("mv saycheese Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if choose == "99":
            timeout(1)
            restart_program()
        elif choose == "0" or choose == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### ULtimate-Dork ######################

    elif choice_tool == "28":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print(
            "\033[1;32m  _   _ _    _   _                 _             ____             _     "
        )
        print(
            "\033[1;32m | | | | |  | |_(_)_ __ ___   __ _| |_ ___      |  _ \  ___  _ __| | __ "
        )
        print(
            "\033[1;32m | | | | |  | __| | '_ ` _ \ / _` | __/ _ \_____| | | |/ _ \| '__| |/ / "
        )
        print(
            "\033[1;32m | |_| | |__| |_| | | | | | | (_| | ||  __/_____| |_| | (_) | |  |   <  "
        )
        print(
            "\033[1;32m  \___/|_____\__|_|_| |_| |_|\__,_|\__\___|     |____/ \___/|_|  |_|\_\ "
        )
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system("apt install python -y")
        os.system("git clone https://github.com/jaxBCD/ULtimate-Dork.git")
        os.system("mv ULtimate-Dork Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if choose == "99":
            timeout(1)
            restart_program()
        elif choose == "0" or choose == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Destroyer-framework ################

    elif choice_tool == "29":
        timeout(1)
        os.system("clear")
        time.sleep(1)
        print(
            "\033[1;32m  ____            _                                     __                                             _     "
        )
        print(
            "\033[1;32m |  _ \  ___  ___| |_ _ __ ___  _   _  ___ _ __        / _|_ __ __ _ _ __ ___   _____      _____  _ __| | __ "
        )
        print(
            "\033[1;32m | | | |/ _ \/ __| __| '__/ _ \| | | |/ _ \ '__| _____| |_| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ / "
        )
        print(
            "\033[1;32m | |_| |  __/\__ \ |_| | | (_) | |_| |  __/ |   |_____|  _| | | (_| | | | | | |  __/\ V  V / (_) | |  |   <  "
        )
        print(
            "\033[1;32m |____/ \___||___/\__|_|  \___/ \__, |\___|_|         |_| |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\ "
        )
        print(
            """\033[1;33m
"""
        )
        timeout(1)
        os.system(
            "git clone https://github.com/Cesar-Hack-Gray/Destroyer-framework")
        os.system("mv Destroyer-framework Tools")
        print("|---------------------------------------------------------------|")
        print("|- Download done You can find the tool in a folder name Tools! -|")
        print("|---------------------------------------------------------------|")
        timeout(1)
        print(
            """
"""
        )
        print("\033[1;34m[99] \033[1;31mBack to main menu")
        print("")
        print("\033[1;34m[00]  \033[1;31mExit ...! ")
        print(
            """
"""
        )
        choose = input("\033[1;35mSet Install >>\033[1;36m ")
        timeout(1)
        if choose == "99":
            timeout(1)
            restart_program()
        elif choose == "0" or choose == "00":
            timeout(2)
            sys.exit()
        else:
            timeout(1)
            print("\n\033[1;31mERROR: Wrong Input")
            timeout(1)
            restart_program()

    #################### Exit..!! ###########################

    elif choice_tool == "0" or choice_tool == "00":
        print("")
        timeout(1)
        print("\033[1;31mexit....")
        print("")
        timeout(1)
        sys.exit()

    #################### Worng..! ###########################
    else:
        timeout(1)
        print("\n\033[1;31mERROR: Wrong Input")
        timeout(1)
        restart_program()
