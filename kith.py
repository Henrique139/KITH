#=======Henrique César=======   #

import sys, os
import subprocess
from time import sleep
from funcoes import fin, limpar


os.system('clear')


#cores
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

print( rosa + '''HENRIQUE CÉSAR, 2021 V 3.0 \nTwitter: @MRCATFAT
KIT DE HACKING PARA TERMUX''' + verde)


print('''
 [ 1 ] --> Ataque de senha
 [ 2 ] --> Análise de vulnerabilidade
 [ 3 ] --> Wordlist
 [ 4 ] --> Pishing 
 [ 5 ] --> Ferramentas
 [ 6 ] --> Coleta de informações
 [ 0 ] --> Sair
''')

menu = int (input(' Selecione uma opção: '))

if menu == 0:
    (exit())

#Menu ataque de senha

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

#Menu análise de vulnerabilidade

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

#Menu wordlists

if menu == 3:
    print(''' [ 1 ] --> Indonesian Wordlist
 [ 2 ] --> BRdumps
 [ 3 ] --> Dadoware
 [ 4 ] --> probable wordlist
 [ 5 ] --> Crunch
 [ 6 ] --> Seclists
 [ 7 ] --> wpa2-wordlists
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
        subprocess.call(["git clone https://github.com/danielmiessler/SecLists && mv SecLists /data/data/com.termux/files/home", "-la"], shell=True)
        fin()

    elif wdl == 7:
        subprocess.call(["git clone https://github.com/kennyn510/wpa2-wordlists && mv wpa2-wordlists /data/data/com.termux/files/home", "-la"], shell=True)
        fin()

    else:
        print('erro')
        limpar()

#Menu phishing

if menu == 4:
    print(''' [ 1 ] --> SocialSploit
 [ 2 ] --> SocialFish
 [ 3 ] --> FishingTool
 [ 4 ] --> Zphisher
 [ 5 ] --> AdvPhishing
 [ 6 ] --> BlackPhish
 [ 7 ] --> SniperPhish
 [ 0 ] --> Voltar 
    ''')

    ps = int (input(' Selecione uma opção:  '))

    if ps == 0:
        limpar()

    elif ps == 1:
        subprocess.call(["git clone https://github.com/Cesar-Hack-Gray/SocialSploit && mv SocialSploit /data/data/com.termux/files/home" ,"-la"],shell=True)
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

    elif ps == 5:
        subprocess.call(["git clone https://github.com/Ignitetch/AdvPhishing && mv AdvPhishing /data/data/com.termux/files/home " ,"-la"],shell=True)
        fin()

    elif ps == 6:
        subprocess.call(["git clone https://github.com/iinc0gnit0/BlackPhish && mv BlackPhish /data/data/com.termux/files/home " ,"-la"],shell=True)
        fin()

    elif ps == 7:
        subprocess.call(["git clone https://github.com/GemGeorge/SniperPhish && mv SniperPhish /data/data/com.termux/files/home " ,"-la"],shell=True)
        fin()

    else:
        print('erro')
        sleep(5)
        limpar()

#Menu ferramentas

if menu == 5:
    print(''' [ 1 ] --> Ngrok
 [ 2 ] --> Xampp
 [ 0 ] --> Voltar
 ''')
    fe = int (input(' Selecione uma opção: '))

    if fe == 0:
        limpar()

    elif fe == 1:
        token = str(input(" DIGITE SEU AUTHTOKEN: "))
        subprocess.call(["git clone https://github.com/PSecurity/ps.ngrok && mv ps.ngrok /data/data/com.termux/files/home && cd && cd ps.ngrok && chmod +x * && ./ngrok authtoken " + token, "-la"], shell = True)
        fin()

    elif fe == 2:
        subprocess.call(["git clone https://github.com/xampp-phoenix/xampp && mv xampp /data/data/com.termux/files/home" ,"-la"],shell=True)
        fin()

    else:
        print('erro')
        sleep(5)
        limpar()

#Menu coleta de informações

if menu == 6:
    print(''' [ 1 ] --> Infoga
 [ 2 ] --> GasMask
 [ 3 ] --> AppMetaData
 [ 4 ] --> ANDROPHSY
 [ 0 ] --> Sair
    ''')

    co = int (input(' Selecione uma opção: '))

    if co == 1:
        subprocess.call(["git clone https://github.com/m4ll0k/Infoga && mv Infoga /data/data/com.termux/files/home" ,"-la"],shell=True)
        fin()

    elif co == 2:
        subprocess.call(["git clone https://github.com/twelvesec/gasmask && mv gasmask /data/data/com.termux/files/home" ,"-la"],shell=True)
        fin()

    elif co == 3:
        subprocess.call(["git clone https://github.com/Microsoft/app-metadata && mv app-metadata /data/data/com.termux/files/home" ,"-la"],shell=True)
        fin()
    
    elif co == 4:
        subprocess.call(["git clone https://github.com/scorelab/ANDROPHSY && mv ANDROPHSY /data/data/com.termux/files/home" ,"-la"],shell=True)
        fin()

    elif co == 0:
        limpar()

    else:
        print('erro')
        sleep(5)
        limpar()


else:
    print('erro')
    sleep(5)
    limpar()
