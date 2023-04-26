#Exercício 5 - Faça um algoritmo que leia dois vetores com 10 elementos cada. Gere um terceiro
#vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos
#dois outros vetores.

lista1 = []
lista2 = []
lista3 = []

print("Lista 1")
for a in range(10):
  numero1 = int(input(f"Digite o {a}º elemento: "))
  lista1.append(numero1)

print("Lista 2")
for i in range(10):
  numero2 = int(input(f"Digite o {i}º elemento: "))
  lista2.append(numero2)
for n in range(10):
  lista3.append(lista1[n])
  lista3.append(lista2[n])

print()
print(f"Primeira lista: {lista1}")
print(f"Segunda lista: {lista2}")
print(f"Lista intercalada é: {lista3}")