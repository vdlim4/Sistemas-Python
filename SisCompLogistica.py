def dimensoesObjeto(): #Função para verificar e recolher os dados de dimensão do objeto.
    while True:
        try: #Verificação do valor a pagar.
            comp = float(input('Digite o comprimento do objeto (em cm): ')) #Comprimento do objeto.
            larg = float(input('Digite a largura do objeto (em cm): ')) #Largura do objeto.
            alt = float(input('Digite a altura do objeto (em cm): ')) #Altura do objeto.

            volume = comp * larg * alt
            print(f'O volume do objeto é (em cm³): {volume}')

            if (volume < 1000):
                valor = 10
            elif (volume < 10000):
                valor = 20
            elif (volume < 30000):
                valor = 30
            elif (volume < 100000):
                valor = 50
            else: #Caso o produto exceda o limite de cm³.
                print('Não aceitamos objetos com dimensões tão grandes!')
                print('Por favor entre com as dimensôes novamente.')
                continue #Retorna ao inicio do laço de repetição.
        except ValueError: #Caso digite um valor não numérico, retorna uma mensagem de erro e solicida novamente os dados.
            print('Valor digitado não é numérico!')
            print('Por favor entre com as dimensôes novamente.')
        else: #Caso ocorra tudo dentro dos padrões, a função retorna o valor em uma variável.
            return valor

def pesoObjeto(): #Função para verificar o peso do objeto.
    while True:
        try: #Verifica o peso e informa o multiplicador.
            kg = float(input('Digite o peso do objeto (em KG): ')) #Peso do objeto.

            if (kg < 0.1):
                valor = 1
            elif (kg < 1):
                valor = 1.5
            elif (kg < 10):
                valor = 2
            elif (kg < 30):
                valor = 3
            else: #Caso o objeto passe do peso máximo.
                print('Não aceitamos objetos tão pesados!')
                print('Por favor entre com o peso novamente.')
                continue #Retorna ao inicio do laço de repetição.
        except ValueError: #Caso digite um valor não numérico, retorna uma mensagem de erro e solicida novamente os dados.
            print('Você digitou o peso com um valor não numérico!')
            print('Por favor entre com o peso novamente.')
        else: #Caso ocorra tudo dentro dos padrões, a função retorna o multiplicador em uma variável.
            return valor 

def rotaObjeto(): #Função para solicitar e verificar a rota escolhida.
    while True: #Verifica se rota é existente e informa o multiplicador.
            print('Selecione a rota:')
            print(' BR - De Brasília para Rio de Janeiro')
            print(' BS - De Brasília para São Paulo')
            print(' RB - De Rio de Janeiro para Brasília')
            print(' SR - De São Paulo para Rio de Janeiro')
            print(' SB - De São Paulo para Brasília')
            print(' RS - De Rio de Janeiro para São Paulo')
            rota = input('>> ') #Rota escolhida para o objeto.

            if (rota == 'BR'):
                valor = 1.5
            elif (rota == 'BS'):
                valor = 1.2
            elif (rota == 'RB'):
                valor = 1.5
            elif (rota == 'SR'):
                valor = 1
            elif (rota == 'SB'):
                valor = 1.2
            elif (rota == 'RS'):
                valor = 1
            else: #Caso a rota seja diferente das siglas informadas a cima, retorna a mensagem de erro e solicita os dados novamente.
                print('Rota inexistente!')
                print('Por favor entre com a rota novamente.')
                continue #Retorna ao inicio do laço de repetição.
            break
    return valor #Caso ocorra tudo dentro dos padrões, a função retorna o multiplicador em uma variável.

#Programa principal:

print('Bem-Vindo a Companhia de Logística do Victor Diego de Lima')
print('-' * 60)
RU_do_Aluno = 4465543

dimen = dimensoesObjeto() #Chama a função para solicitar as dimensôes do objeto!

peso = pesoObjeto() #Chama a função para solicitar o peso do objeto!

rota = rotaObjeto() #Chama a função para solicitar a rota desejada!

calc = dimen * peso * rota #Calculo para saber o valor a ser pago!

print('Finalizando...\n')
print('-' * 65)
print(f'Total a pagar(R$): {calc:.2f} (Dimensões: {dimen} * Peso: {peso} * Rota: {rota})') #Mensagem com o valor total e o calculo dos multiplicadores.
print('-' * 65)