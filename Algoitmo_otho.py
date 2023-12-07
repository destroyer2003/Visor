#y la que soporte guapa
C = 0
SU = 0
CO = 0
CN = 0
VT = 0
VTT = 0

S = int(input("En cuántas ciudades tiene sucursales? "))
while C < S:
    print("¿Cuántas sucursales tiene la ciudad?")
    T = int(input())
    while CO < T:
        print("¿Cuántos empleados tiene?")
        N = int(input())
        while CN < N:
            print("¿Cuánto fue de la venta?")
            V = float(input())
            CN += 1
            SU += V
        CO += 1
        CN = 0
        VT += SU
        VTT += SU
        print("El total de venta por esta sucursal es: $", SU)
        SU = 0
    print("El total de venta por esta ciudad es: $", VTT)
    CO = 0
    C += 1
    VTT = 0

print("El total de venta por día es: $", VT)
