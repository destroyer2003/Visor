#no se te olvide quitar los primeros comentarios xd
n = 10
v = [0] * n
SU = 0

for i in range(1, n + 1):
    print("Ingresar el número")
    v[i - 1] = int(input())
    SU = SU + v[i - 1]

print("El número 2 es:", v[1])
print("El número 4 es:", v[3])
print("La suma de los números es:", SU)