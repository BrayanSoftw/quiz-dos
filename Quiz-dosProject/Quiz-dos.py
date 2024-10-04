#Nombre: Luis Vejarano
#Días: 7
#Salario: 785000
#Prima: salario x días laborados / 360
#Cesantías: salario x días laborados / 360
#Intereses cesantías: cesantías x 12% / días laborados
#Vacaciones: salario x días laborados / 720


#nombre = input('Ingrese su nombre: ')
#dias = int(input('Ingrese la cantidad de dias: '))
#salario = int(input('Ingrese el salario: '))
nombre='Luis'
dia=7
salario = 785000
prima = (salario*dia)/360
def calcularSalario(salario,dia):
    #dia = 7
    #prima = (dia*salario)/360
    #return prima
    #prima = calcularSalario(salario,dias)
    #print('prima: ' +prima)
    #print('cesantias: ' + prima)
    #print('intereses: ' + prima)
    prima = calcularSalario(salario,dia)
    print('prima: ' + prima)
calcularSalario (prima)