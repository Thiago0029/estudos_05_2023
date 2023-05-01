# somando os valores de uma lista numerica

soma = []
op = 'c'
while op == 'c' or op == 'C':
    soma = int(input("Infomre um numero: "))
    op = input("Continuar? ")
    
for i in soma:
    somatoria = i + i

print(somatoria)