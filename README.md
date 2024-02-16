# prueba_odoo_prixz



Modulo de prueba técnica
### Tarea 1 : Visualizar el RFC del cliente en el formulario de órdenes de venta
Este siempre debe verse cuando se haga el cambio del cliente
Nota: cuando el cliente no tenga RFC debe tomar el RFC XAXX010101000.

### Tarea 2 : Agregar campos totalizador en entradas de mercancía y accion planificada

Agregar un campo al movimiento (picking) que tenga la cantidad acumulada de lo reservado.

![image](https://github.com/Omejiaprixz/prueba_odoo_prixz/assets/131466302/d02c8738-5dbe-45dc-9178-af9f1f9a12e5)

### Tarea 3 : Consumo de servicios
Agregar un botón en el modulo que se conecte al api de https://fakestoreapi.com/docs
y leer todos los resultados con un print.

Es necesario convertir esta expresión con utilización de python para poder consumir el servicio
Get all products
fetch('https://fakestoreapi.com/products')
            .then(res=>res.json())
            .then(json=>console.log(json))
