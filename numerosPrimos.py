# Armazena os numeros primos
primos = []

for num in range(2, 31):
    # variavel de controle
    eh_primo = True

    # loop para verificar se o númro é primo
    n = 2
    while  n <= num // 2:
        if num % n == 0:
            eh_primo = False
            break
        n += 1
        
    # add o número primo a lista
    if eh_primo:
        primos.append(num)
        
    # imprimindo os primos
    print(f"Número primos: {primos}")