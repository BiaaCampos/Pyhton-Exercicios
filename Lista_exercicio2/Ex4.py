numero = int(input("Digite um número: "))


if numero > 0 and numero <= 99:
    print("Dezena")
elif numero >= 100 and numero <= 999:
    print("Centena")
else: 
    print("Milênio")