#===========HENRIQUE==========#

#Importações
import sys
import os
import subprocess

#Limpar a tela do terminal
inicio=subprocess.call(["clear","-x"],shell=True)
verde="\033[1;32m"
#Título
print(verde+"  _  __ _  _____"+"\n"+" / |/ // \/__ __\ "+"\n"+" |   / | |  / \ "+"\n"+" |   \ | |  | |"+"\n"+" \_|\_ \\_/  \_/ "+"\n"+"  _     ____  ____  _  __ _____ ____"+"\n"+" / \ /|/  _ \/   _\/ |/ //  __//  __\ "+"\n"+" | |_||| / \||  /  |   / |  \  |  \/|"+"\n"+" | | ||| |-|||  \__|   \ |  /_ |    / "+"\n"+" \_/ \|\_/ \|\ ____/\_|\_\\____\ \_/\_\ ")

print("\n"+"   HENRIQUE CÉSAR,2020  v 1.3"+"\n")
print("\n"+"  KIT DE HACKING INICIANTE PARA TERMUX"+"\n")

#Tela inicial
print(" [1]-Ataque de senha"+"\n"+" [2]-Análise de vulnerabilidade"+"\n"+" [3]-Wordlist"+"\n"+" [4]-Pishing"+"\n"+" [5]-Outros"+"\n"+" [6]-Entre em contato"+"\n"+" [0]-Sair")

#Variável para redirecionar usuário
op=int(input("\n"+" SELECIONE UMA OPÇÃO: "))

#Tela de download de ataque de senha
if op==1:
    print("\n"+" [1]-Facebook Brute"+"\n"+" [2]-Hash buster"+"\n"+" [3]-Black-Hydra"+"\n"+" [4]-Instahack"+"\n"+" [5]-ASU"+"\n"+" [6]-Aircrack"+"\n"+" [7]-1337Hash"+"\n"+" [0]-Voltar")
    
    op2=int(input("\n"+" SELECIONE UMA OPÇÃO: "))
    
#Downloads feitos de acordo com a opção selecionada    

    if op2==1:
        facebookbrute=subprocess.call(["git clone https://github.com/Cesar-Hacker/facebook-brute && mv facebook-brute /data/data/com.termux/files/home" , "-la"], shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op2==2:
        hashbuster=subprocess.call(["git clone https://github.com/s0md3v/Hash-Buster && mv Hash-Buster /data/data/com.termux/files/home","-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op2==3:
        Hydra=subprocess.call(["git clone https://github.com/Gameye98/Black-Hydra && mv Black-Hydra /data/data/com.termux/files/home ","-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op2==4:
        insta=subprocess.call(["git clone https://github.com/fuck3erboy/instahack && mv instahack /data/data/com.termux/files/home ","-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)

    if op2==5:
        asu=subprocess.call(["git clone https://github.com/ASU-LAB/asu-v5 && mv asu-v5 /data/data/com.termux/files/home","-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op2==6:
        air=subprocess.call(["git clone https://github.com/aircrack-ng/aircrack-ng && mv aircrack-ng /data/data/com.termux/files/home","-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op2==7:
        h=subprocess.call(["git clone https://github.com/u0pattern/1337Hash && mv 1337Hash /data/data/com.termux/files/home","-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
#Voltar        
    if op2==0:
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
#Caso o usuário digite algo inválido        

    else:
        print(" OPÇÃO INVÁLIDA")  
        input(" REINICIANDO...")
        python = sys.executable
        os.execl(python, python, * sys.argv)

#Tela de download de análise de vulnerabilidade
if op==2:
    print("\n"+" [1]-Nmap"+"\n"+" [2]-Routersploit"+"\n"+" [3]-Sqlscan"+"\n"+" [4]-Sqlmap"+"\n"+" [5]-Red hawk"+"\n"+" [6]-XAttacker"+"\n"+" [7]-Metasploit"+"\n"+" [0]-Voltar")
    
    op3=int(input("\n"+" SELECIONE UMA OPÇÃO: "))
    
#Downloads feitos de acordo com a opção selecionada 
   
    if op3==1:
        nmap=subprocess.call(["git clone https://github.com/nmap/nmap && mv nmap /data/data/com.termux/files/home","-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op3==2:
         router=subprocess.call(["git clone https://github.com/threat9/routersploit && mv routersploit /data/data/com.termux/files/home","-la"],shell=True)
         input("FERRAMENTA INSTALADA")
         python = sys.executable
         os.execl(python, python, * sys.argv)
        
    if op3==3:
         sqlscan=subprocess.call(["git clone https://github.com/Pure-L0G1C/SQL-scanner && mv SQL-scanner /data/data/com.termux/files/home","-la"],shell=True)
         input("FERRAMENTA INSTALADA")
         python = sys.executable
         os.execl(python, python, * sys.argv)
        
    if op3==4:
        sqlmap=subprocess.call(["git clone https://github.com/sqlmapproject/sqlmap && mv sqlmap /data/data/com.termux/files/home","-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op3==5:
        redh=subprocess.call(["git clone https://github.com/Tuhinshubhra/RED_HAWK&& mv RED_HAWK /data/data/com.termux/files/home ","-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op3==6:
        xat=subprocess.call(["git clone https://github.com/Moham3dRiahi/XAttacker && mv XAttacker /data/data/com.termux/files/home ","-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op3==7:
        meta=subprocess.call(["pkg install metasploit ","-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
#Caso o usuário queira voltar   
    if op3==0:
        input("\n"+" REINICIANDO...")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
#Caso o usuário sigite algo inválido        
    else:
        input(" OPÇÃO INVÁLIDA"+"\n"+" REINICIANDO...")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
#Tela de wordlists        
if op==3:
    print("\n"+" [1]-Indonesian-wordlist"+"\n"+" [2]-Brdumps"+"\n"+" [3]-Banco de dados de senha"+"\n"+" [4]-Dadoware"+"\n"+" [5]-probable wordlist"+"\n"+" [6]-Crunch"+"\n"+" [0]-Voltar")
    
    op4=int(input("\n"+" SELECIONE UMA OPÇÃO: "))
#Downloads    
    if op4==1:
        iw=subprocess.call(["git clone https://github.com/geovedi/indonesian-wordlist && mv indonesian-wordlist /data/data/com.termux/files/home","-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op4==2:
        br=subprocess.call(["git clonehttps://github.com/BRDumps/wordlists  && mv BRDumps /data/data/com.termux/files/home","-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op4==3:
        bd=subprocess.call(["git clone https://github.com/danieldonda/wordlist && mv wordlist /data/data/com.termux/files/home " ,"-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op4==4:
        dw=subprocess.call(["git clone https://github.com/thoughtworks/dadoware && mv dadoware /data/data/com.termux/files/home" ,"-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
       
    if op4==5:
       pw=subprocess.call(["git clone https://github.com/berzerk0/Probable-Wordlists && mv Probable-Wordlists /data/data/com.termux/files/home" ,"-la"],shell=True)
       input("FERRAMENTA INSTALADA")
       python = sys.executable
       os.execl(python, python, * sys.argv)
    if op4==6:
        cr=subprocess.call(["git clone https://github.com/crunchsec/crunch  && mv crunch /data/data/com.termux/files/home" ,"-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
            
    if op4==0:
        python = sys.executable
        os.execl(python, python, * sys.argv)

#tela de pishing        
if op==4:
    print("\n"+" [1]-SocialSploit"+"\n"+" [2]-SocialFish"+"\n"+" [3]-FishingTool"+"\n"+" [4]-Zphisher"+"\n"+" [0]-Voltar")  
      
    op5=int(input(" SELECIONE UMA OPÇÃO: "))
    
    if op5==1:
        ss=subprocess.call(["git clone https://github.com/Cesar-Hack-Gray/SocialSploit && mv.SocialSploit /data/data/com.termux/files/home" ,"-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op5==2:
        sf=subprocess.call(["git clone https://github.com/UndeadSec/SocialFish && mv SocialFish /data/data/com.termux/files/home","-la"],shell=True)
        
    if op5==3:
        ft=subprocess.call(["git clone https://github.com/Vairous7x/V7x-Fishing && mv V7x-Fishing /data/data/com.termux/files/home " ,"-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op5==4:
       zp=subprocess.call(["git clone https://github.com/htr-tech/zphisher && mv zphisher /data/data/com.termux/files/home " ,"-la"],shell=True)
       input("FERRAMENTA INSTALADA")
       python = sys.executable
       os.execl(python, python, * sys.argv)
        
    if op5==0:
        input("VOLTANDO...")
        python = sys.executable
        os.execl(python, python, * sys.argv)      
        
    else:
        input(" OPÇÃO INVÁLIDA")
        python = sys.executable
        os.execl(python, python, * sys.argv)   
           
#tela das ferramentas
if op==5:
    print("\n"+" [1]-Ngrok"+"\n"+" [2]-Kali"+"\n"+" [3]-Xampp"+"\n"+" [0]-Voltar")            
    op6=int(input("\n"+" SELECIONE UMA OPÇÃO: "))
#Downloads
    if op6==1:
        token=str(input(" DIGITE SEU AUTHTOKEN: "))
        ft=subprocess.call(["git clone https://github.com/PSecurity/ps.ngrok && mv ps.ngrok /data/data/com.termux/files/home && cd && cd ps.ngrok && chmod +x * && ./ngrok authtoken"+"token" ,"-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op6==2:
        kali=subprocess.call(["pkg install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh && bash kali.sh && mv kali.sh /data/data/com.termux/files/home", "-la"], shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op6==3:
        xampp=subprocess.call(["git clone https://github.com/xampp-phoenix/xampp && mv xampp /data/data/com.termux/files/home  " ,"-la"],shell=True)
        input("FERRAMENTA INSTALADA")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    if op6==0:
        input("VOLTANDO...")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
#Caso o usuário digite algo inválido    
    else:
        input("OPÇÃO INVÁLIDA ")
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
#tela de contato
if op==6:
    print("\n"+" [Twitter]-->@MRCATFAT"+"\n"+" [Gmail]-->teste1395271@gmail.com"+"\n"+" [facebook]--> https://www.facebook.com/cesarhenriqueabc")
    input("")
    python = sys.executable
    os.execl(python, python, * sys.argv)

#Opção de sair        
if op==0:
    input("Saindo...")
    (exit())
    
else:
    print(" OPÇÃO INVÁLIDA")        
    python = sys.executable
    os.execl(python, python, * sys.argv)
  
