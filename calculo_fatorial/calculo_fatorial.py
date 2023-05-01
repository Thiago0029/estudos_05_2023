#caluclando o fatorial

num = int(input("Informe número para calculo de fatorial: "))

fat = 1
while num >= 1:
    fat = fat * num
    num -=1

print(fat)