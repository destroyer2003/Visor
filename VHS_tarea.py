#muak que buapa
n = 0

print("¿Cuántos alumnos son?")
n = int(input())
vn = ["" for _ in range(n)]
vp = [0.0 for _ in range(n)]

for i in range(n):
    print("¿Cuál es el nombre del alumno", i + 1, "?")
    vn[i] = input()
    print("¿Cuál es el promedio del alumno", vn[i], "?")
    vp[i] = float(input())

for i in range(n):
    for j in range(n):
        if vp[j] < vp[i]:
            # PA = promedio auxiliar, NA = nombre auxiliar
            pa = vp[i]
            na = vn[i]
            vp[i] = vp[j]
            vn[i] = vn[j]
            vp[j] = pa
            vn[j] = na

for i in range(n):
    print("Nombre del alumno:", vn[i])
    print("Promedio:", vp[i])