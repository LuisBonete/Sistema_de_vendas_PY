import secrets

print("Cadastro de usuário")

nome = input("Digite seu nome: ")
cpf = input("Digite seu cpf: ")
email = input("Digite seu email: ")
endereco = input("Digite seu endereco: ")
telefone = input("Digite seu telefone: ")



def gerar_id(digitos=10):

 
    limite_minimo = 10**(digitos - 1)
    limite_maximo = (10**digitos) - 1

    novo_id = secrets.randbelow(limite_maximo - limite_minimo + 1) + limite_minimo
   
 
    return novo_id


id_novo = gerar_id()

print("\nCadastro finalizado")

print(f"Nome: {nome}")
print(f"CPF: {cpf}")
print(f"Email: {email}")
print(f"Endereco: {endereco}")
print(f"Telefone: {telefone}")
print(f"Seu ID é: {id_novo}")
