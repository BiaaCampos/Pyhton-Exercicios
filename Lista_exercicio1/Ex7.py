#Exercício 7 

lista = []
result = 0

for i in range(0 , 10):
  nome = str(input(f"Digite o nome do atleta: "))
  if nome == "":
    break
  print()
  for D in range(0 , 5):
    saltos = float(input(f"Digite o {D}º salto: "))
    lista.append(saltos)
    result = result + saltos
    media = result / 5
  result = 0

  
  print()
  print(f"Atleta: {nome}") 
  print()
  print(f"Primeiro salto: {lista[0]}m")
  print(f"Segundo salto: {lista[1]}m")
  print(f"Terceiro salto: {lista[2]}m")
  print(f"Quarto salto: {lista[3]}m")
  print(f"Quinto salto: {lista[4]}m")
  print()
  print("Resultado Final:")
  print()
  print(f"Atleta: {nome}")
  print(f"Saltos: {lista}")
  print(f"Média dos Saltos: {media}m")
  print()
  lista = []
