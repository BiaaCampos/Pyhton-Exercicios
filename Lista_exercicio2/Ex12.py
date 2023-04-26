operacao = input("Digite a operação desejada (soma +, sub -, div /, mult *): ")
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

if operacao == "soma" or "+":
  resultado = int(numero_1) + int(numero_2)
elif operacao == "sub" or "-":
  resultado = int(numero_1) - int(numero_2)
elif operacao == "div" or "/":
  resultado = int(numero_1) / int(numero_2)
elif operacao == "mult" or "*":
  resultado = int(numero_1) * int(numero_2)

print(f"O resultado da operaçao é: {resultado}")