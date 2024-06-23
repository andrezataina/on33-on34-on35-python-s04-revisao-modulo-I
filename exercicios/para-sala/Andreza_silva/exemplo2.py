'''peso/(altura x altura)'''
def calculo_imc():
    altura = float(input('Digite a sua altura: '))
    peso = float(input('Digite o seu peso: '))
    calculo = peso / (altura ** 2)
    return calculo 
print(f'O seu imc é {calculo_imc()}')

