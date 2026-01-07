velocidade = float(input('Qual é a velocidade atual? '))
if velocidade > 80:
    print('MULTADO! Você ultrapassou o limite de 80KM/h!')
    multa = (velocidade - 80) * 7
    print('A sua multa ficou no valor de R${:.2f}!'.format(multa))
print('Tenha um bom dia, e dirija com segurança!')