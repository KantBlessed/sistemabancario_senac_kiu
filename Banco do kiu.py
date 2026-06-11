import re,validarcpf,validarnome

cadastro = {}

print("$$$$$$$ Bem-vindo ao Kiu Bank $$$$$$$\n")

score: 2000
saldo: None
senha: None

def mostrar_menu():

    print("1 - Realizar Cadastro")
    print("2 - Realizar Login")
    print("3 - Suporte")
    print("4 - Sair")

while True:
    mostrar_menu()

    escolha = int(input(f"\nQual opção deseja realizar? "))
    
    if (escolha == 1):
        
        nome = input("Digite seu nome: ").strip()
        if len(nome) >= 3:
           cadastro["nome"] = nome
           
        cpf = input("Digite seu cpf: ").strip()
        if len(nome) >= 10:
               cadastro["cpf"] = nome
        
        print(f"\nUsuário {nome} cadastrado com sucesso!")
        print("Banco de dados atualizado:")
        
    elif (escolha == 2):
        
        nome = input("Digite seu nome: ")
        if(validarnome(nome)):
            print("Nome Correto!")
        else:
            print("Nome Incorreto! Tente novamente!")
            continue
        
        cpf = input("Digite seu cpf: ")
        if(validarcpf.validar_cpf(cpf)):
            print("Cpf Correto!")
        else:
            print("Cpf Incorreto! Tente novamente!")
    elif (escolha == 3):
        input("Nos envie sua duvida ou sua reclamação, que em breve responderemos! ")
        print("Mensagem enviada com sucesso!")
        continue
        
    else:
        print("Ocorreu um erro ao validar suas informações.")
        break
