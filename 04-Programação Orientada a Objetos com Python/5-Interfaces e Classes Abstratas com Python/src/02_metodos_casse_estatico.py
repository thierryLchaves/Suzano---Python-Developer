# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# Itera sobre cada item no carrinho para exibi-lo
for item, preco in carrinho:
    # Imprime o item e o preço formatado com 2 casas decimais
    print(f"{item}: R${preco:.2f}")

# Imprime o total da compra, também formatado com 2 casas decimais
print(f"Total: R${total:.2f}")


