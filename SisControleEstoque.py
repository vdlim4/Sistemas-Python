def cadastrarPeca(codigo): #Função para cadastrar novas peças.
        print(f'Código da peça 00{codigo}')
        nome = input('Nome da peça: ') #Solicita o nome da peça.
        fabricante = input('Fabricante da peça: ') #Solicita o fabricante da peça.
        while True: #Verifica se o valor digitado é numérico.
            try:
                valor = float(input('Valor da peça: '))
            except:
                print('Valor inválido, insira novamente!') #Caso o valor não for numérico, informa o erro e solicita novamente.
            else:
                break #Se ocorrer tudo dentro dos padrões, o programa segue.
        dicionárioProduto = {'codigo':codigo, 'nome':nome, 'fabricante':fabricante, 'valor':valor} #Dicionario de cadastro das peças.
        listaProdutos.append(dicionárioProduto.copy()) #Adiciona o novo cadastro a uma lista com todos os outros itens adicionados.

def consultarPecas(): #Função para consultar as peças já cadastradas.
    while True: #Verifica se a opção digitada está de acordo com o informado (numérico).
        print('Escolha a opção desejada:')
        print('1 - Consultar todas as Peças')
        print('2 - Consultar Peças por Código')
        print('3 - Consultar Pecas por Fabricante')
        print('4 - Retornar')

        try:
            opcaoConsulta = int(input('>> ')) #Coleta a opção de consulta.
        except:
            print('Opção inválida, insira novamente!') #Caso o valor não for numérico, informa o erro e solicita novamente.
        else: #Se ocorrer tudo dentro dos padrões, o programa segue.
            if (opcaoConsulta == 4):
                return
            elif (opcaoConsulta == 1):
                for produto in listaProdutos: #Passa por toda a lista de produtos.
                    print('-' * 20)
                    for i, j in produto.items(): #Recebe as informações de cada produto.
                        print(f'{i}: {j}') #Imprime na tela cada produto.
                    print('-' * 20)
            elif (opcaoConsulta == 2):
                codigoP = int(input('Código da peça: ')) #Coleta o código desejado.
                for produto in listaProdutos:
                    if (produto['codigo'] == codigoP): #Verifica se o codigo digitado confere com algum já existente na lista.
                        print('-' * 20)
                        for i, j in produto.items(): #Recebe as informações do produto.
                            print(f'{i}: {j}') #Imprime na tela cada produto.
                        print('-' * 20)
            elif (opcaoConsulta == 3):
                fabricanteP = input('Fabricante da peça: ') #Coleta o fabricante desejado.
                for produto in listaProdutos:
                    if (produto['fabricante'] == fabricanteP): #Verifica se o fabricante digitado confere com algum já existente na lista.
                        print('-' * 20)
                        for i, j in produto.items(): #Recebe as informações do produto.
                            print(f'{i}: {j}') #Imprime na tela cada produto aquele fabricante.
                        print('-' * 20)
            else:
                print('Opção inválida, favor tentar novamente!') #Caso o número informado não estiver no menu, retorna e solicita novamente.

def removerPeca(): #Função para remover alguma peça cadastrada.
    try: #Verifica se o valor digitado é numérico.
        remover = int(input('Digite o código da peça a ser removida: ')) #Coleta o código desejado para a remoção.
    except:
        print('Código inválido, favor tentar novamente!') #Caso o valor informado não for numérico, retorna e solicita novamente.
    else: #Se ocorrer tudo dentro dos padrões, o programa segue.
        for produto in listaProdutos:
            if (produto['codigo'] == remover): #Verifica se o código digitado está na lista.
                listaProdutos.remove(produto) #Remove o item relacionado ao código digitado acima.
                print('Peça removida com sucesso!')

#Programa principal:
print('Bem-Vindo ao Controle de Estoque da Biscicletaria do Victor Diego de Lima')
RU_do_Aluno = 4465543
#Variáveis globais:
codigoProduto = 0 #Contador para o código dos produtos.
listaProdutos = [] #Lista com todos os produtos já cadastrados.

#Laço de repetição para o menu principal.
while True:
    print('Escolha a opção desejada:')
    print('1 - Cadastrar peças')
    print('2 - Consultar Peças')
    print('3 - Remover peças')
    print('4 - Sair')
    
    try: #Verifica se o valor digitado é numérico.
        opcao = int(input('>> ')) #Coleta a opção desejada.
    except:
        print('Opção inválida, favor tentar novamente!') #Caso o valor não for numérico, informa o erro e solicita novamente.
    else: #Se ocorrer tudo dentro dos padrões, o programa segue.
        if (opcao == 4): # Opção 'Sair'.
            print('Encerrado...')
            break #Encerra o programa.
        elif (opcao == 1): #Opção 'Cadastrar Peças'.
            print('Você escolheu a opção de Cadastrar Peças')
            codigoProduto += 1 #Adiciona um ao contador.
            cadastrarPeca(codigoProduto) #Chama a função de cadastrar.
            continue
        elif (opcao == 2): #Opção 'Consultar Peças'.
            print('Você escolheu a opção de Consultar Peças')
            consultarPecas() #Chama a função de consultar.
        elif (opcao == 3): #Opção 'Remover Peças'.
            print('Você escolheu a opção de Remover peças')
            removerPeca() #Chama a função de remover.
        else:
            print('Opção inválida, favor tentar novamente.') #Caso o número informado não estiver no menu, retorna e solicita novamente.