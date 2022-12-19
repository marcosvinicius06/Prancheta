import random
x = ("ate mais")
print("Você quer começar?")
n1 = input()
if n1 == "sim" :
    print("Voce comecou")
    nomo = input("qual o seu nome?")
    idade = input("qual a sua idade?")
    print("--------------")
    print('nome:', nomo)
    print('idade:', idade)
    print("seu numero é:", random.randrange(1, 10))
    print("--------------")
    print(x)
else:
    print(x)
