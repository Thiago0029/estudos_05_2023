#Script para verificar se numero é par ou impar

print("vamos verificar se número e impar ou par")

n = int(input("Digite um numero: "))

if n%2 == 0:
    print("Par")
    
elif n%2 !=0:
    print("Impar")

else:
    print("Erro de calculo")