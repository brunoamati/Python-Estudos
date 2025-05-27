class Objeto():
    def __init__(self,tipo,fabricante):
        self.tipo = tipo
        self.fabricante = fabricante
        self.__registro = None

    def set_registro(self,registro):
        self.__registro = registro

    def get_registro(self):
        return self.__registro
    
    def get_fabr_tp(self):
        print(f'Tipo do objeto: {self.tipo}\nFabricante do objeto: {self.fabricante}\n')

class Eletronico(Objeto):
    def energia(self):
        print(f'funciono com energia')

class Computador(Eletronico):
    def perifericos(self):
        print(f'Tenho perifericos')

def num_registro():
        while True:
            c = input(f'Tem numero de registro?(S/N)')
            if c == 'S' or c == 's':
                d = input('Digite o numero do registro: ')
                return d
            elif c == 'N' or c == 'n':
                return 'Sem numero de Registro'
            else:
                print(f'Resposta invalida,tente novamente')

if __name__ == '__main__':
    a = input(f'Digite o tipo do pruduto(Artigo, mercadoria, peça): ')
    b = input(f'Digite o fabricante: ')

    
    objeto_1 = Objeto(a,b)
    objeto_1.get_fabr_tp()
    objeto_1.set_registro(num_registro())
    print(f'N° de registro: {objeto_1.get_registro()}')

    meu_computador = Computador('Mercadoria','Lenovo')
    meu_computador.energia()
    meu_computador.perifericos()