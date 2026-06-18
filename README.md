# Calculadora de IMC

# Validar texto
def pedir_texto(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato:
            return dato
        print("Error: este campo no puede estar vacío.")

# Validar número entero
def pedir_entero(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit():
            return int(dato)
        print("Error: ingresa un número válido.")

# Validar número decimal
def pedir_decimal(mensaje):
    while True:
        try:
            dato = float(input(mensaje).strip())
            return dato
        except ValueError:
            print("Error: ingresa un número válido.")

# Captura de datos
nombre = pedir_texto("Nombre: ")
apellido_paterno = pedir_texto("Apellido paterno: ")
apellido_materno = pedir_texto("Apellido materno: ")
edad = pedir_entero("Edad: ")
peso = pedir_decimal("Peso en kg: ")
estatura = pedir_decimal("Estatura en metros: ")

# Cálculo del IMC
imc = peso / (estatura ** 2)

# Resultados
print("\n----- DATOS DEL USUARIO -----")
print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"IMC: {imc:.2f}")
