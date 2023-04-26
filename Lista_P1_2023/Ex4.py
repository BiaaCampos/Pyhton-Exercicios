# 4 -Desafio: Sistema de Cadastro de Produtos: Crie um sistema em Python que utilize a estrutura de dados dicionário para permitir o cadastro de produtos em um estoque. 
# O sistema deve permitir a inserção, remoção e atualização de produtos, bem como a exibição de todos os produtos cadastrados. 
# Cada produto deve possuir as seguintes informações: 
# a. Nome 
# b. Descrição 
# c. Preço 
# d. Quantidade em estoque O sistema deve ter um menu que permita ao usuário escolher entre as opções de inserir, remover, atualizar e exibir produtos, bem como sair do sistema. 
# Quando o usuário escolher uma das opções, o sistema deve solicitar as informações necessárias para realizar a operação (por exemplo, nome, descrição, preço, etc.). 
# Ao final de cada operação, o sistema deve exibir a lista atualizada de todos os produtos cadastrados.

print("MERCADINHO GI-BI")
print("")
print("Para prosseguir escolha uma opção:")
print("")
print("1 - Cadastrar Produtos, 2 - Remoção de Produto, 3 - Atualizar produtos, 4 - Mostrar lista de produtos, 5 - Mostar lista de opções,  6 - Finalizar")
print("")

def cadastroProdutosMercadinho():
  listaProdutos = []
  listaProdutosCadastrados = []
  opcaoAtualizacao = []
  valorAtualizacao = []
  quantidadeAtualizada = []
  opcoesEscolha = ["1 - Cadastrar Produtos, 2 - Remoção de Produto, 3 - Atualizar produtos, 4 - Mostrar lista de produtos, 5 - Mostar lista de opções, 6 - Finalizar"]
  while True:
    opcao = input("Escolha qual opção deseja realizar: ")
    print("")
    if opcao > "6":
      print("Escolha uma opção válida!")
    else:
      if opcao == "1":
        print("CADASTRAR PRODUTO!")
        print("")
        nomeProduto = input("Digite o nome do produto: ")
        descricaoProduto = input("Descrição do produto: ")
        precoProduto = float(input("Digite o preço do produto: "))
        quantidadeProduto = int(input("Digite a quantidade do produto: "))
        listaProdutosCadastrados = {"Nome": nomeProduto, "Descrição": descricaoProduto, "Preço": precoProduto, "Quantidade": quantidadeProduto}
        listaProdutos.append(listaProdutosCadastrados)
        print(f"Produto '{nomeProduto}' foi cadastrado com sucesso!")
        print("")
        print(listaProdutos)
        print("")
      elif opcao == "2":
        print("REMOVER PRODUTO!")
        print("")
        removerProduto = input("Digite qual produto deseja remover: ")
        produto_encontrado = False
        for i, produto in enumerate(listaProdutos):
          if produto["Nome"] == removerProduto:
            listaProdutos.pop(i)
            print(f"O produto '{removerProduto}' foi removido com sucesso!")
            print("")
            print(listaProdutos)
            print("")
            produto_encontrado = True
            break
        if not produto_encontrado:
          print("Produto não encontrado.")
      elif opcao == "3":
        print("ATUALIZAR PRODUTO!")
        print("")
        atualizarProduto = input("Digite o nome do produto que deseja atualizar: ")
        produtoEncontrado = False
        for produto in listaProdutos:
          if produto["Nome"] == atualizarProduto:
            produtoSelecionado = produto
            produtoEncontrado = True
            break
        if produtoEncontrado:
          while True:
            atualizacaoProduto = input("Qual dessas opções deseja modificar: a - Nome, b - Descrição, c - Preço, d - Quantidade, e - Todas as opções: ")
            if atualizacaoProduto in ["a", "b", "c", "d", "e"]:
              if atualizacaoProduto == "a":
                print("Opção selecionada: NOME")
                nomeAtualizado = input("Digite o novo nome: ")
                produtoSelecionado["Nome"] = nomeAtualizado
                print(f"Produto selecionado foi atualizado com sucesso!")
                print("")
                print(listaProdutos)
                print("")
              elif atualizacaoProduto == "b":
                print("Opção selecionada: DESCRIÇÃO")
                descricaoAtualizada = input("Digite a nova descrição: ")
                produtoSelecionado["Descrição"] = descricaoAtualizada
                print(f"Descrição do produto selecionado foi atualizado com sucesso!")
                print("")
                print(listaProdutos)
                print("")
              elif atualizacaoProduto == "c":
                print("Opção selecionada: PREÇO")
                precoAtualizado = float(input("Digite o novo preço: "))
                produtoSelecionado["Preço"] = precoAtualizado
                print(f"Preço do produto selecionado foi atualizado com sucesso!")
                print("")
                print(listaProdutos)
                print("")
              elif atualizacaoProduto == "d":
                print("Opção escolhida: QUANTIDADE")
                quantidadeAtualizada = int(input("Digite a quantidade atualizada: "))
                produtoSelecionado["Quantidade"] = quantidadeAtualizada
                print(f"Quantidade do produto selecionado foi atualizado com sucesso!")
                print("")
                print(listaProdutos)
                print("")
              elif atualizacaoProduto == "e":
                print("Opção escolhida: TODAS AS OPÇÕES")
                nomeAtualizado = input("Digite o novo nome: ")
                descricaoAtualizada = input("Digite a nova descrição: ")
                precoAtualizado = float(input("Digite o novo preço: "))
                quantidadeAtualizada = int(input("Digite a quantidade atualizada: "))
                produtoSelecionado["Nome"] = nomeAtualizado
                produtoSelecionado["Descrição"] = descricaoAtualizada
                produtoSelecionado["Preço"] = precoAtualizado
                produtoSelecionado["Quantidade"] = quantidadeAtualizada
                print("Todos as opções foram atualizadas com sucesso!")
                print("")
                print(listaProdutos)
                print("")
              break
        else:
          print("Escolha uma opção válida!")
      elif opcao == "4":
        print("LISTA DE PRODUTOS!")
        print("")
        print(f"Há {len(listaProdutos)} no estoque!")
        print("")
        print(f"Lista atualizada dos produtos: ")
        print(listaProdutos)
        print("")
      elif opcao == "5":
        print("Você pode escolher entre essas opções:")
        print(opcoesEscolha)
        print("")
      elif opcao == "6":
        print("FINALIZAR PROGRAMA!")
        print("")
        print("Valeeeeu!! :)")
        break
             
cadastroProdutosMercadinho()