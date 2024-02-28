from controller import obtenerMenu, agregar, mostrarContrato, mostrarContratos, modificarEstado, buscarEstado

contratos=[]
seguir=True

while seguir:
    opcion=obtenerMenu()
    match opcion:
        case 1:
            agregar(contratos)
        case 2:
            mostrarContratos(contratos)
        case 3:
            mostrarContrato(contratos)
        case 4: 
            buscarEstado(contratos)
        case 5:
            modificarEstado(contratos)
        case 6:
            print("HASTA PRONTO")
            seguir=False
        case default:
            print("Ingrese una opcion valida")
            
            
            
