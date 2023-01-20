from .conexionDB import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE peliculas(
    id INTEGER,
    nombre VARCHAR(25),
    duracion VARCHAR(10),
    genero VARCHAR(25),
    PRIMARY KEY(id AUTOINCREMENT)
    )
    
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        title = 'Crear Registro'
        mensage = 'El registro se creo corrrectamente'

        messagebox.showinfo(title, mensage)
    except:
        title = 'Crear Registro'
        mensage = 'Ya existe una tabla'

        messagebox.showwarning(title, mensage)

def borrar():
    conexion = ConexionDB()

    sql = 'DROP TABLE peliculas'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        title = 'Borrar Registro'
        mensage = 'El registro se borro corrrectamente'

        messagebox.showinfo(title, mensage)
    except:
        title = 'Borrar Registro'
        mensage = 'No existe ningun registro actualmente'

        messagebox.showerror(title, mensage)


class Peli:
    def __init__(self, nombre, duracion, genero):
        self.id = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero


    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'


def guardar(pelicula):
    conexion = ConexionDB()

    sql = f"""INSERT INTO peliculas (nombre, duracion, genero) VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion con el registro'
        mensaje = 'El Registro aun no fue creado'

        messagebox.showerror(titulo, mensaje)


def listar():
    conexion = ConexionDB()

    list = []

    sql = 'SELECT * FROM peliculas'

    try:
        conexion.cursor.execute(sql)
        list = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        tile = 'Listado de peliculas'
        mensaje = 'El registro aun no fue creado'
        messagebox.showinfo(tile, mensaje)
    return list


def editar(pelicula, id):
    conexion = ConexionDB()

    sql = f"""UPDATE peliculas
    SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}', genero = '{pelicula.genero}'
    WHERE id = {id}
    """

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        title= 'error'
        mensaje = 'Accion imposible de realizar'
        messagebox.showerror(title, mensaje)


def eliminar(id):
    conexion = ConexionDB()

    sql = f'DELETE FROM peliculas WHERE id = {id}'

    conexion.cursor.execute(sql)
    conexion.cerrar()