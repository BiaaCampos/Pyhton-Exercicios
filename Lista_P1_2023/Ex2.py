# 2 - Desafio: Fila de atendimento em uma loja: Imagine que você trabalhe em uma loja que recebe muitos clientes diariamente e precisa organizar uma fila de atendimento. 
# Utilizando a estrutura de dados lista como uma fila, crie um programa em Python que simule o atendimento aos clientes e apresente as seguintes funcionalidades: 
# a. Adicionar um cliente à fila: o programa deve permitir a entrada do nome do cliente e adicioná-lo ao final da fila de atendimento.
#  b. Atender um cliente: o programa deve retirar o primeiro cliente da fila de atendimento e exibir uma mensagem indicando que ele foi atendido.
#  c. Exibir a fila de atendimento: o programa deve exibir a lista de clientes que ainda estão aguardando atendimento.

from collections import deque

print("Pronto Atendimento da GI-BI")
print("")
print("Para prossegir escolha uma opção:")
print("")
print("1 - Cadastrar novo cliente, 2 - Retirar clientes, 3 - Exibir lista de clientes, 4 - Finalizar atendimento")
print("")

def atendimento():
  cliente = deque([])
  clienteAtendido = []
  while True:
    opcao = input("Escolha a opção: ")
    print("")
    if opcao == "1":
      nome = input("Digite o nome do cliente: ")
      cliente.append(nome)
      print(f"Cliente '{nome}' foi adicionado há lista!")
      print("")
    elif opcao == "2":
      if len(cliente) > 0:
        clienteAtendido = cliente.popleft()
        print(f"O cliente '{clienteAtendido}' foi atendido!")
        print("")
      else:
        print("Não há clientes na fila.")
        print("")
    elif opcao == "3":
      if len(cliente) > 0:
        print("Clientes que ainda não foram atendidos:", cliente)
        print("")
      else:
        print("Não hà nenhum cliente na fila!")
        print("")
    else:
      print("Obrigada pela paciência!")
      break

atendimento()