a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a < b and a < c and b < c:
  maior = c
  menor = a
elif a < b and b > c and c > a:
  maior = b
  menor = a
elif a > b and a < c and b < c: 
  maior = c
  menor = b
elif a < b and b > c and c < b:
  maior = b
  menor = c
elif a > b and c > b and b < a:
  maior = a
  menor = b
elif a > b and b > c and c < a:
  maior = a
  menor = c

print(f"O menor valor é {menor} e o maior valor é {maior}")