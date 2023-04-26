#Exercício 4 - Crie um algoritmo que leia 10 números, guarde-os em uma lista “ORDEM”. Depois
#gere uma segunda lista “REVERSA” que deve conter os elementos em ordem inversa a original.

listaOrdem = []
listaReverso = [] 

for i in range(0 , 10):
  numero = int(input(f"Digite o {i}º número inteiro: "))
  listaOrdem.append(numero)
for a in range(9, -1 , -1):
  listaReverso.append(listaOrdem[a])

print()
print(f"A lista Ordem: {listaOrdem}")
print(f"A lista Reversa: {listaReverso}")