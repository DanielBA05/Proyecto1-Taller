def limite(num1, num2, R):
    # Añadir ceros si los números tienen 4 dígitos
    num1 = num1 * 10 if 1000 <= num1 < 10000 else num1
    num2 = num2 * 10 if 1000 <= num2 < 10000 else num2

    # Concatenar los números y verificar si algún dígito excede el límite r
    comb = str(num1) + str(num2)
    return all(comb.count(i) <= R for i in set(comb))

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

