def acha_maior(lista):
    maior = lista[0]
    indice_maior = 0

    for i in range (len(lista)):
        print(f"Agora vou testar se lista [{i}], ou seja, {lista[i]}>{maior}")
        if lista[i] > maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior

def acha_menor(lista):
    menor = lista[0]
    indice_menor = 0
    for i in range (len(lista)):
        print(f"Agora vou testar se lista [{i}], ou seja, {lista[i]}<{menor}")
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i
    return indice_menor
        
precos = [100, 150, 1000, 200, 300]
carros = ["up", "fusca", "celta", "ka", "corsinha"]
local_maior = acha_maior(precos)

print(f"No fim o mais caro é {carros[local_maior]} e custa {precos[local_maior]}")

x = -10
lista_x = []
lista_f = []
while x < 10:
    f = 2 * (x ** 2) + 4 / x
    lista_f.append(f)
    lista_x.append(x)
    x += 0.1
local_menor = acha_menor(lista_f)
print(f'0 yv = {lista_f[local_menor]} e o xv = {lista_x[local_menor]}')
import matplotlib.pyplot as plt
plt.plot(lista_x, lista_f,"bo")
plt.grid()
plt.show()
        