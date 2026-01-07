p = float(input('Qual é o preço do produto? R$'))
d = p - (p * 5 / 100)
print('O preço do produto com o desconto de 5% passou de R${:.2F} para R${:.2F}.'.format(p, d))
