#Exercício 2 - Crie um algoritmo que leia 4 notas de 10 alunos, calcule e guarde em uma lista a média de cada aluno. No final mostre quantos 
#alunos tiveram a média maior ou igual a 7.

lista = []
media = 0
qntd = 0

for i in range(1, 11):
  for a in range(1, 5):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    media = media + nota
  media_final = media / 4
  lista.append(media_final)
  media = 0
  print()

for n in lista:
  if n >= 7:
    qntd += 1

print(lista)
print()
print(f"{qntd} alunos tiveram a média igual ou maior que 7.")