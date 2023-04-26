# 3 - Desafio: Controle de Acesso: Imagine que você está trabalhando em uma empresa que desenvolve sistemas de controle de acesso a prédios corporativos. 
# Cada funcionário da empresa possui um crachá de acesso com seu nome, número de identificação e setor em que trabalha. Essas informações são armazenadas em uma tupla de tuplas, 
# onde cada tupla interna contém o nome, o número de identificação e o setor de um funcionário. 
# O desafio é escrever um programa em Python que permita realizar as seguintes operações: 
# a. Adicionar um novo funcionário à tupla de funcionários 
# b. Remover um funcionário existente da tupla de funcionários 
# c. Alterar o setor de um funcionário existente na tupla de funcionários 
# d. Consultar as informações de um funcionário existente na tupla de funcionários 
# e. Para implementar esse programa, você pode definir funções que realizam cada uma dessas operações, e usar a tupla de funcionários como uma variável global dentro do programa. 
# Para interagir com o usuário, você pode usar a função input() para receber os dados necessários, e a função print() para exibir as informações solicitadas.

print("empresa da GI-BI")
print("")
print("Para prossegir escolha uma opção:")
print("")
print("1 - Cadastrar funcionário, 2 - Modificar setor, 3 - Exibir funcionários, 4 - Remover Funcionário, 5 - Finalizar")
print("")

def empresa():
  tuplaFuncionario = []
  listaFuncionario = []
  funcionarioRemovido = []
  while True:
    opcao = input("Escolha a opção: ")
    print("")
    if opcao > "5":
        print("Escolha uma opção válida!")
    else:
      if opcao == "1":
        nomeFuncionario = input("Digite o nome do funcionário: ")
        id = input("Digite o número de identificação do funcionário: ")
        for funcionario in listaFuncionario:
          if funcionario[1] == id:
            print("Digite um ID válido ou inexistente:")
            id = input("")
          break
        setor = input("Digite o setor do funcionário: ")
        tuplaFuncionario = (nomeFuncionario, id, setor)
        listaFuncionario.append(tuplaFuncionario)
        print("")
        print(f"funcionario '{nomeFuncionario}' foi adicionado há lista!")
        print("")
      elif opcao == "2":
        funcModificado = input("Digite o nome do funcionário que será modificado: ")
        setorModificado = input("Digite o novo setor: ")
        funcionario_encontrado = False
        for i, funcionario in enumerate(listaFuncionario):
          if funcionario[0] == funcModificado:
            listaFuncionario[i] = (funcionario[0], funcionario[1], setorModificado)
            print("Setor do funcionário modificado com sucesso!")
            print("")
            funcionario_encontrado = True
            break
        if not funcionario_encontrado:
          print("Funcionário não encontrado.")
      elif opcao == "3":
        if len(listaFuncionario) > 0:
          print(f"Há {len(listaFuncionario)} funcionários na lista!")
          print("")
          detalhesFuncionarios = []
          for funcionario in listaFuncionario:
            detalhesFuncionario = (funcionario[0], funcionario[1], funcionario[2])
            detalhesFuncionarios.append(detalhesFuncionario)
          print("")
          print(tuple(listaFuncionario))
        else:
          print("Não há funcionários na lista!")
          print("")
      elif opcao == "4":
        funcionarioRemovido = input("Digite o nome do funcionário que será removido: ")
        funcionario_encontrado = False
        for i, funcionario in enumerate(listaFuncionario):
          if funcionario[0] == funcionarioRemovido:
            listaFuncionario.pop(i)
            print(f"Funcionário {funcionarioRemovido} removido com sucesso!")
            print("")
            funcionario_encontrado = True
            break
        if not funcionario_encontrado:
          print("Funcionário não encontrado.")
      elif opcao == "5":
        print("Valeeeeeeu!!! :)")
        break


empresa()