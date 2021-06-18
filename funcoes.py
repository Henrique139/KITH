#Arquivo com as duas funções
#usado para separar do script principal

def fin():
    input(' Ação finalizada')
    os.system('clear')
    python = sys.executable
    os.execl(python, python, * sys.argv)

def limpar():
    os.system('clear')
    python = sys.executable
    os.execl(python, python, * sys.argv)


