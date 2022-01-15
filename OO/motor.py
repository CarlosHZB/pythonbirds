class Motor:
    velocidade = 0

    @classmethod
    def acelerar(cls):
        cls.velocidade += 1

    @classmethod
    def frear(cls):
        cls.velocidade -= 2

if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)