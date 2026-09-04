#!/usr/bin/env python3

import sys
import argparse
import os
import time
import http.client
import subprocess
import re
import urllib.request
import urllib.parse
import urllib.error
import json
# 'telnetlib' removed because it is deprecated and unused in Python 3.12+
import glob
import random
import queue
import threading
import base64
from getpass import getpass
from sys import argv
from platform import system
from xml.dom import minidom
from optparse import OptionParser
from time import sleep

os.system('clear')

directories = ['/uploads/', '/upload/', '/files/', '/resume/', '/resumes/', '/documents/', '/docs/', '/pictures/', '/file/', '/Upload/', '/Uploads/', '/Resume/', '/Resume/', '/UsersFiles/', '/Usersiles/', '/usersFiles/', '/Users_Files/', '/UploadedFiles/',
               '/Uploaded_Files/', '/uploadedfiles/', '/uploadedFiles/', '/hpage/', '/admin/upload/', '/admin/uploads/', '/admin/resume/', '/admin/resumes/', '/admin/pictures/', '/pics/', '/photos/', '/Alumni_Photos/', '/alumni_photos/', '/AlumniPhotos/', '/users/']
shells = ['wso.php', 'shell.php', 'an.php', 'hacker.php', 'lol.php', 'up.php', 'cp.php', 'upload.php',
          'sh.php', 'pk.php', 'mad.php', 'x00x.php', 'worm.php', '1337worm.php', 'config.php', 'x.php', 'haha.php']
upload = []
yes = set(['yes', 'y', 'ye', 'Y'])
no = set(['no', 'n'])

# Notice 'r' added before triple quotes to make it a raw string
YUVRAJlogo = r"""
 /$$$$$$$                  /$$       /$$$$$$$                          
| $$__  $$                | $$      | $$__  $$                         
| $$  \ $$  /$$$$$$   /$$$$$$$      | $$  \ $$ /$$$$$$   /$$$$$$       
| $$$$$$$/ /$$__  $$ /$$__  $$      | $$$$$$$//$$__  $$ /$$__  $$      
| $$__  $$| $$$$$$$$| $$  | $$      | $$____/| $$  \__/| $$  \ $$      
| $$  \ $$| $$_____/| $$  | $$      | $$     | $$      | $$  | $$      
| $$  | $$|  $$$$$$$|  $$$$$$$      | $$     | $$      |  $$$$$$/      
|__/  |__/ \_______/ \_______/      |__/     |__/       \______/       
                                                                       
                                                                       
                                       
        ~ Advanced Tool By Yuvraj | Github: real-tungsten | Instagram: @0fficial.yuvraj ~
        ~⚠️ Note: Strictly created for educational purposes and programming research.~
"""

def menu():
    print(YUVRAJlogo + """\033[1m
 [!] This Tool Must Run As ROOT [!]
\033[0m
   {1}--Information Gathering
   {2}--Password Attacks
   {3}--Wireless Testing
   {4}--Exploitation Tools
   {5}--Sniffing & Spoofing
   {6}--Web Hacking
   {7}--Private Web Hacking
   {8}--Post Exploitation
   {0}--Install The Tool Updates
   {99}-Exit
 """)
    choice = input("yuvraj~# ")
    os.system('clear')
    if choice == "1":
        info()
    elif choice == "2":
        passwd()
    elif choice == "3":
        wire()
    elif choice == "4":
        exp()
    elif choice == "5":
        snif()
    elif choice == "6":
        webhack()
    elif choice == "7":
        dzz()
    elif choice == "8":
        postexp()
    elif choice == "0":
        updatetool()
    elif choice == "99":
        clearScr()
        sys.exit()
    else:
        menu()

def updatetool():
    print("This Tool is Only Available for Linux and Similar Systems.")
    choiceupdate = input("Continue Y / N: ").lower()
    if choiceupdate in yes:
        os.system("git clone https://github.com/technicaldada/hackerpro.git")
        os.system("cd hackerpro && sudo bash ./update.sh")
    else:
        menu()

def doork():
    print("doork is a open-source passive vulnerability auditor tool.")
    doorkchice = input("Continue Y / N: ").lower()
    if doorkchice in yes:
        os.system("pip3 install beautifulsoup4 requests")
        os.system("git clone https://github.com/AeonDave/doork")
        clearScr()
        doorkt = input("Target : ")
        os.system(f"cd doork && python3 doork.py -t {doorkt} -o log.log")
    else:
        info()

def postexp():
    clearScr()
    print(YUVRAJlogo)
    print("   {1}--Shell Checker")
    print("   {2}--POET")
    print("   {3}--Phishing Framework \n")
    print("   {99}-Return to main menu \n\n ")
    choice11 = input("yuvraj~# ")
    os.system('clear')
    if choice11 == "1":
        sitechecker()
    elif choice11 == "2":
        poet()
    elif choice11 == "3":
        weeman()
    elif choice11 == "99":
        menu()
    else:
        postexp()

def scanusers():
    site = input('Enter a website : ')
    try:
        users = site
        users = users.replace('http://www.', '').replace('http://', '').replace('.', '').replace('-', '').replace('/', '')
        while len(users) > 2:
            print(users)
            resp = urllib.request.urlopen(site + '/cgi-sys/guestbook.cgi?user=%s' % users).read().decode('utf-8')
            if 'invalid username' not in resp.lower():
                print("\tFound -> %s" % users)
            users = users[:-1]
    except Exception as e:
        print("Error:", e)
    info()

def brutex():
    clearScr()
    print("Automatically brute force all services running on a target.")
    os.system("git clone https://github.com/1N3/BruteX.git")
    clearScr()
    brutexchoice = input("Select a Target : ")
    os.system(f"cd BruteX && chmod 777 brutex && ./brutex {brutexchoice}")

def arachni():
    print("Arachni is a feature-full, modular, high-performance Ruby framework.")
    cara = input("Install And Run ? Y / N : ").lower()
    clearScr()
    if cara in yes:        
        os.system("git clone git://github.com/Arachni/arachni.git")
        os.system("cd arachni && sudo gem install bundler && bundle install --without prof && rake install")
    print("exemple : http://www.target.com/")
    tara = input("Select a target to scan : ")
    clearScr()
    os.system(f"cd arachni/bin && chmod 777 arachni && ./arachni {tara}")

def XSStrike():
    clearScr()
    print("XSStrike is a python script designed to detect and exploit XSS vulnerabilites.")
    os.system("sudo rm -rf XSStrike")
    os.system("git clone https://github.com/UltimateHackers/XSStrike.git && cd XSStrike && pip3 install -r requirements.txt && clear && python3 xsstrike")

def crips():
    clearScr()
    os.system("git clone https://github.com/Manisso/Crips.git")
    os.system("cd Crips && sudo bash ./update.sh")
    os.system("python3 crips.py")

def weeman():
    print("HTTP server for phishing in python.")
    choicewee = input("Install Weeman ? Y / N : ").lower()
    if choicewee in yes:
        os.system("git clone https://github.com/samyoyo/weeman.git && cd weeman && python3 weeman.py")
    else:
        menu()

def h2ip():
    host = input("Select A Host : ")
    try:
        ips = socket.gethostbyname(host)
        print(ips)
    except Exception as e:
        print("Could not resolve host:", e)
    input("Press Enter to continue...")
    info()

def ports():
    clearScr()
    target = input('Select a Target IP : ')
    os.system(f"nmap -O -Pn {target}")

def atscan():
    print("Do You To Install ATSCAN ?")
    choiceshell = input("Y/N: ").lower()
    if choiceshell in yes:
        os.system("sudo rm -rf ATSCAN")
        os.system("git clone https://github.com/AlisamTechnology/ATSCAN.git && cd ATSCAN && perl atscan.pl")
    else:
        menu()

def commix():
    print("Automated All-in-One OS Command Injection and Exploitation Tool.")
    choicecmx = input("Continue: y/n :").lower()
    if choicecmx in yes:
        os.system("git clone https://github.com/stasinopoulos/commix.git commix")
        os.system("cd commix && python3 commix.py")
    else:
        info()

def pixiewps():
    print("Pixiewps is a tool used to bruteforce offline the WPS pin.")
    choicewps = input("Continue ? Y/N : ").lower()
    if choicewps in yes:
        os.system("git clone https://github.com/wiire/pixiewps.git")
        os.system("cd pixiewps && make && sudo make install")
    else:
        menu()

def webhack():
    print(YUVRAJlogo)
    print("   {1}--Inurlbr")
    print("   {2}--Wordpress & Joomla Scanner")
    print("   {3}--File Upload Checker")
    print("   {4}--Shell and Directory Finder")
    print("   {5}--BruteX - Automatically brute force all services")
    print("   {6}--Arachni - Web Application Security Scanner")
    print("   {99}-Back To Main Menu \n")
    choiceweb = input("yuvraj~# ")
    if choiceweb == "1":
        inurl()
    elif choiceweb == "2":
        clearScr()
    elif choiceweb == "3":
        clearScr()
    elif choiceweb == "4":
        shelltarget()
    elif choiceweb == "5":
        brutex()
    elif choiceweb == "6":
        arachni()
    elif choiceweb == "99":
        menu()
    else:
        webhack()

def inurl():
    print("Inurlbr not fully configured in this script. Coming soon.")
    input("Press enter...")
    menu()

def nmap():
    choice7 = input("Install Nmap? Y / N : ").lower()
    if choice7 in yes:
        os.system("git clone https://github.com/nmap/nmap.git")
        os.system("cd nmap && ./configure && make && sudo make install")
    else:
        info()

def sqlmap():
    print("usage : python3 sqlmap.py -h")
    choice8 = input("Continue: y/n :").lower()
    if choice8 in yes:
        os.system("git clone https://github.com/sqlmapproject/sqlmap.git sqlmap-dev")
    else:
        info()

def grabuploadedlink(url):
    try:
        for dir_path in directories:
            currentcode = urllib.request.urlopen(url + dir_path).getcode()
            if currentcode in [200, 403]:
                print(f"-------------------------")
                print(f"  [ + ] Found Directory : {url}{dir_path} [ + ]")
                print(f"-------------------------")
                upload.append(url + dir_path)
    except:
        pass

def grabshell(url):
    try:
        for upl in upload:
            for shell in shells:
                currentcode = urllib.request.urlopen(upl + shell).getcode()
                if currentcode == 200:
                    print("-------------------------")
                    print(f"  [ ! ] Found Shell : {upl}{shell} [ ! ]")
                    print("-------------------------")
    except:
        pass

def shelltarget():
    print("exemple : http://target.com")
    line = input("target : ").rstrip()
    grabuploadedlink(line)
    grabshell(line)

def poet():
    print("POET is a simple POst-Exploitation Tool.")
    choicepoet = input("y / n :").lower()
    if choicepoet in yes:
        os.system("git clone https://github.com/mossberg/poet.git")
        os.system("python3 poet/server.py")
    else:
        postexp()

def cupp():
    print("cupp is a password list generator ")
    choicecupp = input("Continue: y/n : ").lower()
    if choicecupp in yes:
        os.system("git clone https://github.com/Mebus/cupp.git")
        print("file downloaded successfully")
    else:
        passwd()

def reaver():
    print("Reaver has been designed to be a robust and practical attack against WPS.")
    creaver = input("y / n :").lower()
    if creaver in yes:
        os.system("sudo apt-get -y install build-essential libpcap-dev sqlite3 libsqlite3-dev aircrack-ng pixiewps")
        os.system("git clone https://github.com/t6x/reaver-wps-fork-t6x.git")
        os.system("cd reaver-wps-fork-t6x/src/ && ./configure && make")
    else:
        wire()

def clearScr():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')

def info():
    clearScr()
    print(YUVRAJlogo)
    print("  {1}--Nmap ")
    print("  {2}--Port Scanning")
    print("  {3}--Host To IP")
    print("  {4}--XSStrike")
    print("  {5}--Dork - Google Dorks")
    print("  {6}--Scan A server's Users  ")
    print("  {7}--Crips\n  ")
    print("  {99}-Back To Main Menu \n\n")
    choice2 = input("yuvraj~# ")
    if choice2 == "1":
        nmap()
    elif choice2 == "2":
        ports()
    elif choice2 == "3":
        h2ip()
    elif choice2 == "4":
        XSStrike()
    elif choice2 == "5":
        doork()
    elif choice2 == "6":
        scanusers()
    elif choice2 == "7":
        crips()
    elif choice2 == "99":
        menu()
    else:
        info()

def passwd():
    clearScr()
    print(YUVRAJlogo)
    print("   {1}--Cupp ")
    print("   {99}-Back To Main Menu \n")
    choice3 = input("yuvraj~# ")
    if choice3 == "1":
        cupp()
    elif choice3 == "99":
        menu()
    else:
        passwd()

def bluepot():
    print("You need to have at least 1 bluetooth receiver.")
    choice = input("Continue ? Y / N : ").lower()
    if choice in yes:
        os.system("wget https://github.com/andrewmichaelsmith/bluepot/raw/master/bin/bluepot-0.1.tar.gz && tar xfz bluepot-0.1.tar.gz && sudo java -jar bluepot/BluePot-0.1.jar")
    else:
        wire()

def fluxion():
    print("Fluxion is a wifi key cracker using evil twin attack.")
    choice = input("Continue ? Y / N : ").lower()
    if choice in yes:
        os.system("git clone https://github.com/thehackingsage/Fluxion.git") 
        os.system("cd Fluxion/install && sudo chmod +x install.sh && sudo ./install.sh")
        os.system("cd Fluxion && sudo chmod +x fluxion.sh && sudo ./fluxion.sh")
    else:
        wire()

def wire():
    clearScr()
    print(YUVRAJlogo)
    print("   {1}--Reaver ")
    print("   {2}--Pixiewps")
    print("   {3}--Bluetooth Honeypot GUI Framework")
    print("   {4}--Fluxion\n")
    print("   {99}-Back To The Main Menu \n\n")
    choice4 = input("yuvraj~# ")
    if choice4 == "1":
        reaver()
    elif choice4 == "2":
        pixiewps()
    elif choice4 == "3":
        bluepot()
    elif choice4 == "4":
        fluxion()
    elif choice4 == "99":
        menu()
    else:
        wire()

def exp():
    clearScr()
    print(YUVRAJlogo)
    print("   {1}--ATSCAN")
    print("   {2}--sqlmap")
    print("   {3}--commix")
    print("   {99}-Go Back To Main Menu \n\n")
    choice5 = input("yuvraj~# ")
    if choice5 == "1":
        atscan()
    elif choice5 == "2":
        sqlmap()
    elif choice5 == "3":
        commix()
    elif choice5 == "99":
        menu()
    else:
        exp()

def snif():
    clearScr()
    print(YUVRAJlogo)
    print("   {1}--PyPisher")
    print("   {99}-Back To Main Menu \n\n")
    choice6 = input("yuvraj~# ")
    if choice6 == "1":
        print("Functionality not added yet.")
        input("Press enter...")
        snif()
    elif choice6 == "99":
        menu()
    else:
        snif()

def dzz():
    print("Private Web Hacking - Coming Soon")
    input("Press Enter...")
    menu()

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\n[!] Exiting Program. Bye Yuvraj!\n")
        sys.exit()