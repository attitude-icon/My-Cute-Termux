import os
import sys
import random
import time
import colorsys
import pip


def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def banner():
    clr()
    logo = """
        __  ___             _____     __
       /  |/  /_  __       / ___/_ __/ /____
      / /|_/ / / / /      / /__/ // / __/ -_)
     / /  / / /_/ /_____  \___/\_,_/\__/\__/
    /_/  /_/\__, /|_   _|__ _ _ _ _ _  _ __  __ 
           /____/   | |/ -_) '_| V | |_||\ \/ /
            V1.0    |_|\___|_| |_|_|\___//_/\_\   


    Coded by : https://github.com/HACK3RY2J/
    Youtube  : https://youtube.com/c/PandaHackers/
    """
    print(logo)


def requirmnts():
    os.system('pkg install git -y && pkg install python -y && pkg install toilet -y && pkg install figlet -y')


def load3():
    Intro = """
    Welcome to Termux!

    Wiki:            https://wiki.termux.com
    Community forum: https://termux.com/community
    IRC channel:     #termux on freenode
    Gitter chat:     https://gitter.im/termux/termux
    Mailing list:    termux+subscribe@groups.io

    Search packages:   pkg search <query>
    Install a package: pkg install <package>
    Upgrade packages:  pkg upgrade
    Learn more:        pkg help
    """
    print("Restoring Your Termux To Original..")
    os.system('cd .. && cd .. && cd usr && cd bin && cat login && cd .. && cd etc && cat > motd ')
    os.system(print(Intro))
    print("Exit And Termux And Re-Open\n\tSee Your Old Termux")


def LScrees():
    requirmnts()
    clr()
    banner()
    print(
        "This Tool Is Designed For Termux Only.\n\tUsing In Other Terminal Or Linux May Cause Error.\n\nYou Are About To Customize Your Termux.")
    input("\tPress Enter To Continue >->")
    clr()
    banner()
    op = input("What You Want To Do..\n1.Customize\n2.Restore\n>>>")
    while True:
        if op == "1":
            txt = input("Enter Your Text To Be Displayed on Login Screen\n>>>")
            print(txt)
            qwe = input("What Do You Want At Startup\n1.Figlet Your Text..\n2.Border Your Figltet Name..\n>>>")
            while True:
                if qwe == "1":
                    asd1 = os.system('figlet ' + txt)
                    print(asd1)
                    zx = input("Do You Want To Continue[y/n]: ")
                    while True:
                        if zx == "y" or "Y" or "Yes" or "YES":
                            print("Installing Requirements...")
                            os.system(
                                'cd .. && cd .. && cd usr && cd bin && cat login && cd .. && cd etc && cat > motd ')
                            os.system(print(os.system('figlet ' + txt)))
                            print("Exit And Termux And Re-Open\n\tSee The magic")
                        elif zx == "n" or "N" or "no" or "NO":
                            print("Task Has Been Succesfully Aborted.\n\n\n1.Try Again.\n2.Exit")
                            az = input("Enter Your Choice: ")
                            while True:
                                if az == "1":
                                    LScrees()
                                elif az == "2":
                                    banner()
                                    print("Thanks For Using My Cute Termux\n\tWe Hope To See You Again")
                                    exit()
                                else:
                                    print("Invalid Input Detected")
                                    exit()
                        else:
                            print("Invalid Input Detected")
                            exit()
                elif qwe == "2":
                    asd2 = os.system('toilet -f mono12 -F border ' + txt)
                    print("Your Startup Screen Will Look Similar To This.")
                    print(asd2)
                    zx = input("Do You Want To Continue[y/n]: ")
                    while True:
                        if zx == "y" or "Y" or "Yes" or "YES":
                            print("Installing Requirements...")
                            os.system(print(os.system('toilet -f mono12 -F border ' + txt)))
                            print("Exit And Termux And Re-Open\n\tSee The magic")
                        elif zx == "n" or "N" or "no" or "NO":
                            print("Task Has Been Succesfully Aborted.\n\n\n1.Try Again.\n2.Exit")
                            az = input("Enter Your Choice: ")
                            while True:
                                if az == "1":
                                    exit()
                                    print("Restarting The Program")
                                    time.sleep(2)
                                    os.system('python cusm.py')
                                elif az == "2":
                                    banner()
                                    print("Thanks For Using My Cute Termux\n\tWe Hope To See You Again")
                                    exit()
                                else:
                                    print("Invalid Input Detected")
                                    exit()
                        else:
                            print("Invalid Input Detected")
                            exit()
                else:
                    print("Invalid Input Detected")
                    exit()
        if op == "2":
            load3()
        else:
            print("Invalid Input Detected")
            exit()


LScrees()

