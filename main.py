import dataset
miBase = dataset.connect("sqlite:///datos.db")
tabla = miBase["Productos"]




def listar():
    print("*********** Listado de productos *****************")
    for cada_item inimport dataset
miBase = dataset.connect("sqlite:///base.db")
tabla = miBase["Productos"]

while True:
    opciones = input("\nA - Agregar\nL - Listar\nS - Salir\nBT - Buscar en toda la base:\nR - Remover por nombre\nID - Borrar por ID\n").upper()

    match opciones:

        case "A":
            agregarProducto = input("\nProducto: ").strip()
            agregarPrecio = float(input("\nPrecio: ").strip())
            agregarCategoria = input("\nCategoria: ").strip()

            agregar = {"Nombre":agregarProducto,"Precio":agregarPrecio,"Categoria":agregarCategoria}

            tabla.insert(agregar)

        case "S":
            break
        
        case "L":
            for items in tabla:
                print(f'ID:{items["id"]} | Producto: {items["Nombre"]} | Precio: {items["Precio"]} | Categoria: {items["Categoria"]}')
                
        case "R":
            removerNombre = input("\nProducto a remover: ").strip()
            
            tabla.delete(Nombre=removerNombre)
            
            print(f"\n{removerNombre} se ha quitado con exito!\n")
         
        case "ID":
            borrarID = int(input("\nID de prod. a borrar: ").strip())
            tabla.delete(id=borrarID)
            
            print(f"\nEl producto cuyo ID es {borrarID} fue quitado con exito!!!\n")
               
        case "AC":
            idBuscar = int(input("\nID a actualizar: "))
            
            nombreActualizar = input("\nNombre nuevo: ")
            precioActualizar = float(input("\nprecio nuevo: "))
            catActualizar = input("\nCategoria nueva: ")
            
            actualizar = {"id":idBuscar,"Nombre":nombreActualizar, "Precio":precioActualizar,"Categoria":catActualizar}
            tabla.upsert(actualizar,["id"])
        
        case "BT":
            buscarTodo = input("\nProducto a buscar: ")
            
            encontrados = tabla.find(Nombre=buscarTodo)
            
            for encontrado in encontrados:
                print(f'{encontrado["Nombre"]} Se encontró en ID: {encontrado["id"]}')
            
             tabla:
        print(f'ID: {cada_item["id"]} | Producto: {cada_item["Nombre"]} | Precio: {cada_item["Precio"]} | Categoria: {cada_item["Categoria"]} ')
    
