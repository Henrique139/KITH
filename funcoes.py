#Arquivo com as duas funções

def fin():
    input(' Ação finalizada')
    os.system('clear')
    python = sys.executable
    os.execl(python, python, * sys.argv)

def limpar():
    os.system('clear')
    python = sys.executable
    os.execl(python, python, * sys.argv)
