#Exercício 3 - Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.

lista = []

for i in range(5):
  numero = int(input(f"Digite um número inteiro: "))
  lista.append(numero)
  print(f"O número {numero} está na posição {i} da lista")
  print()