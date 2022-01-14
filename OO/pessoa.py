class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa('Roger', 49)
    print(p.nome, p.idade)
    print(Pessoa.cumprimentar(p))
    #Linha de cima e de baixo são a mesma coisa
    print(p.cumprimentar())