#=======Henrique César=======   #

import sys, os
import subprocess
from time import sleep


os.system('clear')

#funções de finalizar ação e limpart tela

def fin():
    input(' Ação finalizada')
    os.system('clear')
    python = sys.executable
    os.execl(python, python, * sys.argv)

def limpar():
    os.system('clear')
    python = sys.executable
    os.execl(python, python, * sys.argv)

verde = '\33[1;32m'
rosa = '\33[1;35m'

#interface inicial

print( verde + '''

   _   __ _____  _____ 
  | | / /|_   _||_   _|
  | |/ /   | |    | |  
  |    \   | |    | |  
  | |\  \ _| |_   | |  
  \_| \_/ \___/   \_/  
                       
                       
  _   _   ___   _____  _   __ _____ ______ 
 | | | | / _ \ /  __ \| | / /|  ___|| ___ |
 | |_| |/ /_\ \| /  \/| |/ / | |__  | |_/ /
 |  _  ||  _  || |    |    \ |  __| |    / 
 | | | || | | || \__/\| |\  \| |___ | |\ \ 
 \_| |_/\_| |_/ \____/\_| \_/\____/ \_| \_|

''')

print( rosa + '''HENRIQUE CÉSAR, 2021 V 2.0 \nTwitter: @MRCATFAT
KIT DE HACKING PARA TERMUX''' + verde)


print('''
 [ 1 ] --> Ataque de senha
 [ 2 ] --> Análise de vulnerabilidade
 [ 3 ] --> Wordlist
 [ 4 ] --> Pishing 
 [ 5 ] --> Ferramentas
 [ 6 ] --> DoS
 [ 0 ] --> Sair
''')

menu = int (input(' Selecione uma opção: '))

if menu == 0:
    (exit())

if menu == 1:
    print('''

 [ 1 ] --> facebook brute
 [ 2 ] --> Hash Buster
 [ 3 ] --> Black hydra
 [ 4 ] --> Instahack
 [ 5 ] --> ASU
 [ 6 ] --> Aircrack
 [ 7 ] --> 1337Hash
 [ 0 ] --> voltar

''')

    atq = int (input(' Selecione uma opção: '))

    if atq == 0:
        limpar()

    elif atq == 1:
        subprocess.call(["git clone https://github.com/Cesar-Hacker/facebook-brute && mv facebook-brute /data/data/com.termux/files/home" , "-la"], shell=True)
        fin()

    elif atq == 2:
        subprocess.call(["git clone https://github.com/s0md3v/Hash-Buster && mv Hash-Buster /data/data/com.termux/files/home","-la"],shell=True)
        fin()

    elif atq == 3:
        subprocess.call(["git clone https://github.com/Gameye98/Black-Hydra && mv Black-Hydra /data/data/com.termux/files/home ","-la"],shell=True)
        fin()

    elif atq == 4:
        subprocess.call(["git clone https://github.com/fuck3erboy/instahack && mv instahack /data/data/com.termux/files/home ","-la"],shell=True)
        fin()

    elif atq == 5:
        subprocess.call(["git clone https://github.com/ASU-LAB/asu-v5 && mv asu-v5 /data/data/com.termux/files/home","-la"],shell=True)
        fin()

    elif atq == 6:
        subprocess.call(["git clone https://github.com/aircrack-ng/aircrack-ng && mv aircrack-ng /data/data/com.termux/files/home","-la"],shell=True)
        fin()

    elif atq == 7:
        subprocess.call(["git clone https://github.com/u0pattern/1337Hash && mv 1337Hash /data/data/com.termux/files/home","-la"],shell=True)
        fin()

    else:
        print('erro')
        sleep(5)
        limpar()

if menu == 2:
    print(''' [ 1 ] --> Nmap
 [ 2 ] --> Routersploit
 [ 3 ] --> Sqlscan
 [ 4 ] --> Sqlmap
 [ 5 ] --> Red Hawk
 [ 6 ] --> XAttacker
 [ 7 ] --> Metasploit
 [ 0 ] --> Voltar

        ''')

    anl = int (input(' Selecione uma opção: '))

    if anl == 0:
        limpar()
    
    elif anl == 1:
        subprocess.call(["git clone https://github.com/nmap/nmap && mv nmap /data/data/com.termux/files/home","-la"],shell=True)
        fin()

    elif anl == 2:
        subprocess.call(["git clone https://github.com/threat9/routersploit && mv routersploit /data/data/com.termux/files/home","-la"],shell=True)
        fin()
    elif anl == 3:
        subprocess.call(["git clone https://github.com/Pure-L0G1C/SQL-scanner && mv SQL-scanner /data/data/com.termux/files/home","-la"],shell=True)
        fin()
    elif anl == 4:
        subprocess.call(["git clone https://github.com/sqlmapproject/sqlmap && mv sqlmap /data/data/com.termux/files/home","-la"],shell=True)
        fin()

    elif anl == 5:
        subprocess.call(["git clone https://github.com/Tuhinshubhra/RED_HAWK&& mv RED_HAWK /data/data/com.termux/files/home ","-la"],shell=True)
        fin()

    elif anl == 6:
        subprocess.call(["git clone https://github.com/Moham3dRiahi/XAttacker && mv XAttacker /data/data/com.termux/files/home ","-la"],shell=True)
        fin()

    elif anl == 7:
        subprocess.call(["pkg install metasploit ","-la"],shell=True)
        fin()

    else:
        print('erro')
        sleep(5)
        limpar()

if menu == 3:
    print(''' [ 1 ] --> Indonesian Wordlist
 [ 2 ] --> BRdumps
 [ 3 ] --> Dadoware
 [ 4 ] --> probable wordlist
 [ 5 ] --> Crunch
 [ 6 ] --> Seclists
 [ 0 ] --> Voltar
 ''')
 
    wdl = int (input(' Selecione uma opção: '))

    if wdl == 0:
        limpar()

    elif wdl == 1:
        subprocess.call(["git clone https://github.com/geovedi/indonesian-wordlist && mv indonesian-wordlist /data/data/com.termux/files/home","-la"],shell=True)
        fin()

    elif wdl == 2:
        subprocess.call(["git clonehttps://github.com/BRDumps/wordlists  && mv BRDumps /data/data/com.termux/files/home","-la"],shell=True)
        fin()

    elif wdl == 3:
        subprocess.call(["git clone https://github.com/thoughtworks/dadoware && mv dadoware /data/data/com.termux/files/home" ,"-la"],shell=True)
        fin()

    elif wdl == 4:
        subprocess.call(["git clone https://github.com/berzerk0/Probable-Wordlists && mv Probable-Wordlists /data/data/com.termux/files/home" ,"-la"],shell=True)
        fin()

    elif wdl == 5:
        subprocess.call(["git clone https://github.com/crunchsec/crunch  && mv crunch /data/data/com.termux/files/home" ,"-la"],shell=True)
        fin()
    
    elif wdl == 6:
        subprocess.call(["git clone https://github.com/danielmiessler/SecLists && mv SecLists /data/data/com.termux/files/home"])

    else:
        print('erro')
        limpar()

if menu == 4:
    print(''' [ 1 ] --> SocialSploit
 [ 2 ] --> SocialFish
 [ 3 ] --> FishingTool
 [ 4 ] --> Zphisher
 [ 0 ] --> Voltar 
    ''')

    ps = int (input(' Selecione uma opção:  '))

    if ps == 0:
        limpar()

    elif ps == 1:
        subprocess.call(["git clone https://github.com/Cesar-Hack-Gray/SocialSploit && mv.SocialSploit /data/data/com.termux/files/home" ,"-la"],shell=True)
        fin()

    elif ps == 2:
        subprocess.call(["git clone https://github.com/UndeadSec/SocialFish && mv SocialFish /data/data/com.termux/files/home","-la"],shell=True)
        fin()

    elif ps == 3:
        subprocess.call(["git clone https://github.com/Vairous7x/V7x-Fishing && mv V7x-Fishing /data/data/com.termux/files/home " ,"-la"],shell=True)
        fin()

    elif ps == 4:
        subprocess.call(["git clone https://github.com/htr-tech/zphisher && mv zphisher /data/data/com.termux/files/home " ,"-la"],shell=True)
        fin()

    else:
        print('erro')
        sleep(5)
        limpar()

if menu == 5:
    print(''' [ 1 ] --> Ngrok
 [ 2 ] --> Xampp
 [ 0 ] --> Voltar
 ''')
    ot = int (input(' Selecione uma opção: '))

    if ot == 0:
        limpar()

    elif ot == 1:
        token = str(input(" DIGITE SEU AUTHTOKEN: "))
        subprocess.call(["git clone https://github.com/PSecurity/ps.ngrok && mv ps.ngrok /data/data/com.termux/files/home && cd && cd ps.ngrok && chmod +x * && ./ngrok authtoken " + token, "-la"], shell = True)
        fin()

    elif ot == 2:
        subprocess.call(["git clone https://github.com/xampp-phoenix/xampp && mv xampp /data/data/com.termux/files/home" ,"-la"],shell=True)
        fin()

    else:
        print('erro')
        sleep(5)
        limpar()

if menu == 6:
    print(''' [ 1 ] --> Xerxes
 [ 2 ] --> hammer
 [ 3 ] --> Doser
 [ 0 ] --> Voltar
 ''')

    ddos = int (input(' Selecione uma opção: '))

    if ddos == 0:
        limpar()

    elif ddos == 1:
        subprocess.call(["git clone https://github.com/XCHADXFAQ77X/XERXES && mv XERXES /data/data/com.termux/files/home  " ,"-la"],shell=True)  
        fin()

    elif ddos == 2:
        subprocess.call(["git clone https://github.com/cyweb/hammer && mv hammer /data/data/com.termux/files/home  " ,"-la"],shell=True)           
        fin()

    elif ddos == 3:
        subprocess.call(["git clone https://github.com/Quitten/doser.py  && mv doser.py /data/data/com.termux/files/home " ,"-la"],shell=True)  
        fin()

else:
    print('erro')
    sleep(5)
    limpar()
