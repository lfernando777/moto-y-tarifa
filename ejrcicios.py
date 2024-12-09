def calcular_precio(precio_original, dia, es_feriado=False):
    
    if es_feriado:
        descuento = 0.25  
    else:
        
        if dia.lower() == "martes":
            descuento = 0.12  
        elif dia.lower() == "sabado":
            descuento = 0.18
             
        else:
            descuento = 0  

    precio_con_descuento = precio_original * (1 - descuento)
    return precio_con_descuento

precio_original = float(input("Introduce el precio de la moto: "))


dia = input("Introduce el día de la compra (martes, sábado, otro): ")
es_feriado = input("¿Es feriado? (sí/no): ").lower() == "sí"

precio_martes = calcular_precio(precio_original, "martes", es_feriado)
precio_sabado = calcular_precio(precio_original, "sabado", es_feriado)
precio_feriado = calcular_precio(precio_original, "otro", True)  # Si es feriado aplica el 25%

# Mostrar los resultados
print(f"Si compras el día martes, pagarás: ${precio_martes:.2f}")
print(f"Si compras el día sábado, pagarás: ${precio_sabado:.2f}")
print(f"Si es feriado, pagarás: ${precio_feriado:.2f}")


