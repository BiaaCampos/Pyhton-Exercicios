#Exercício 1 - Crie um algoritmo que leia 20 números inteiros e os guarde em uma lista. Além de guardar todas em uma única lista, separe os números pares em uma lsita "par" 
#e ímpares em uma lista "ímpar". No final mostre as listas e seus valores.

lista = []
impar = []
par = []

for i in range(1 , 10):
  numero = int(input("Digite um número inteiro: "))
  lista.append(numero)
  par_teste = numero % 2
  if par_teste == 0:
     par.append(numero)
  else: 
    impar.append(numero)

print()
print(f"Lista de todos os números: {lista}")
print()
print(f"Lista dos números ímpares: {impar}")
print(),                                                                                              
print(f"Lista dos números pares: {par}")