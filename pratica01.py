produto = {
    'nome': 'notebook',
    'preco': 3500.00,
    'estoque': 15
}

del produto['estoque']

produto['preco'] = 4000.00

print(f"Nome: {produto['nome']}, Preço: R${produto['preco']:,.2f}")