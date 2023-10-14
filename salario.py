salario = float(input("salraio do funcionario é: R$"))
aumento = salario + (salario * 15/100)

print("o salario era R$ {:.2f} agora com aumento de 15% passa a ganhar R$ {:.2f}".format(salario, aumento))