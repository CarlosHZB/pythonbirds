class Pessoa:
    def __init__(self,*filhos , nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    roger = Pessoa(nome='Roger', idade=49)
    agamenon = Pessoa(nome='Agamenon', idade=58)
    andresa = Pessoa(roger, agamenon, nome='Andresa', idade=69)
    print(roger.nome, roger.idade)
    print(andresa.nome, andresa.idade)
    for filho in andresa.filhos:
        print('Filho:' + filho.nome)
