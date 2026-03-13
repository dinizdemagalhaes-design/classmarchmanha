valor_da_hora = float(input("Digite o valor da hora trabalhada (R$): "))
horas = float(input("Digite a quantidade de horas trabalhadas: "))
salario = valor_da_hora * horas

if salario <= 2112:
    imposto = 0
elif salario <= 2826.65:
    imposto = salario * 0.075
elif salario <= 3757.05:
    imposto = salario * 0.15
elif salario <= 4664.68:
    imposto = salario * 0.225
else:
    imposto = salario * 0.27


print ("O valor do salário bruto é", salario)
print ("O valor do imposto é ", imposto)
print ("O valor do salário líquido é ", salario - imposto)
