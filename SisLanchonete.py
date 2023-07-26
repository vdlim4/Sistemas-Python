print('Bem-Vindo a Lanchonete do Victor Diego de Lima')
print('-----------------CARDÁPIO-----------------')
print('| Código |       Descrição       | Valor |')
print('| 100    |    Cachorro-Quente    |  9,00 |')
print('| 101    | Cachorro-Quente Duplo | 11,00 |')
print('| 102    |        X-Egg          | 12,00 |')
print('| 103    |        X-Salada       | 12,00 |')
print('| 104    |        X-Bacon        | 14,00 |')
print('| 105    |        X-Tudo         | 17,00 |')
print('| 200    |   Refrigerante Lata   |  5,00 |')
print('| 201    |      Chá Gelado       |  4,00 |')

valor = 0 #Valor a ser somado após o pedido.
while True:
    codigo = int(input('Entre com o código desejado: ')) #Entrada do código do produto.
    
    #Estrutura para verificação dos códigos:
    if (codigo == 100):
        print('Você pediu um Cachorro-Quente no valor de R$9,00')
        valor += 9
    elif (codigo == 101):
        print('Você pediu um Cachorro-Quente Duplo no valor de R$11,00')
        valor += 11
    elif (codigo == 102):
        print('Você pediu um X-Egg no valor de R$12,00')
        valor += 12
    elif (codigo == 103):
        print('Você pediu um X-Salada no valor de R$12,00')
        valor += 12
    elif (codigo == 104):
        print('Você pediu um X-Bacon no valor de R$14,00')
        valor += 14
    elif (codigo == 105):
        print('Você pediu um X-Tudo no valor de R$17,00')
        valor += 17
    elif (codigo == 200):
        print('Você pediu um Refrigerante Lata no valor de R$5,00')
        valor += 5
    elif (codigo == 201):
        print('Você pediu um Chá Gelado no valor de R$4,00')
        valor += 4
    else: #Retorno caso a opção seja inválida.
        print('Opção inválida!')
        continue
    
    #Laço de repetição para a verificação da variável pedirMais:
    while True:
        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('0 - Não')
        pedirMais = int(input('>> '))
        if (pedirMais == 1 or pedirMais == 0): 
            break #Finaliza a verificação e passa para o if seguinte fora do laço.
        else: #Caso digite algo alem de 0 e 1, o laço informa o erro e repete a pergunta.
            print('Opção incorreta!')
            continue
    if (pedirMais == 1): #Caso digite 1, o programa reinicia.
        continue
    else: #Caso digite 0, o programa finaliza.
        break

print('Finalizando pedido...')
print('O total a ser pago é: R${:.2f}' .format(valor)) #Valor total do pedido.