print("=== CALCULADORA DE ÍNDICE DE MASA CORPORAL (IMC) ===")

while True:
    nombre = input("Ingresa tu nombre: ").strip()
    if nombre:
        break
    print("Error: El nombre no puede estar vacío.")

while True:
    apellido_paterno = input("Ingresa tu apellido paterno: ").strip()
    if apellido_paterno:
        break
    print("Error: El apellido paterno no puede estar vacío.")

while True:
    apellido_materno = input("Ingresa tu apellido materno: ").strip()
    if apellido_materno:
        break
    print("Error: El apellido materno no puede estar vacío.")

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad > 0:
            break
        print("Error: La edad debe ser mayor que cero.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")

while True:
    try:
        peso = float(input("Ingresa tu peso en kg: "))
        if peso > 0:
            break
        print("Error: El peso debe ser mayor que cero.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")

while True:
    try:
        estatura = float(input("Ingresa tu estatura en metros: "))
        if estatura > 0:
            break
        print("Error: La estatura debe ser mayor que cero.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")

imc = peso / (estatura ** 2)

print("\n===== RESULTADOS =====")
print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad}")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"IMC: {imc:.2f}")
