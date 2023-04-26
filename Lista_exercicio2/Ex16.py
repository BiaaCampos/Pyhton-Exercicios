count = 0

while(count <= 10):
  a = float(input("Valor do 1º produto:R$ "))
  b = float(input("Valor do 2º produto:R$ "))
  c = float(input("Valor do 3º produto:R$ "))
  total = a + b + c
  print("Mercadinho BigBig")
  print(f"1º Produto:R${a:.2f}")
  print(f"2º Produto:R${b:.2f}")
  print(f"3º Produto:R${c:.2f}")
  print(f"O total da compra é:R${total:.2f} ")
  dinheiro = float(input("Dinheiro:R$ "))
  troco = dinheiro - total
  print(f"Dinheiro:R${dinheiro:.2f}")
  print(f"O troco é:R${troco:.2f}")
  count = count + 1