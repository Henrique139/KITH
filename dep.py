import subprocess

input("instalando algumas depêndencias")

comando1=subprocess.call(["apt install git", "-la"], shell=True)
comando1=subprocess.call(["apt update", "-la"], shell=True)

comando2=subprocess.call(["apt upgrade", "-la"], shell=True)

comando3=subprocess.call(["apt install nano", "-la"], shell=True)

comando4=subprocess.call(["apt install wget", "-la"], shell=True)

comando5=subprocess.call(["apt install python", "-la"], shell=True)

comando6=subprocess.call(["apt install php", "-la"], shell=True)
