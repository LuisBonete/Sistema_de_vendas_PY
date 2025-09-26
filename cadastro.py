import secrets

print("Cadastro de usuário")
print("Por favor digite o seu nome")
nome = input("Digite seu nome: ")
print("Por faor digite o seu CPF (999.999.999-99")
cpf = input("Digite seu cpf: ")
print("Digite o seu email (usario@gmail.com)")
email = input("Digite seu email: ")
print("Por favor digite seu endereço")
endereco = input("Digite seu endereco: ")
print("Digite seu telefone (41)99999-9999")
telefone = input("Digite seu telefone: ")

nome_ot = nome.replace('_',' ').strip()

cpf_ot = cpf.replace('-','').replace('.', '')

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
