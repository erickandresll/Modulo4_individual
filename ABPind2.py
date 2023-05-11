class Vendedor:
    def __init__(self, id_vendedor, nombre, apellido, departamento):
        self.id_vendedor = id_vendedor
        self.nombre = nombre 
        self.apellido = apellido
        self.departamento = departamento
        self.ventas = [] #Lista para registrar la venta.
        self.clientes = [] #Lista para registrar clientes.
        
    #Se añade el monto de la venta y cliente a las listas.    
    def vender(self, cliente, monto):
        self.ventas.append(monto)
        if cliente not in self.clientes:
            self.clientes.append(cliente)
    
    #Se registra el cliente.        
    def registrar_cliente(self, cliente):
        if cliente not in self.clientes:
            self.clientes.append(cliente)
    
    #Se visualiza el número de ventas realizadas por el vendendor.    
    def reporte_ventas(self):
        return len(self.ventas)
    
    #Devuelve el monto total de las ventas.             
    def monto_ventas(self):
        return sum(self.ventas) 
    
class Cliente: 
    def __init__(self, id_cliente, nombre, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.compras = [] #Lista para registrar compras del cliente.
        self.cotizaciones = [] #Lista para registrar cotizaciones del cliente.
    
    #Añade el monto de la compra.    
    def comprar(self, monto):
        self.compras.append(monto)
    
    #Actualiza correo del cliente.     
    def actualizar_correo(self, nuevo_correo):
        self.correo = nuevo_correo
    
    #Añade la cotización a la lista de cotizaciones.    
    def solicitar_cotizacion(self, producto, precio):
        self.cotizaciones.append((producto, precio))
    
    #El cliente puede revisar el monto total de las compras realizadas.    
    def saldo_actual(self):
        return sum(self.compras)

class Administrador: 
    def __init__(self, run, nombre, sucursal):
        self.run = run
        self.nombre = nombre
        self.sucursal = sucursal
        self.vendedores = []
        self.stock = {}
        self.saldo_caja = 0
     
    #Revisa si el producto ya existe, actualiza, sino añade el producto y la cantidad.     
    def actualizar_stock(self, producto, cantidad):
        if producto in self.stock:
            self.stock[producto] += cantidad 
        else:
            self.stock[producto] = cantidad
    
    #Ingresa vendedor nuevo.
    def ingresar_vendedor(self, vendedor):
        self.vendedores.append(vendedor)    

    # Calcula el total de productos, revisa si hay stock, actualiza cantidad nueva.
    def comprar_productos(self, productos):
        total = sum(productos,values())
        for producto, cantidad in productos.items():
            if producto in self.stock:
                self.stock[producto] += cantidad
            else:
                self.stock[producto] = cantidad
        self.obtener_saldo_caja -= total 
    
    #Revisa el saldo en caja.    
    def saldo_caja(self):
        return self.saldo_caja
               
class Bodega:
    def __init__(self, sku, producto, cantidad, tipo_producto=None):
        self.sku = sku
        self.producto = producto
        self.cantidad = cantidad
        self.tipo_producto = tipo_producto
        self.proveedores = []
        
    #Ingresa nuevo stock de productos. 
    def ingresar_productos(self, cantidad):
        self.cantidad += cantidad 
       
    #Elimina stock de producto validando que no sea mayor a lo que tiene en stock.
    def eliminar_cantidad(self, cantidad):
        if cantidad > self.cantidad:
            print("La cantidad a eliminar es mayor.")
        else:
            self.cantidad -= cantidad
    
    #Agrega proveedor.
    def agregar_proveedor(self, proveedor):
        self.proveedores.append(proveedor)
        

       