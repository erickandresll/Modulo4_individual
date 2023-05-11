class Vendedor:
    def __init__(self, id_vendedor, nombre, departamento):
        self.id_vendedor = id_vendedor
        self.nombre = nombre 
        self.departamento = departamento
        
    def vender(self):
        print("Se han vendido X unidades del producto H")
        
    def anadir_cliente(self):
        print("Se ha añadido correctamente al cliente Juan")
        
    def abrir_caja(self):
        print("Se ha ingresado correctamente el vendedor Juan")
        
class Cliente: 
    def __init__(self, id_cliente, nombre, direccion):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        
    def comprar(self):
        print("Compra aceptada")
        
    def actualizar_datos(self):
        print("Se han actualizado tus datos")
        
    def cotizar(self):
        print("Se a generado una nueva cotización N°1234")
        
class Administrador: 
    def __init__(self, run, nombre, sucursal):
        self.run = run
        self.nombre = nombre
        self.sucursal = sucursal
    
    def actualizar_stock(self):
        print("Se ha actualizar el producto X")
        
    def ingresar_vendedor(self):
        print("Se ha ingresado correctamente el vendedor")
        
    def comprar_producto(self):
        print("Se a generado nueva orden de compra")
        

