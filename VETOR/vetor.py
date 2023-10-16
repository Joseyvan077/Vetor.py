
Q = [0] * 20

for i in range(20):
    numero = float(input(f"Digite o valor positivo {i + 1}: "))
    
    while numero < 0:
        numero = float(input("Digite um número positivo: "))
    
    Q[i] = numero

maior_elemento = Q[0]
posicao_maior = 0

for i in range(1, 20):
    if Q[i] > maior_elemento:
        maior_elemento = Q[i]
        posicao_maior = i


menor_elemento = Q[0]
posicao_menor = 0

for i in range(1, 20):
    if Q[i] < menor_elemento:
        menor_elemento = Q[i]
        posicao_menor = i


print(f"O maior elemento de Q é {maior_elemento} e ele ocupa a posição {posicao_maior}.")
print(f"O menor elemento de Q é {menor_elemento} e ele ocupa a posição {posicao_menor}.")