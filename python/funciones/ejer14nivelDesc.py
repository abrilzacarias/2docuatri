def sueldoF(pNivel,pSB):
    descuentos= pSB*0.12
    sueldoCDescuentos= pSB-descuentos
    if (pNivel==2) or (pNivel==3):
        desc23= pSB*0.11
        descuentos+=desc23
        sueldoCDescuentos-=desc23
    
    if nivel==1:
        bono=20000
    elif nivel==2:
        bono=30000
    elif nivel==3:
        bono=40000
    else:
        return "Nivel seleccionado incorrecto"

    if (nivel==1) or (nivel==2) or (nivel==3):
        descFinales=descuentos
        sueldoFinal=sueldoCDescuentos+bono
        return f"Descuentos: ${descFinales} \nTotal a pagar: ${sueldoFinal} " 

empleados = 8

for empleado in range(1,empleados+1):
    nivel=int(input(f"Ingrese el nivel(1, 2 o 3) del empleado {empleado}: "))
    SB=float(input(f"Ingrese el sueldo base del empleado {empleado}: "))
    print(sueldoF(nivel,SB))