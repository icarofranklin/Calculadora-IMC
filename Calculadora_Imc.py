peso = float(input('Qual é seu peso? (KG) '))
altura = float(input('Qual é sua altura? (m) '))

imc = peso / (altura**2)
print('O IMC dessa pessoa é de {}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')

elif imc >= 18.5 and imc < 25:
    print('Você está na faixa de PESO normal')

elif imc >= 25 and imc < 30: 
    print('Você está SOBREPESO')

elif imc >= 30 and imc < 40:
    print('Cuidado, você está em OBESIDADE!')

elif imc >= 40:
    print ('Tome muito cuidado, você está em OBESIDADE MORBIDA!')