"""En esta función tenemos R que es el máximo de vecs que se puede
repetir un número, también está el dominio que sería num1 y a num2, el ámbito
de las variables num1, num2, es el cuerpo de la función limite"""

def limite(num1, num2, R):

    num1 = num1 * 10 if 1000 <= num1 < 10000 else num1
    num2 = num2 * 10 if 1000 <= num2 < 10000 else num2

    comb = str(num1) + str(num2)
    return all(comb.count(i) <= R for i in set(comb))

"""El dominio de C y R es cualquier número entero, y el ámbito de todas las 
variables definidas dentro de la función generar están limitadas a esa función."""

def generar(C: int, R: int):
    res=[]
    a=1000
    while a*C<100000:
        b=a*C #Regla de divisibilidad
        if limite(b,a,R):
            res += f"{b}/{a}={C}\n"
        a += 1
    return "".join(res)

T = int(input())

casos = [(int(c),int(r)) for _ in range(T) for c,r in [input().split()]]
pruebas = [generar(c[0], c[1]) for c in casos]

i = 0
while i < len(pruebas) - 1:
    print(pruebas[i])
    i += 1
print(pruebas[-1][:-1])

