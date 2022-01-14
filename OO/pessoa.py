class Pessoa:
    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    #Linha de cima e de baixo são a mesma coisa
    print(p.cumprimentar())