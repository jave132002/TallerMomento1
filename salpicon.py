frutas = []

print("\nGestion de frutas pal salpicon")
for i in range(1, 11):
    print(f"\nIngrese la fruta N°: {i} de 10")
    
    while True:
        nombre = input("Ingrese el nombre de la fruta: ")
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("Pilas, El nombre solo debe contener letras.")

    while True:        
        precio = input("Digite el valor de la fruta: ").replace('.', '')
        if precio.replace(',', '.', 1).isdigit():
            precio = float(precio.replace(',', '.'))
            break
        else:
            print("Ha ocurrido un Error, Precio invalido.")

    # Se agrega la fruta a la lista
    fruta = {"nombre": nombre, "precio": precio}
    frutas.append(fruta)     

    print("=" * 40)
# Ordenar frutas después de agregar todas
frutas_ordenadas = sorted(frutas, key=lambda x: x["precio"], reverse=True)

# Mostrar frutas ordenadas al final
print("\n" + "=" * 40)
print("\nFrutas ordenadas de mayor a menor precio:")
print("=" * 40)
for fruta in frutas_ordenadas:
    print(f"Nombre: {fruta['nombre']}, Precio: ${fruta['precio']:.2f}")

total = sum(fruta["precio"] for fruta in frutas_ordenadas)

print("\n" + "=" * 40)
print(f"Total para el Salpicon: ${total:,.2f}")
print("=" * 40)
print("Estamos listos para el Salpicon 🍹")