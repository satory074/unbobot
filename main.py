import platform
import subprocess
import sys

def notify(text:list[str], logo:str='./data/satori.ico'):
    if platform.system() == 'Linux': # WSL2
        # Format -Text
        s: str = text.pop(0)
        for i in range(len(text)):
            s += f',"{text[i]}"'

        # Notify
        cmd: list[str] =  ['powershell.exe', '-command', 'New-BurntToastNotification', '-Text', s, '-AppLogo', logo]
        res = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

        # Print error
        [print(l.rstrip().decode("utf-8")) for l in iter(res.stdout.readline, b'')]

text:str = ['Notify', 'text1', 'text2']
notify(text)