import dataset  

miBase = dataset.connect("sqlite:///datos.db")  # Conecta o crea si no existe la base de datos datos.db
tabla = miBase["Productos"]  # crea automáticamente una tabla si no existe.

while True:  

    opciones = input ("""
    L - LISTAR
    A - AGREGAR
    Q - QUITAR POR NOMBRE
    I - QUITAR POR ID
    B - BUSCAR PRIMERO
    T - BUSCAR TODO 
    S - SALIR """).strip().upper() #transformo las letras en mayuculas o quito espacios.Menú y guarda la opción elegida por el usuario

    match opciones:  

        case "B":  

            busco = input("\nProducto a buscar: ").strip()  
            encontrado = tabla.find_one(Nombre=busco)  
            print(f'{busco} esta en la posicion {encontrado["id"]}')  

        case "T":  # Buscar todos los productos con ese nombre

            busco = input("\nBuscar en toda la base: ").strip()  
            encontrado = tabla.find(Nombre=busco)  
            for cosa in encontrado: 
                print(f'{busco} esta en el ID: {cosa["id"]}')  

        case "S":  # Salir del programa

            break  

        case "A":  

            nombreProducto = input("\nNombre: ")  
            precioProducto = float(input("\nPrecio: ")) 
            categoriaProducto = input("\nCategoría: ") 
            productoAgregar = {"Nombre": nombreProducto, "Precio": precioProducto, "Categoria": categoriaProducto}  # Crea un diccionario con los datos del producto
            tabla.insert(productoAgregar)  # Inserta el diccionario como un nuevo registro en la tabla

        case "L":  # Listar todos los productos

            for cosa in tabla:  # Recorre cada registro de la tabla
                print(f"ID: {cosa['id']} | ","\n", f"Nombre: {cosa['Nombre']} | ","\n",f"Precio: {cosa['Precio']} | ","\n",f"Categoria: {cosa['Categoria']}")  
        
        case "Q":  # Eliminar productos por nombre

            quitarProducto = input("\nProducto a quitar: ")  
            tabla.delete(Nombre=quitarProducto)  
            print(f"--- {quitarProducto} eliminado con éxito--- ")  

        case "I":  # Eliminar un producto por ID

            quitarProducto = int(input("\nId de producto a quitar: ")) 
            tabla.delete(id=quitarProducto)  
            print(f" ----Producto con ID: {quitarProducto} eliminado con éxito---- ") 
