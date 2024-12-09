def calcular_salario(horas_trabajadas, tarifa):
    if horas_trabajadas > 40:
        horas_normales = 40
        horas_extras = horas_trabajadas - 40
        salario = (horas_normales * tarifa) + (horas_extras * tarifa * 2.5)
    else:
        salario = horas_trabajadas * tarifa
    return salario

horas_trabajadas = float(input("Introduce las horas trabajadas: "))
tarifa = float(input("Introduce la tarifa por hora: "))

salario = calcular_salario(horas_trabajadas, tarifa)

print(f"El salario total del trabajador es: ${salario:.3f}")
