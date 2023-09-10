valorPago = valorTotalConta = preco = 0

resposta = input("Deseja algo?")

while resposta!= "n":
    codigo = input("Código: ")
    qtd = int(input("Quantidade: "))
    if codigo == "100":
        preco = 1.20
    elif codigo == "101":
        preco = 1.30
    elif codigo == "102":
        preco = 1.50
    elif codigo == "103":
        preco = 1.20
    elif codigo == "104":
        preco = 1.30
    elif codigo == "105":
        preco = 1
    valorPago = qtd * preco
    valorTotalConta += valorPago 
    print(codigo, qtd, valorPago)
    
    resposta = input("Deseja algo?")
print("Valor Total = R$", valorTotalConta)