# Recursividade

# Formula geral para o fatorial
# fat(num) = 1, se num  = 0 ou se num = 1 'Caso Base'
# fat(num) = num * fat(num - 1), para num > 1 'Caso Recursivo'

def fat(num):
    if num == 0 or num == 1:
        return 1 
    else:
        return num * fat(num - 1)

if __name__ == '__main__':
    x = int(input('Digite um numero inteiro positivo para calcular o fatorial: '))
    try:
        res = fat(x)
    except RecursionError:
        print(f'O numero fornecido é muito grande ou negativo')
    else:
        print(f'o fatorial de {x} é {res}')