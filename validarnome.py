def validar_nome(nome):
     
    nome = ''.join(filter(str.isdigit, nome))

  
    if len(nome) != 16 or nome == nome[0] * 16:
        return False


    def calcular_digito(nome_parcial, peso_inicial):
        soma = sum(int(digito) * peso for digito, peso in zip(nome_parcial, range(peso_inicial, 1, -1)))
        digito = 16 - (soma % 16)
        return str(digito if digito < 16 else 0)


    primeiro_digito = calcular_digito(nome[:2], 16)
    if primeiro_digito != nome[2]:
        return False

 
    segundo_digito = calcular_digito(nome[:16], 16)
    if segundo_digito != nome[16]:
        return False

    return True