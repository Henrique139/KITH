import subprocess
import os
from time import sleep 

def inst():
    os.system('clear')
    sleep(2)


os.system('clear')

print('=== Instalando algumas coisas que podem ser úteis ===')


print('=== Atualizando Lista de pacotes ===')

subprocess.call(["apt update", "-la"], shell=True)

subprocess.call(["apt upgrade", "-la"], shell=True)

subprocess.call(["pkg update", "-la"], shell=True)

subprocess.call(["pkg upgrade", "-la"], shell=True)

inst()

print('=== Instalando editor de texto  NANO ===')
subprocess.call(["apt install nano", "-la"], shell=True)

inst()

print('=== instalando wget ===')
subprocess.call(["apt install wget", "-la"], shell=True)

inst()

print('=== Instalando PHP ===')
subprocess.call(["apt install php", "-la"], shell=True)

inst()

print('=== Instalando coreutils ===')
subprocess.call(["pkg install coreutils", "-la"], shell=True)

inst()

print('===  Instalando Curl ===')
subprocess.call(["apt install curl", "-la"], shell=True)

inst()

print('===  Iniciando o KITH ===')
sleep(3)
subprocess.call(["python kith.py", "-la"],shell=True)



