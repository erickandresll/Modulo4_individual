import csv
import pickle

# Función para agregar usuarios al archivo CSV

def agregar_usuario(nombre, telefono, edad):
    with open('colaboradores.csv', 'a', newlines='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, telefono, edad])
    print("Usuario agregado exitosamente.")
    
# Función para revisar info de usuarios en el archivo CSV.

def rev_info():
    with open('colaboradores.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader: 
            nombre, telefono, edad = row
            print(f"Nombre: {nombre}, Teléfono: {telefono}, Edad: {edad}")


# Clase para definir nuevo usuario. 

def 