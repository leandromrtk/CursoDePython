
n = int(input("quantos numeros vai digitar? "))
vet = []
i = 0

for i in range(n):
    i = int(input("Digite um número: "))
    i += 1
    vet.append(n) 
    
print("Numeros negativos:")
soma_negativos = 0
for i in vet:
    if i < 0:
        print(i)
       
print(f"Soma dos negativos: {soma_negativos}")


# Perguntar ao usuário o tamanho do vetor
tamanho_vetor = int(input("Digite o tamanho do vetor: "))

# Criar um vetor do tamanho desejado
vetor = [0] * tamanho_vetor

# Preencher o vetor com números fornecidos pelo usuário
for i in range(tamanho_vetor):
    vetor[i] = int(input(f"Digite o número para a posição {i}: "))

# Verificar e imprimir os números negativos
print("Números negativos no vetor:")
for numero in vetor:
    if numero < 0:
        print(numero)