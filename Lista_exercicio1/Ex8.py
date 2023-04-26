#Exercício 8 

lista = []
count = 1
total = 0

print("Mercadinho BigBig")
while count > 0:
  a = float(input(f"Valor do {count}º produto:R$ "))
  lista.append(a)
  if a == 0:
    for i in lista:
      total = total + i
    print(f"O total da compra foi: {total}")
    dinheiro = float(input("Dinheiro:R$ "))
    troco = dinheiro - total
    print(f"O troco é:R${troco:.2f}")
    count = 0
    total = 0
    lista = []
  if a == -1:
    count = -1
  count = count + 1