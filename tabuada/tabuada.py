#script para geração de tabuada

print("Famos criar uma tabuado")

num = int(input("Infome um numero para gerar uma tabuada: "))

#usando um while pois e um script bem básico

i = 0

while i <=10:
    ta = num * i
    print(num, " X ",+i, " = ",+ta)
    i+=1