import random

print("----PAGAMENTO----")

forma = input("Digite a sua froma de pagamento: ")
hora = input("Digite o horario que voce está realzando o pagamento:")
data = input("Digite a data que voce está realizando o seu pagamento")

preco = random.randint(1,100)

id_pagamento = random.randint(1,100)

print("Dados do pagamento ")

print(f"Metodo de pagamento",{forma})
print(f"Hora que realizou o pagamento",{hora})
print(f"Data que realizou o pagameto",{data})
print("Valor pago ",{preco})
print("id do seu oagamento",{id_pagamento})

