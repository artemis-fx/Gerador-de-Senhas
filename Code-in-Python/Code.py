import random
senha = []
al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w' ,'x' , 'y', 'z']
ce = ['@','#','$','%','*','+']
ns = int(input('Quantos algarimos você quer? '))
for c in range(0, ns):
    senha.append(random.randint(0, 9))
letras = int(input('Quantas letras você quer? '))
for b in range(0, letras):
    senha.append(random.choice(al))
especial = int(input('Quantos caracteres especiais você quer? '))
for e in range(0,especial):
    senha.append(random.choice(ce))
print(f'Sua senha com {ns} algarismo(s),{letras} letra(s) e {especial} caractere(s) especiai(s) é ')
for i in senha:
    print(f'\033[31m{i}\033[m',end='')
