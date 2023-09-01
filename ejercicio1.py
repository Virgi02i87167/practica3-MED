def obtenerMes(num):
            mes = (
                "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
            )
            if 1 <= num <= 12:
                nombremes = mes[num - 1]
                return nombremes
            else:
                return "El mes no existe"

numeroMes = int(input("Ingresa un mes: "))
nombreMes = obtenerMes(numeroMes)
print("El mes correspondiente es:", nombreMes)