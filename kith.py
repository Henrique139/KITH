import sys
import os
import subprocess

inicio=subprocess.call(["clear","-x"])

print("___________________________________________________________ ")
print("  | /   •   ___         |   |      __      ___    | /   ") 
print("  《    |    |          |---|     /__\     |      《   ")
print("  | \   |    |          |   |    /    \    |__    | \             ")
print("___________________________________________________________  ")

print("Por HENRIQUE CÉSAR  V:1.0")

print("\n"+"  KIT DE HACKING INICIANTE PARA TERMUX"+"\n")
print("\n"+"Algumas ferramentas podem ser de nível avançado"+"\n")


print(" [1]-Ataque de senha")
print(" [2]-Análise de vulnerabilidade")
print(" [3]-Wordlist")
print(" [4]-Pishing")
print(" [0]-Sair")

op=int(input("\n"+" SELECIONE UMA OPÇÃO: "))

if op==1:
    print("\n"+" [1]-Facebook Brute"+"\n"+" [2]-Hash buster"+"\n"+" [3]-Black-Hydra"+"\n"+" [4]-Instahack"+"\n"+" [0]-Voltar")
    op2=int(input("\n"+" SELECIONE UMA OPÇÃO: "))
    if op2==1:
        facebookbrute=subprocess.call(["git clone https://github.com/Cesar-Hacker/facebook-brute", "-la"], shell=True)
    if op2==2:
        hashbuster=subprocess.call(["git clone https://github.com/s0md3v/Hash-Buster","-la"],shell=True)
    if op2==3:
        Hydra=subprocess.call(["git clone https://github.com/Gameye98/Black-Hydra","-la"],shell=True)
    if op2==4:
        insta=subprocess.call(["git clone https://github.com/fuck3erboy/instahack","-la"],shell=True)
    if op2==0:
        python = sys.executable
        os.execl(python, python, * sys.argv)
    else:
        print(" OPÇÃO INVÁLIDA")  
        input(" REINICIANDO...")
        python = sys.executable
        os.execl(python, python, * sys.argv)
if op==2:
    print("\n"+" [1]-Nmap"+"\n"+" [2]-Routersploit"+"\n"+" [3]-Sqlscan"+"\n"+" [4]-Sqlmap"+"\n"+" [5]-Red hawk"+"\n"+" [6]-XAttacker"+"\n"+" [0]-Voltar")
    op3=int(input("\n"+" SELECIONE UMA OPÇÃO: "))
    if op3==1:
        nmap=subprocess.call(["git clone https://github.com/nmap/nmap","-la"],shell=True)
    if op3==2:
         router=subprocess.call(["git clone https://github.com/threat9/routersploit","-la"],shell=True)
    if op3==3:
         sqlscan=subprocess.call(["git clone https://github.com/Pure-L0G1C/SQL-scanner","-la"],shell=True)
    if op3==4:
        sqlmap=subprocess.call(["git clone https://github.com/sqlmapproject/sqlmap","-la"],shell=True)
    if op3==5:
        redh=subprocess.call(["git clone https://github.com/Tuhinshubhra/RED_HAWK","-la"],shell=True)
    if op3==6:
        xat=subprocess.call(["git clone https://github.com/Moham3dRiahi/XAttacker","-la"],shell=True)
    if op3==0:
        input("\n"+" REINICIANDO...")
        python = sys.executable
        os.execl(python, python, * sys.argv)
    else:
        input(" OPÇÃO INVÁLIDA"+"\n"+" REINICIANDO...")
        python = sys.executable
        os.execl(python, python, * sys.argv)
if op==3:
    print("\n"+" [1]-Indonesian-wordlist"+"\n"+" [2]-Brdumps"+"\n"+" [3]-Banco de dados de senha"+"\n"+" [4]-Dadoware"+"\n"+" [5]-probable wordlist"+"\n"+" [0]-Voltar")
    op4=int(input("\n"+" SELECIONE UMA OPÇÃO: "))
    if op4==1:
        iw=subprocess.call(["git clone https://github.com/geovedi/indonesian-wordlist","-la"],shell=True)
    if op4==2:
        br=subprocess.call(["git clonehttps://github.com/BRDumps/wordlists" ,"-la"],shell=True)
    if op4==3:
        bd=subprocess.call(["git clone https://github.com/danieldonda/wordlist" ,"-la"],shell=True)
    if op4==4:
        dw=subprocess.call(["git clone https://github.com/thoughtworks/dadoware" ,"-la"],shell=True)
    if op4==5:
       pw=subprocess.call(["git clone https://github.com/berzerk0/Probable-Wordlists" ,"-la"],shell=True)
    if op4==0:
        python = sys.executable
        os.execl(python, python, * sys.argv)
if op==4:
    print("\n"+" [1]-SocialSploit"+"\n"+" [2]-SocialFish"+"\n"+" [3]-FishingTool")    
    op5=int(input(" SELECIONE UMA OPÇÃO: "))
    if op5==1:
        ss=subprocess.call(["git clone https://github.com/Cesar-Hack-Gray/SocialSploit" ,"-la"],shell=True)
    if op5==2:
        sf=subprocess.call(["git clone https://github.com/UndeadSec/SocialFis","-la"],shell=True)
    if op5==3:
        subprocess.call(["git clone https://github.com/Vairous7x/V7x-Fishing" ,"-la"],shell=True)
if op==0:
    (exit())
else:
    print(" OPÇÃO INVÁLIDA")        
    python = sys.executable
    os.execl(python, python, * sys.argv)
  
