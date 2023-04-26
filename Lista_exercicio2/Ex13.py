nome_aluno = input("Digite o nome do aluno: ")
prova = float(input("Digite a 1º nota: "))
trabalho = float(input("Digite a 2º nota: "))
atividade = float(input("Digite a 3º nota: "))
participacao = float(input("Digite a 4º nota: "))
media = prova + trabalho + atividade + participacao / 4

if media >= 7:
  print("Aluno está Aprovado")
elif media >= 5 and media < 7:
   print("Aluno está em Exame")
else:
  print("Aluno está Reprovado")