dados = ('João', 'Analista', 4000.00, 'Pedro', 'Vendedor', 2500.00)


for i in range(0, len(dados), 3):
    nome = dados[i]
    cargo = dados[i + 1]
    print(f"Nome: {nome}, Cargo: {cargo}")
