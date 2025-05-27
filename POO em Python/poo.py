# orientação a objetos: paradigma de programação
# Classes e objetos
from objetos import *

class Veiculo:
    def movimentar(self):
        print(f'sou um veiculo e me desloco')
    
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo # __ deixa o atributo privado dentro da classe
        self.__num_registro = None

    #setter gravar elemento na classe
    def set_num_registro(self, registro):
        self.__num_registro = registro

    # getter permitir acessar algo dentro da classe
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')    
    
    def get_num_registro(self):
        return self.__num_registro

class Carro(Veiculo):
    #metodo init sera herdado
    def movimentar(self):
        print(f'sou um carro e ando por ruas')

class Motocicleta(Veiculo):
    def movimentar(self):
        print(f'Corro muito')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)
    
    def get_categoria(self):
        return self.__cat
    
    def movimentar(self):
        print(f'eu voo alto')
if __name__ == '__main__':
    meu_veiculo = Veiculo('GM','Cadillac')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro('490321-1')
    print(f'Registro: {meu_veiculo.get_num_registro()}\n')

    meu_carro = Carro('Volkswagen', 'Polo')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()

    seu_carro = Carro('Audi', 'AS Sportback')
    seu_carro.movimentar()
    seu_carro.get_fabr_modelo()

    moto = Motocicleta('Harley Davidson', 'Nightster special')
    moto.movimentar()
    moto.get_fabr_modelo()

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f'Categoria: {meu_aviao.get_categoria()}')

    meu_computador = Computador('Peça', 'Fiat')
    meu_computador.perifericos()