def calculadora(a,b,c):
    if c == '+':
        return a + b
    elif c == '-':
        d = input('Deseja calcular o primeiro valor menos o segundo?(S/N) Caso não sera calculado o inverso')
        if d == 'S' or d == 's':
            return a - b
        elif d == 'N' or d == 'n':
            return b - a
        else:
            return 'Resposta invalida'
    elif c == '*':
        return a * b
    elif c == '/':
        d = input('Deseja calcular o primeiro valor dividido pelo segundo?(S/N) Caso não sera calculado o inverso: ')
        if d == 'S' or d == 's':
            e = input('Deseja saber o resto da operação?(S/N): ')
            if e == 'S' or e =='s':
                Resultados = []
                Resultados.append(a/b)
                Resultados.append(a%b)
                return Resultados
            else:
                return a / b
        elif d == 'N' or d == 'n':
            e = input('Deseja saber o resto da operação?(S/N)')
            if e == 'S' or e =='s':
                Resultados = []
                Resultados.append(b/a)
                Resultados.append(b%a)
                return Resultados
            else:
                return b / a
        else:
            return 'Resposta invalida'
    else:
        return 'Operador invalido'

title = 'Calculadora'    
print(title.center(20, '-'))
loop = 1
while loop == 1:
    loop = int(input('Caso queira parar de Calcular 2 valores insira qualquer valor que não seja 1: '))
    if loop == 1:
            x = int(input('Digite um numero para calcular: '))
            y = int(input('Digite outro numero para calcular: '))
            z = input('Digite qual o operador que ira usar (+,-,* ou /): ')
            res = calculadora(x,y,z)
            print(res)
    else:
        print('Calculadora encerrada...')
        break

print('Fim do programa')
