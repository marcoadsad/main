
#valores bases
total_usuarios = 0
suma_edades = 0

while True:
    # Imprimir el menú tal como viene en el ejemplo
    print("\n1.- Ingresar usuario y contraseña.")
    print("2.- Calcular edad promedio.")
    print("3.- Salir.")
    
    opcion = input("Seleccione opción: ")
    
    if opcion == "1":
        if total_usuarios >= 3:
            print("No se pueden ingresar más usuarios.")
        else:
            nombre = input("Ingrese nombre de usuario: ")
            
            # Bucle exclusivo para validar la edad
            while True:
                try:
                    edad_texto = input("Ingrese edad del usuario: ")
                    
                    # Si el usuario mete un punto obligamos a que falle
                    if "." in edad_texto:
                        int("forzar_error") 
                        
                    edad = int(edad_texto) # Intentamos convertir a número entero
                    # Si todo sale bien, sumamos y pasamos al siguiente usuario
                    suma_edades += edad
                    total_usuarios += 1
                    break # Rompe el bucle de la edad
                    
                except ValueError: # Si no es un entero, atrapa el error aquí
                    print("Debe ingresar la edad como numero entero.")
                    print("Inténtelo nuevamente.")
                    
    elif opcion == "2":
        if total_usuarios == 0:
            print("No es posible calcular promedio.")
        else:
            promedio = suma_edades / total_usuarios
            print(f"La edad promedio de los usuarios es: {promedio:.1f}")
            
    elif opcion == "3":
        break # Termina el programa
        
    else:
        print("Seleccione una opción válida.")