class Direcao:
    valor = 'Norte'

    @classmethod
    def girar_direita(cls):
        if cls.valor == 'Norte':
            cls.valor = 'Leste'
        elif cls.valor == 'Leste':
            cls.valor = 'Sul'
        elif cls.valor == 'Sul':
            cls.valor = 'Oeste'
        else:
            cls.valor = 'Norte'

    @classmethod
    def girar_esquerda(cls):
        if cls.valor == 'Norte':
            cls.valor = 'Oeste'
        elif cls.valor == 'Oeste':
            cls.valor = 'Sul'
        elif cls.valor == 'Sul':
            cls.valor = 'Leste'
        else:
            cls.valor = 'Norte'


if __name__ == '__main__':
    direcao = Direcao()
    print(direcao.valor)
    direcao.girar_direita()
    print(direcao.valor)
    direcao.girar_direita()
    print(direcao.valor)
    direcao.girar_esquerda()
    print(direcao.valor)
    direcao.girar_esquerda()
    print(direcao.valor)