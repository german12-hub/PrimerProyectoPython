#Pida al usuario su edad con input().
#Si es menor de 18, muestre "Sos menor de edad.".
#Si está entre 18 y 65, muestre "Sos adulto.".
#Si tiene más de 65, muestre "Sos adulto mayor.".

try:
    edad = int(input("Ingresa tu edad: "))
    if edad >= 66:
        print("Sos adulto mayor")
    elif edad >= 18:
        print("Sos adulto")
    else:
        print("Sos menor de edad")
except ValueError:
    print("Por favor ingresá un número válido")