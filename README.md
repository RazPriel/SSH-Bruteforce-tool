# SSH-Bruteforce-tool
A simple Python script demonstrating how an SSH brute-force attack works.  

## ✨ Features

- Attempts SSH login with a list of passwords (wordlist).  
- Uses multithreading for faster attempts.  
- Shows which passwords succeed or fail.  

## 🛠️ Requirements

- Python 3.x  
- [paramiko](https://pypi.org/project/paramiko/)  

Install dependencies:

```bash
pip install paramiko
```

## 🚀 Usage (authorized environments only)

1. Clone this repository:

```bash
git clone https://github.com/RazPriel/SSH-Bruteforce-tool.git SSHBruteForce
cd SSHBruteForce
```

2. Prepare a wordlist file containing passwords to try (e.g. `passwords.txt`).

3. Run the script:

```bash
python3 ssh_bruteforce.py
```

4. Enter the required details when prompted:

```
[+] Target address: 192.168.1.10
[+] SSH Username: testuser
[+] Passwords file path: passwords.txt
```

5. The script will start attempting logins and show output such as:

```
[ *** Starting SSH Bruteforce on: 192.168.1.10 With account: testuser *** ]
[-] Incorrect Login: password123
[-] Incorrect Login: admin
[+] Found Password: secret123, For Account: testuser
```

