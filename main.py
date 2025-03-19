## Voy a ganar este examen 
helados = []  # Lista para almacenar los helados
contador_id = 1  # Contador para asignar IDs únicos (NO reiniciarlo dentro del bucle)

while True:
    print("\nGestión de Helados")
    print("1. Agregar un helado")
    print("2. Ver lista de helados")
    print("3. Modificar un helado")
    print("4. Eliminar un helado")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":  # Agregar un helado
        nombre = input("Ingrese el nombre del helado: ")
        descripcion = input("Ingrese la descripción del helado: ")
        precio = input("Ingrese el precio del helado: ")

        if precio.isdigit():  # Solo permite números enteros
            precio = int(precio)  # Convertimos a entero
            helado = {"id": contador_id, "nombre": nombre, "descripcion": descripcion, "precio": precio}
            helados.append(helado)  # Se usa la variable correcta
            contador_id += 1  # Incrementamos correctamente el ID
            print("Helado agregado correctamente.")
        else:
            print("Error: El precio debe ser un número entero.")

    elif opcion == "2":  # Ver lista de helados
        if len(helados) == 0:  # Se usa la variable correcta
            print("No hay helados registrados.")
        else:
            print("\nLista de Helados:")
            for helado in helados:
                print("ID:", helado["id"], ", Nombre:", helado["nombre"], ", Descripción:", helado["descripcion"], ", Precio: $", helado["precio"])

    elif opcion == "3":  # Modificar un helado
        id_modificar = input("Ingrese el ID del helado a modificar: ")
        
        if id_modificar.isdigit():
            id_modificar = int(id_modificar)
            encontrado = False
            
            for helado in helados:
                if helado["id"] == id_modificar:
                    nuevo_nombre = input("Nuevo nombre (deje en blanco para no cambiar): ")
                    nueva_descripcion = input("Nueva descripción (deje en blanco para no cambiar): ")
                    nuevo_precio = input("Nuevo precio (deje en blanco para no cambiar, sin decimales): ")
                    
                    if nuevo_nombre:
                        helado["nombre"] = nuevo_nombre
                    if nueva_descripcion:
                        helado["descripcion"] = nueva_descripcion
                    if nuevo_precio.isdigit():  # Solo números enteros
                        helado["precio"] = int(nuevo_precio)
                    
                    print("Helado modificado correctamente.")
                    encontrado = True
                    break
            
            if not encontrado:
                print("Error: No se encontró un helado con ese ID.")
        else:
            print("Error: El ID debe ser un número.")

    elif opcion == "4":  # Eliminar un helado
        id_eliminar = input("Ingrese el ID del helado a eliminar: ")
        
        if id_eliminar.isdigit():
            id_eliminar = int(id_eliminar)
            encontrado = False
            
            for helado in helados:
                if helado["id"] == id_eliminar:
                    helados.remove(helado)  # Se usa la variable correcta
                    print("Helado eliminado correctamente.")
                    encontrado = True
                    break
            
            if not encontrado:
                print("Error: No se encontró un helado con ese ID.")
        else:
            print("Error: El ID debe ser un número.")

    elif opcion == "5":  # Salir
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente nuevamente.")