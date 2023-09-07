#progressao aritmetica
n = int(input("Digite o número de termos: "))
razao = int(input("Digite a razão: "))
a1 = int(input("Digite o primeiro termo: "))
print(a1)
for i in range(1, n+1):
    an = a1 + (i * razao)
    print(an)

