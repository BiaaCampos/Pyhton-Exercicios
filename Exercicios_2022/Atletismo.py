#Atletismo/Salto em Distância
#pedir qtd de atletas, pedir qtd de saltos por atleta
#para cada atleta: pedir nome, pedir cada salto em metros, mostrar melhor e o pior saltos,
#mostrar a média de saltos do atleta
#No final mostrar o nome/média do atleta com a maior média de saltos

qdte_atletas = int(input("Qual a quantidade de atletas: "))
qdte_saltos = int(input("Qual a quantidade de saltos por atletas: "))
print()
result = 0
media1 = 0

for i in range(0 , qdte_atletas):
  nome = str(input(f"Digite o nome do atleta {i}: "))
  print()

  for D in range(0 , qdte_saltos):
    saltos = float(input(f"Digite o salto em metros {D}: "))
    result = result + saltos
    if D == 0:
      melhor_salto = saltos
      pior_salto = saltos

    if melhor_salto < saltos:
      melhor_salto = saltos

    if pior_salto > saltos:
      pior_salto = saltos
    

  media = result / qdte_saltos
  if media1 < media:
    media1 = media
    nome_variavel = nome

  print()
  print(f"Melhor salto: {melhor_salto}m")
  print(f"Pior salto: {pior_salto}m")
  print(f"média: {media:.2f}m")
  result = 0
  print()

print(f"Atleta {nome_variavel} com a maior média de {media1:.2f}m")