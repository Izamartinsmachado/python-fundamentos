from time import sleep
print('*' * 40)
print('Analisador de Triángulos')
print('*' * 40)
ps = float(input('Primeiro Seguimento:'))
ss = float(input('Segundo Seguimento:'))
ts = float(input('Terceiro Seguimento:'))
print('Processando...')
sleep(3)
if ps < ss + ts and ss < ps + ts and ts < ps + ss:
    print('Os seguimentos acima podem formar triangulo')
else:
    print('Os seguimnentos acima não podem formar triangulo')
