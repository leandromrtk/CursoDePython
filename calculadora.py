class Calculadora: ## Declaração da Classe
    
    def __init__(self, numero1, numero2): ## método construtor
        self.numero1 = numero1
        self.numero2 = numero2

    def somar(self):
        soma = self.numero1 + self.numero2
        print(f"Resultado da soma: ", soma)

    def multiplicar(self):
        mult = self.numero1 * self.numero2
        print(f"Resultado da multiplicação: ", mult)

    def dividir(self):
        divida = self.numero1 / self.numero2
        print(f"Resultado da Divisão: ", divida)

    def diminuir(self):
        diminua = self.numero1 - self.numero2
        print(f"Resultado da subtração: ", diminua)
