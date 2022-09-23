fi = 1000.00
co = 200.00
ad = 5/100

vendedor = input('Nome do vndedor: ')
n_carro = int(input('Quantidade de carros vendidos: '))

total_v= co * n_carro

salario = (fi + total_v) + total_v * ad

print(f'Vendedor {vendedor} vendeu {n_carro} carros e vai reseber {total_v} de variavel mais 5% por venda')
print(f'Salario fixo {fi}')
print(f'Total a reseber no mês {salario}')