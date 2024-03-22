import os

def restart_laptop():
    if os.name == 'nt':  # for Windows
        os.system('shutdown /r /t 1')
    elif os.name == 'posix':  # for Linux/MacOS
        os.system('sudo reboot')

restart_laptop()
