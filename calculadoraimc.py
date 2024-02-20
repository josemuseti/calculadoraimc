peso = float(input ('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é oa sua altura?(m) '))
imc = peso/ (altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if  imc < 18.5:
    print ('Você esta abaixo do peso')
elif 18.5 <= imc < 25:
    print ('Você esta na faixa de peso')
elif imc >= 25 :
    print ('Você esta em sobrepeso')
