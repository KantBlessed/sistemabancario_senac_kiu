def validarCelular():
    validar = input("Você deseja validar seu celular? ").lower.strip()
    if validar == "sim" or validar == "s":
        print("celular validad com sucesso")
    else:
        print("autorização bloqueada! ")