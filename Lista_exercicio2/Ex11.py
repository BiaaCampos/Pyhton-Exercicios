count = 1
qtde = 0
while(count <= 100):
    mult = 1
    while (mult <= count):
        if count % mult == 0:
            qtde += 1
        mult += 1
    if qtde == 2:
      if (count%2) == 0:
       print(f"{count}: Par e Primo")
      else:
       print(f"{count}: Ímpar e Primo")
    elif (count%2) == 0:
      print(f"{count}: Par")
    else:
      print(f"{count}: Ímpar")
    qtde = 0
    count = count + 1