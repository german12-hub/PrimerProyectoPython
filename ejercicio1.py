# ejercicio1.py
# Variables personales y cálculo de años hasta los 50

# --- Datos (editar con tus datos) ---
nombre = "Germán"
edad = 32
ciudad = "Buenos Aires"

# --- Calculo ---
objetivo = 50
años_faltantes = objetivo - edad

# --- Salida --
# Usamos f-strings (forma limpia de formatear texto en Python)
print(f"Hola, soy {nombre}, tengo {edad} años y vivo en {ciudad}.")

if años_faltantes > 0:
    print(f"Me faltan {años_faltantes} años para cumplir {objetivo}.")
elif años_faltantes == 0:
    print(f"¡Hoy cumplís {objetivo} años! Feliz cumpleaños 🥳")
else:
    # Si ya pasaste los 50
    print(f"Ya pasaste los {objetivo} por {-años_faltantes} años. ¡Qué genio!")
