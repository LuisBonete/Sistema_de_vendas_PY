import secrets

print("Cadastro de fornecedores")
print("Por favor digite o nome do fornecedor")
nome = input("Digite o nome: ")
print("Por favor digite o CNPJ (999.999.999/0001-99")
cpf = input("Digite o CNPJ: ")
print("Digite o email (usario@gmail.com)")
email = input("Digite o email: ")
print("Por favor digite o endereço")
endereco = input("Digite o endereco: ")
print("Digite o telefone (41)99999-9999")
telefone = input("Digite o telefone: ")

nome_ot = nome.replace('_',' ').strip()

cpf_ot = cpf.replace('-','').replace('.', '').replace('/', '').strip

email_ot = email.strip()

endereco_ot = endereco.replace('-', '').strip()

telefone_ot = telefone.replace('-', '').replace('(', '').replace(')', '').replace(' ', '').strip()


def gerar_id(digitos=10):
    
    limite_minimo = 10**(digitos - 1)
    limite_maximo = (10**digitos) - 1

    novo_id = secrets.randbelow(limite_maximo - limite_minimo + 1) + limite_minimo
    
    return novo_id

id_novo = gerar_id()

print("\nCadastro finalizado")


print(f"Nome: {nome_ot}")
print(f"CPF: {cpf_ot}")
print(f"Email: {email_ot}")
print(f"Endereco: {endereco_ot}")
print(f"Telefone: {telefone_ot}")
print(f"Seu ID é: {id_novo}") # Usando 'id_novo' que foi definida
