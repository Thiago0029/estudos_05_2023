# somando os valores de uma lista numerica

op = 'c'
soma = []

while op =='c' or op =='C':
    soma = int(input("Infomre um numero: "))
    op = input("digite c para continuar: ")

for i in soma:
    soma +=i

print(soma)