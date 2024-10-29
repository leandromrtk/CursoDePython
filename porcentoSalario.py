print("Valor salarial")


def salario_(salario, porcentagem):

    porcentagem_do_salario = salario * (porcentagem / 100)

    return porcentagem_do_salario


salario = float(input("Digite o salario: "))
porcentagem = float(input("Dgite a porcentagem: "))

print(f"Porcentagem do salario: R$ {salario_(salario, porcentagem)}")

aumento_salarial = salario + salario_(salario, porcentagem)

print(f"Salario aumentou para: R$ {aumento_salarial}")

