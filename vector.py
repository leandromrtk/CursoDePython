# inicia vetor vazio
vetor = []
i = 0
tamanho_vetor = int(input("Digite o tamanho do vetor: "))

for i in range(tamanho_vetor):
    n = float(input("Digite um numero para iniciar o vetor: "))
    i += 1
    vetor.append(n) # adiciona valores ao vetor
    
soma = 0
for i in range(tamanho_vetor):
     soma += n

media = soma / len(vetor) # media dos vetores

print(f"Media do vetor: {media}")

soma = sum(vetor)
print(f"Tamanho do vetor: {len(vetor)}")
print(soma)
print("="*4)
