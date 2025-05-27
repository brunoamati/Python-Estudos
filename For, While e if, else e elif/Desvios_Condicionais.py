# Simples, composto, encadeado
# Operadores = if, else, elif

n1 = n2 = 0.0
media = 0.0

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota nota: '))

# calcular media aritimetica das notas
media = (n1+n2) / 2

if (media >= 7): #simples apenas usa esse
    print("Aprovado!")
    print("Parabens!")
elif (media>=5): #encadeado usa esse
    print('Recuperação...')
else: #composto usa esse
    print('Reprovado...')

print('Sua média é : {}'.format(media)) #.format é outra concatenação
