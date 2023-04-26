#Entrada
valor = int(input('Digite um valor inteiro: '))

#Processamento
valor = str(valor)
valor = valor[::-1]
qnd = len(valor) - 1
count = 0
aux = qnd
valorfinal = 0
print()

#Base 10
print('Base 10')
while count <= aux:
  exp = 10 ** qnd
  resultado = int(valor[qnd]) * exp
  valorfinal = valorfinal + resultado 
  print(f'{valor[qnd]} x {exp} = {resultado}')
  qnd -= 1
  count += 1

print(f'Resultado = {valorfinal}')
count = 0
qnd = len(valor) - 1
valorfinal = 0
print()

#Base 8
print('Base 8')
while count <= aux:
  exp = 8 ** qnd
  resultado = int(valor[qnd]) * exp
  valorfinal = valorfinal + resultado
  print(f'{valor[qnd]} x {exp} = {resultado}')
  qnd -= 1
  count += 1

print(f'Resultado = {valorfinal}')
resto = 0
base8 = valorfinal
octal = ''

while base8 >= 1:
  resto = base8 % 8
  base8 = base8 // 8
  octal = octal + str(resto)

print(f'O número {valorfinal} em octal é {octal[::-1]}')

count = 0
qnd = len(valor) - 1
valorfinal = 0
print()

#Base 2
print('Base 2')
while count <= aux:
  exp = 2 ** qnd
  resultado = int(valor[qnd]) * exp
  valorfinal = valorfinal + resultado 
  print(f'{valor[qnd]} x {exp} = {resultado}')
  qnd -= 1
  count += 1
print(f'Resultado = {valorfinal}')
resto = 0
base2 = valorfinal
binario = ''

while base2 >= 1:
  resto = base2 % 2
  base2 = base2 // 2
  binario = binario + str(resto)

print(f'O número {valorfinal} em binário é {binario[::-1]}')