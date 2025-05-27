from math import sqrt

class NumeronegativoError(Exception):
    def __init__(self):
        pass

if __name__ == '__main__':
    try:
        num = int(input('Difgite um numero positivo: '))
        if num < 0:
            raise NumeronegativoError
    except NumeronegativoError:
        print(f'Foi fornecido um numero negativo')
    else:
        print(f'A Raiz quadrada de {num} é {sqrt(num)}')
    finally:
        print(f'Fim do calculo')