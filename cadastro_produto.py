import secrets

print("Cadastro de produto")

nome = input("Digite o nome do porduto: ")

preco = input("Digite o preco do produto: ")

categoria = input("Digite a categoria do produto ")

codigo = input("Digite o codigo de barras do produto: ")

estoque = input("Digite a quantidade que será adicionada ao estoque: ")

nome_ot = nome.replace('_',' ').strip()

preco_ot = preco.replace('-','').replace('.', '').replace(',', '')

categoria_ot = categoria.strip()

estoque_ot = estoque.replace('-', '').replace('.', '').strip()

codigo_ot = codigo.replace('-', '').replace('(', '').replace(')', '').replace(' ', '').strip()


def gerar_id(digitos=10):
    
    limite_minimo = 10**(digitos - 1)
    limite_maximo = (10**digitos) - 1

    novo_id = secrets.randbelow(limite_maximo - limite_minimo + 1) + limite_minimo
    
    return novo_id

id_novo = gerar_id()

print("\nCadastro finalizado")


print(f"Nome: {nome_ot}")
print(f"Preco: {preco_ot}")
print(f"Cateogria: {categoria_ot}")
print(f"Estoque: {estoque_ot}")
print(f"Codigo: {codigo_ot}")
print(f"Seu ID é: {id_novo}") 
