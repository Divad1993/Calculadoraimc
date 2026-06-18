print("=== CALCULADORA DE ÍNDICE DE MASA CORPORAL (IMC) ===")

# Validar nombre
while True:
    nombre = input("Ingresa tu nombre: ").strip()
    if nombre:
        break
    print("Error: El nombre no puede estar vacío.")

# Validar apellido paterno
while True:
    apellido_paterno = input("Ingresa tu apellido paterno: ").strip()
    if apellido_paterno:
        break
    print("Error: El apellido paterno no puede estar vacío.")

# Validar apellido materno
while True:
    apellido_materno = input("Ingresa tu apellido materno: ").strip()
    if apellido_materno:
        break
    print("Error: El apellido materno no puede estar vacío.")

# Validar edad
while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad > 0:
            break
        print("Error: La edad debe ser mayor que cero.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")

# Validar peso
while True:
    try:
        peso = float(input("Ingresa tu peso en kilogramos: "))
        if peso > 0:
            break
        print("Error: El peso debe ser mayor que cero.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")

# Validar estatura
while True:
    try:
        estatura = float(input("Ingresa tu estatura en metros: "))
        if estatura > 0:
            break
        print("Error: La estatura debe ser mayor que cero.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")

# Calcular IMC
imc = peso / (estatura ** 2)

# Mostrar resultados
print("\n===== RESULTADOS =====")
print(f"Nombre completo: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} m")
print(f"Índice de Masa Corporal (IMC): {imc:.2f}")
