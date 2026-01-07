a = int(input('Qual é o primeiro número?'))
b = int(input('Qual é o segundo número?'))
c = int(input('Qual é o terceiro número?'))
#verificando qual é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando qual é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número é o {}'.format(menor))
print('O maior número é o {}'.format(maior))
