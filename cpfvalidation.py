import re,validarcpf,validarnome
from datetime import datetime

'''cpf = input("Digite seu cpf: ")
if(validarcpf.validar_cpf(cpf)):
    print("Cpf Correto!")
else:
    print("Cpf Incorreto!")'''

'''idade = int(input("Enre com sua idade: "))
if(idade>0 and idade<120):
    print(f"idade cadastrada: {idade}")
else:
    print("Idade inválida!")'''

agora = datetime.now()
print(agora)
data = agora.date()
print(f"Data atual: {data}")
hora = agora.time()
print(f"hora atual: {hora}")
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
print(f"Data formatada: {data_formatada}")


    