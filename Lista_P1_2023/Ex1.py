# 1 - Desafio: Pilha de produtos em um depósito: Imagine que você está trabalhando em uma empresa de armazenamento de materiais de construção e precisa desenvolver um programa em Python 
# para gerenciar a entrada e saída de produtos em um depósito. Você decide utilizar a estrutura de dados lista como uma pilha para armazenar as informações dos produtos que entram no 
# depósito. Cada produto será representado por um dicionário contendo as seguintes informações: nome, quantidade, data de entrada e data de validade. Ao receber um novo produto, 
# o programa deverá inseri-lo na pilha. Ao realizar uma venda, o programa deverá retirar o produto mais antigo que ainda está dentro da validade. 
# Caso não haja produtos dentro da validade, o programa deverá exibir uma mensagem de alerta. Para facilitar a visualização dos produtos, o programa deverá 
# ter uma opção de listar todos os produtos presentes na pilha, ordenados por data de entrada (do mais antigo para o mais recente). Para completar o desafio, você deve implementar 
# essa solução utilizando a estrutura de dados lista como uma pilha em Python.


import datetime 

dataAtual = datetime.date.today()

print("Empresa de motinha da GI-BI")
print("")
print("Para prosseguir escolha uma opção:")
print("")
print("1 - Cadastrar novo produto, 2 - venda de produto, 3 - Exibir lista de clientes, 4 - Finalizar")
print("")

def empresaGiBi():
    listaProdutos = []
    while True:
        opcao = input("Escolha uma opção: ")
        print("")
        if opcao not in ["1", "2", "3", "4"]:
            print("Escolha uma opção válida!")
        else:
            if opcao == "1":
                print("CADASTRO DE PRODUTOS")
                print("")
                nomeProduto = input("Digite o nome do produto: ")
                quantidadeProduto = int(input("Quantidade: "))
                count = 1
                while count <= quantidadeProduto:
                    dataEntrada = input(f"Posição: {count} \n Digite a data de produção do produto (no formato dd/mm/aaaa): ")
                    dataEntrada = datetime.datetime.strptime(dataEntrada, '%d/%m/%Y').date()
                    dataValidade = input("Digite a data de validade do produto (no formato dd/mm/aaaa): ")
                    dataValidade = datetime.datetime.strptime(dataValidade, '%d/%m/%Y').date()
                    listaProd = {'nome': nomeProduto, 'quantidade': 1, 'dataEntrada': dataEntrada,'dataValidade':  dataValidade}
                    listaProdutos.append(listaProd)
                    count += 1
                print("")
                print("Lista de Produtos atualizada:")
                print(listaProdutos)
                print("")
            elif opcao == "2":
                produtoVendido = False
                print("VENDER PRODUTOS")
                print("")
                itemVendido = input("Digite o nome do produto a ser vendido: ")
                for i, produto in enumerate(listaProdutos):
                    if produto['nome'] == itemVendido and dataAtual <= produto['dataValidade']:
                        print(f"O produto '{produto['nome']}' foi vendido.")
                        listaProdutos.remove(produto)
                        print("Lista de produtos que não foram vendidos:")
                        print(listaProdutos)
                        print("")
                        produtoVendido = True
                        break
                if not produtoVendido:
                    print("Não há nenhum produto com esse nome ou na validade para ser vendido!")
                    print("")
            elif opcao == "3":
                print("Lista de Produtos")
                for produto in reversed(listaProdutos):
                  print(listaProdutos)
                print("")
            elif opcao == "4":
                print("Tchau! :)")
                break

empresaGiBi()
