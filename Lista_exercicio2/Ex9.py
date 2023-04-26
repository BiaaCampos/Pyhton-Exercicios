horario = input("Informe o horário: ")

if horario >= '00:00' and horario <= '12:59':
  print("Manhã")
elif horario >= '13:00' and horario <= '18:59':
  print("Tarde")
else:
  print("Noite")