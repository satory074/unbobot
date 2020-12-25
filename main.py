import platform
import subprocess
import sys
import chardet

def run_powershell(cmd:str):
    print(f"Powershell > {' '.join(cmd)}")
    res = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Print error
    if s := res.stdout.readline:
        for l in iter(res.stdout.readline, b''):
            e: str = chardet.detect(l)['encoding']
            print(l.rstrip().decode(e) if e else '')

def notify(text:list[str], logo:str='./data/satori.ico'):
    if platform.system() == 'Linux': # WSL2
        # Format -Text
        s: str = text.pop(0)
        for i in range(len(text)):
            s += f',"{text[i]}"'

        # Notify
        cmd: list[str] =  ['powershell.exe', '-command', 'New-BurntToastNotification', '-Text', s, '-AppLogo', logo]
        run_powershell(cmd)

text: str = ['Notify', 'text1', 'text2']
notify(text)