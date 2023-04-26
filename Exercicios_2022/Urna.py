
# Trabalho Urna
# Curso: Análise e Desenvolvimento de Sistemas
# Diciplina: Construção de Algoritmos
# Semestre: 1

#Urna 
print("Candidatos para as eleições 2022")
print()
print("1. Vincent Vega")
print("2. Jules Winnfield")
print("3. Marsellus Wallace")     
print() 

eleitores = int(input("Informe a quantidade de eleitores: "))

count = 1
tentativa = 1
candidato1 = 0
candidato2 = 0
candidato3 = 0
qnd_eleitores = 0

while(count <= eleitores):
  voto = int(input("Qual seu voto: "))
  print(count)
  if voto == 1 or voto == 2 or voto == 3:
    validacao = 1
    qnd_eleitores += 1
    print("Voto concluído")
    if voto == 1:
      candidato1 = candidato1 + 1
    if voto == 2:
      candidato2 = candidato2 + 1
    if voto == 3:
      candidato3 = candidato3 + 1
  else:
    print("Voto inválido!")
    while(tentativa < 5):
      voto = int(input("Qual seu voto: "))
      if voto == 1 or voto == 2 or voto == 3:
        print("Voto concluído") 
        if voto == 1:
          candidato1 = candidato1 + 1
        if voto == 2:
          candidato2 = candidato2 + 1
        if voto == 3:
          candidato3 = candidato3 + 1
        tentativa = 5
        validacao = 1
      else:
        print("Voto inválido!")
        tentativa = tentativa + 1
  count = count + 1

  validacao = 0

if qnd_eleitores != 0:
  porcentagem1 = (candidato1 / eleitores) * 100
  porcentagem2 = (candidato2 / eleitores) * 100
  porcentagem3 = (candidato3 / eleitores) * 100

else:
  porcentagem1 = 0
  porcentagem2 = 0
  porcentagem3 = 0

print(f"Candidato 1: com {candidato1} votos e com a porcentagem de: {porcentagem1}%")
print(f"Candidato 2: com {candidato2} votos e com a porcentagem de: {porcentagem2}%")
print(f"Candidato 3: com {candidato3} votos e com a porcentagem de: {porcentagem3}%")

if porcentagem1 > porcentagem2 and porcentagem1 > porcentagem3:
  print("O vencedor foi: Vincente Vega")
  candidato2 = 0
  candidato3 = 0
if porcentagem2 > porcentagem1 and porcentagem2 > porcentagem3:
  print("O vencedor foi: Jules Winnfield")
  candidato1 = 0
  candidato3 = 0
if porcentagem3 > porcentagem1 and porcentagem3 > porcentagem2:
  print("O vencedor foi: Marcellus Wallace")
  candidato1 = 0
  candidato2 = 0
  
if porcentagem1 == porcentagem2 == porcentagem3:
  print(f"Empate entre Vincente Vega com {porcentagem1}%, Jules Winnfield com {porcentagem2}% e Marcellus Wallace com {porcentagem3}%")
elif porcentagem1 == porcentagem2 and porcentagem1 > porcentagem3:
  print(f"Empate entre Vincente Vega com {porcentagem1}% e Jules Winnfield com {porcentagem2}%")
elif porcentagem1 == porcentagem3 and porcentagem3 > porcentagem2:
  print(f"Empate entre Vincente Vega com {porcentagem1}% e Marcellus Wallace com {porcentagem3}%")
elif porcentagem2 == porcentagem3 and porcentagem2 > porcentagem1:
  print(f"Empate entre Jules Winnfield com {porcentagem2}% e Marcellus Wallace com {porcentagem3}%")