import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, r'C:\Users\Note\Desktop\Projeto V&V\project\BiscoitoChines')
from gettingAdvice import bridge

# Oi!
# Esta é uma aplicação de Biscoitinho da Sorte que acessa uma API que entrega
# pequenos conselhos em formato "slip" (ou fichinhas), que usa o unnitest.mock 
# como ferramenta de teste (100% experimental para mim kkk).
# Requisitos para rodar: python3
# caso algo dê errado na instalação do python3 e a biblioteca requests não vier
# automaticamente, o comando
# > pip install requests
# deve resolver.

# > python application.py
# ^ comando para rodar a aplicação na linha de comando, na pasta BiscoitoChines 
# aberta.

loop = True


while loop:
    params = {'params':{'id':'', 'query':''}}

    option = input("1 para receber um conselho aleatório" + 
    "\n 2 para receber um conselho com o seu número da sorte" +
    "\n 3 para pedir um conselho com uma palavra \n")

    print(option)
    if option == '2':
        dataAlter = input("Digite seu número da sorte\n")
        params['params']['id'] = dataAlter
    elif option == '3':
        dataAlter = input("Digite uma palavra (em inglês ^^)\n")
        params['params']['query'] = dataAlter

    results = bridge(params=params)

    print(results)

