a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))


aux = 0

if a != b and a != c and b != c :

    if a < b and a < c and b < c :
      a = a  

    if a < b and a < c and b > c: 
     aux = b
     b = c
     c = aux
    elif a > b and a < c and b < c:
      aux = a
      a = b
      b = aux
    elif a < b and c < b and a > c:
      aux1 = a
      aux2 = b
      a = c
      c = aux2
      b = aux1
    elif a > b and a > c and b < c:
      aux1 = a
      aux2 = c
      a = b
      b = aux2
      c = aux1
    elif c < b and c < a and b < a:
      aux = a 
      a = c
      c = aux

    print (c , b , a)