a = int(input("Digite um número inteiro: "))

resultado = 1
count = a
variavel = ''

if a <= 0:
  print("Digite  um valor maior que 0!")
else:
  while count > 1:
    resultado = resultado * count
    mult = str(count)
    variavel = variavel + '*' + mult
    count  -= 1

variavel = variavel [2:]
print(f"Fatorial de 5: {a}! = {variavel}*1 = {resultado}")