nombre = input("Ingrese su nombre: ")
dias = int(input("Ingrese la cantidad de dias: "))
salario = int(input("Ingrese el salario: "))
Prima = (salario * dias) / 360
Cesantias = (salario * dias) / 360
Intereses_cesantias = Cesantias * 0.12 / dias
Vacaciones = (salario * dias) / 720


def calcularLiquidacion():
    liquidacion = (Prima + Cesantias + Intereses_cesantias + Vacaciones)
    return liquidacion


print(f"Señor {nombre} para los {dias} dias laborados y salario {salario}, su liquidacion se compone asi: \n"
      f"Prima: ${Prima:.2f} \n"
f"Cesantias: ${Cesantias:.2f} \n"
f"Intereses cesantias: ${Intereses_cesantias:.2f} \n"
f"vacaiones: ${Vacaciones:.2f} \n"
f"luqidacion: ${calcularLiquidacion():.2f}")
