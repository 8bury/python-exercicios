login_valido = "kezia"
senha_valida = "123"
tentativas = 0

while tentativas < 3:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    
    if login == login_valido and senha == senha_valida:
        print("Login realizado com sucesso!")
        tentativas = 4
    else:
        print("Login ou senha inválidos. Tente novamente.")
        tentativas += 1
    if tentativas == 3:
        print("Número máximo de tentativas excedido. Tente novamente mais tarde.")