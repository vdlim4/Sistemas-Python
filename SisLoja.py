print('Bem-Vindo a loja do Victor Diego de Lima')
valor = float(input('Informe o valor do produto: ')) #Entrada do valor dos produtos.
quantidade = float(input('Informe a quantidade de produtos: ')) #Entrada da quantidade dos produtos.
subTotal = valor * quantidade #Cálculo valor total sem desconto.

#Estrutura para verificar a porcentagem de desconto.
if (quantidade < 10): #Até 9 unidades.
    desconto = 0
elif (quantidade < 100): #De 10 até 99 unidades.
    desconto = 5
elif (quantidade < 1000): #De 100 até 999 unidades.
    desconto = 10
else: #Mais que 1000 unidades.
    desconto = 15

calculoDesc = subTotal * (desconto / 100) #Cálculo valor do desconto.
total = subTotal - calculoDesc #Cálculo valor total com desconto.

print('O valor sem desconto foi de: R$ {:.2f}' .format(subTotal))
print('O valor com desconto foi de: R$ {:.2f} (Desconto {}%)' .format(total, desconto))