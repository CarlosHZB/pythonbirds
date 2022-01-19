class Pessoa:
    olhos = 2

    def __init__(self,*filhos , nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'

    @staticmethod
    def metodo_estatico():
        return 23

    @classmethod
    def nome_e_atributo_de_classes(cls):
        return f'{cls} - olhos: {cls.olhos}'

class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    roger = Mutante(nome='Roger', idade=49)
    agamenon = Pessoa(nome='Agamenon', idade=58)
    andresa = Pessoa(roger, agamenon, nome='Andresa', idade=69)
    print(roger.nome, roger.idade)
    print(andresa.nome, andresa.idade)
    for filho in andresa.filhos:
        print('Filho:' + filho.nome)
    print(Pessoa.olhos)
    print('Olhos do roger:', roger.olhos)
    print(roger.metodo_estatico(), Pessoa.metodo_estatico())
    print(roger.nome_e_atributo_de_classes(), " - ", Pessoa.nome_e_atributo_de_classes())