#Programa criado por ABNER CESTARI

#Variaveis Globais

lista_funcionarios = [] #lista
codigo_funcionario = 0 #contador

#Função para cadastrar funcionario
def cadastrar_func (codigo): #função 1
    print ('\n*****************************************************')
    print ('*** Bem vindo ao menu de cadastrar funcionário(s) ***')
    print ('*****************************************************\n')
    print ('O ID do funcionário novo é: {}'.format(codigo))
    nome = input('Digite o nome do funcionário: ')
    setor = input('Digite o setor: ').upper()

#Loop para garantir que o usuário não digite valores incorretos para o campo de 'salário' usando excessões
    while True:
        try:
            salario = int(input('Digite o salário: R$ '))
        except (ValueError): #excessão, caso o usuário digite 0 ou quaisquer outro tipo de caracteres
            print ('Valor inválido, digite apenas números inteiros.\n')
            continue #volta ao inicio do laço
        if salario >= 1: #caso o valor digitado de salário for maior ou igual a 1, o programa segue saindo do laço
            break

    dicionario_func = {'ID'     : codigo,
                    'Nome'      : nome,
                    'Setor'     : setor,
                    'Salário'   : salario}
    lista_funcionarios.append(dicionario_func.copy()) #todos os dados são salvos em uma cópia da lista
    print ('Funcionário cadastrado com sucesso!')

#Função para consultar funcionário
def consultar_func ():
    print ('') 
    print ('**************************************************')
    print ('*** Bem vindo ao menu de consultar funcionário ***')
    print ('**************************************************')
    while True:
        opcao_consultar = input ('\nEscolha a opção desejada:\n'+
                                 '1 - Consultar todos os funcionários\n'+
                                 '2 - Consultar funcionário por ID\n'+
                                 '3 - Consultar funcionário por setor\n'+
                                 '4 - Retornar ao menu principal\n'+
                                 '>> ')

        if opcao_consultar == '1':
            print ('Você escolheu consultar todos os funcionários\n')
            for funcionario in lista_funcionarios: #loop para varrer todas a lista de funcionários
                print ('--------------------------------')
                for key, value in funcionario.items():
                    print ('{}: {}'.format(key,value))

        elif opcao_consultar == '2':
            print ('Você escolheu consultar funcionário por ID\n')
            try: #novamente prevenção para não causar error de valor
                valor_desejado = int(input ('Entre com o ID desejado: '))
            except (ValueError):
                print ('ID não encontrada, tente novamente')
                continue
            for funcionario in lista_funcionarios:
                if funcionario['ID'] == valor_desejado:
                    print ('--------------------------------')
                    for key, value in funcionario.items():
                        print ('{}: {}'.format(key,value))

        elif opcao_consultar == '3':
            print ('Você escolheu consultar funcionário por setor\n')
            valor_desejado = input ('Entre com o setor desejado: ').upper()
            for funcionario in lista_funcionarios:
                if funcionario['Setor'] == valor_desejado:
                    print ('--------------------------------')
                    for key, value in funcionario.items():
                        print ('{}: {}'.format(key,value))

        elif opcao_consultar == '4':
            return #sai da função e retorna para o programa principal
        else:
            print ('Opção inválida!\n')
            continue #volta para o início do laço

#Remover funcionário
def remover_func ():
    print ('')
    print ('************************************************')
    print ('*** Bem vindo ao menu de remover funcionário ***')
    print ('************************************************\n')

#Loop para garantir que o usuário não digite valores incorretos para o campo de 'ID' usando excessões
    while True:
        try:
            valor_desejado = int(input('Entre com o ID do funcionário que deseja remover: '))
        except (ValueError):
            print ('ID não encontrada, tente novamente.\n')
            continue
        if valor_desejado >= 1:
            break
        else:
            print ('ID não encontrada, tente novamente')
            continue

    for funcionario in lista_funcionarios:
        if funcionario['ID'] == valor_desejado:
            lista_funcionarios.remove(funcionario) #função .remove para deletar chave da lista
            print ('Funcionario removido com sucesso.')

#programa principal
print ('*****************************************************************************')
print ('** Bem-vindo ao programa de gerenciamento de funcionários do Abner Cestari **')
print ('*****************************************************************************')

while True:
    opcao_principal = input ('\nEscolha a opção desejada:\n'+
                             '1 - Cadastrar funcionário\n'+
                             '2 - Consultar funcionários\n'+
                             '3 - Remover funcionário\n'+
                             '4 - Sair\n'+
                             '>> ')

    if opcao_principal == '1':
        codigo_funcionario = codigo_funcionario + 1 #caso a escolha 1 for feita, um novo número será adicionado ao contador que servirá de códio de identificação para o funcionário
        cadastrar_func(codigo_funcionario)

    elif opcao_principal == '2':
        consultar_func()

    elif opcao_principal == '3':
        remover_func()

    elif opcao_principal == '4':
        break #encerra o laço do programa principal e o encerra

    else:
        print ('Opção inválida!\n')
        continue #repete o laço caso o usuário digitar algo além dos números disponíveis no menu

#Fim do programa