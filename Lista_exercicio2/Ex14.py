salario = float(input("Informe o salário: R$"))

if salario < 800:
  porcentagem = 20
  aumento = salario * 0.20
elif salario >= 800 and salario < 1300:
  porcentagem = 15
  aumento = salario * 0.15
elif salario >= 1300 and salario < 2500:
  porcentagem = 10
  aumento = salario * 0.10
else:
  porcentagem = 5
  aumento = salario * 0.05

print(f"O salário antigo: R${salario:.0f}")
print(f"A porcentagem aplicada foi de: {porcentagem}%")
print(f"O aumento será de: R${aumento:.0f}")
print(f"O novo salário é: R${salario + aumento:.0f}")