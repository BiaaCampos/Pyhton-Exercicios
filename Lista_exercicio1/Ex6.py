#Exercício 6 - Faça um algoritmo que receba a temperatura média de cada mês do ano e
#armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as
#temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso:
#1 – Janeiro, 2 – Fevereiro, . . . ).

lista1 = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
lista2 = []
lista3 = []
media = 0

for a in range(0, len(lista1)):
  temp = float(input(f"Digite a temperatura do mês de {lista1[a]}: "))
  lista2.append(temp)
for n in lista2:
  media = media + n
mediaTotal = media / 12

print()
print(f"Meses: {lista1}")
print(f"Temperaturas: {lista2}")
print(f"A média anual das temperaturas são: {mediaTotal}")
print()

for i in range(0, len(lista2)): 
  if lista2[i] > mediaTotal:
    lista3.append(lista2[i])
    print(f'O mês de {lista1[i]} teve a temperatura maior que a média anual')