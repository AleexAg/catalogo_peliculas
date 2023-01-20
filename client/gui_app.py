import tkinter as tk
from tkinter import ttk, messagebox
from model.peliculasDAO import crear_tabla, borrar
from model.peliculasDAO import Peli, guardar, listar, editar, eliminar


def menu_barra(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    #INICIALIZA LA BARRA SUPERIOR
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    menu_consulta = tk.Menu(barra_menu, tearoff=0)

    #BARRA SUPERIOR DEL PROGRAMA
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    barra_menu.add_cascade(label='Consultas', menu=menu_consulta)


    menu_inicio.add_command(label='Crear nuevo registro', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar registro', command=borrar)
    menu_inicio.add_command(label='Salir', command=root.destroy) #CIERRA EL PROGRAMA

    menu_consulta.add_command(label='EJEMPLO 1')
    menu_consulta.add_command(label='EJEMPLO 2')
    menu_consulta.add_command(label='Salir', command=root.destroy) #CIERRA EL PROGRAMA

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.config(width=1080, height=720, bg='#DEF5B6')

        self.id = None

        self.campos_pelis()

        self.desabilitar_c()

        self.tabla_pelis()
    def campos_pelis(self):

        #APARTADOS DEL PROGRAMA

        self.label_name = tk.Label(self, text='Nombre: ')
        self.label_name.config(font=('Arial', 12, 'bold'), bg='#DEF5B6')
        self.label_name.grid(row=0, column=0, padx=10, pady=10)

        self.label_duration = tk.Label(self, text='Duaracion: ')
        self.label_duration.config(font=('Arial', 12, 'bold'), bg='#DEF5B6')
        self.label_duration.grid(row=1, column=0, padx=10, pady=10)

        self.label_gene = tk.Label(self, text='Genero: ')
        self.label_gene.config(font=('Arial', 12, 'bold'), bg='#DEF5B6')
        self.label_gene.grid(row=2, column=0, padx=10, pady=10)

        #ENTRADAS DE CADA CAMPO
        self.mi_nombre = tk.StringVar()

        self.entr_name = tk.Entry(self, textvariable=self.mi_nombre)
        self.entr_name.config(width= 50)
        self.entr_name.config(font=('Arial', 12))
        self.entr_name.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.duracion = tk.StringVar()
        self.entr_dur = tk.Entry(self, textvariable=self.duracion)
        self.entr_dur.config(width=50)
        self.entr_dur.config(font=('Arial', 12))
        self.entr_dur.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.genero = tk.StringVar()
        self.entr_gen = tk.Entry(self, textvariable=self.genero)
        self.entr_gen.config(width=50)
        self.entr_gen.config(font=('Arial', 12))
        self.entr_gen.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        #BOTONES

        self.nuevo_b = tk.Button(self, text='NUEVO', command=self.habilitar_campos)
        self.nuevo_b.config(width=20,
                            font=('Arial', 12, 'bold'),
                            fg='#FFFFFF', bg='#219218',
                            cursor='hand2',
                            activebackground='#33A92A')
        self.nuevo_b.grid(row=4, column=0, padx=10, pady=10)


        self.guardar_b = tk.Button(self, text='GUARDAR', command=self.guardar)
        self.guardar_b.config(width=20,
                             font=('Arial', 12, 'bold'),
                             fg='#FFFFFF', bg='#146BEE',
                             cursor='hand2',
                             activebackground='#3081F9')
        self.guardar_b.grid(row=4, column=1, padx=10, pady=10)



        self.calcel_b = tk.Button(self, text='CANCELAR', command=self.desabilitar_c)
        self.calcel_b.config(width=20,
                            font=('Arial', 12, 'bold'),
                            fg='#FFFFFF', bg='#C60E0E',
                            cursor='hand2',
                            activebackground='#F51A1A')
        self.calcel_b.grid(row=4, column=2, padx=10, pady=10)


    def habilitar_campos(self):
        self.entr_name.config(state='normal')
        self.entr_dur.config(state='normal')
        self.entr_gen.config(state='normal')

        self.guardar_b.config(state='normal')
        self.calcel_b.config(state='normal')

    def desabilitar_c(self):
        self.id = None
        self.mi_nombre.set('')
        self.duracion.set('')
        self.genero.set('')

        self.entr_name.config(state='disabled')
        self.entr_dur.config(state='disabled')
        self.entr_gen.config(state='disabled')

        self.guardar_b.config(state='disabled')
        self.calcel_b.config(state='disabled')

    def guardar(self):

        pelicula = Peli(
            self.mi_nombre.get(),
            self.duracion.get(),
            self.genero.get(),
        )
        if self.id == None:
            guardar(pelicula)
        else:
            editar(pelicula, self.id)


        self.tabla_pelis()
        self.desabilitar_c()


    def tabla_pelis(self):
        self.lista = listar()
        self.lista.reverse()
        self.tabla = ttk.Treeview(self, columns=('NOMBRE', 'DURACION', 'GENERO'))

        ##SCROLLBAR

        self.scroll = ttk.Scrollbar(self,
                                    orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=5, column=4, sticky='nse')
        self.tabla.config(yscrollcommand=self.scroll.set)


        self.tabla.grid(row=5, column=0, columnspan=5, sticky='nse')
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACION')
        self.tabla.heading('#3', text='GENERO')

        for i in self.lista:
            self.tabla.insert('', 0, text=i[0], values=(i[1], i[2], i[3]))


        self.editar = tk.Button(self, text='EDITAR', command=self.editarp)
        self.editar.config(width=20,
                              font=('Arial', 12, 'bold'),
                              fg='#FFFFFF', bg='#146BEE',
                              cursor='hand2',
                              activebackground='#3081F9')
        self.editar.grid(row=6, column=0, padx=10, pady=10)

        self.eliminar_b = tk.Button(self, text='ELIMINAR', command=self.eliminar_pelicula)
        self.eliminar_b.config(width=20,
                             font=('Arial', 12, 'bold'),
                             fg='#FFFFFF', bg='#C60E0E',
                             cursor='hand2',
                             activebackground='#F51A1A')
        self.eliminar_b.grid(row=6, column=2, padx=10, pady=10)


    def editarp(self):
        try:
            self.id = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(
                self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(
                self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(
                self.tabla.selection())['values'][2]
            self.habilitar_campos()

            self.entr_name.insert(0, self.nombre_pelicula)
            self.entr_dur.insert(0, self.duracion_pelicula)
            self.entr_gen.insert(0, self.genero_pelicula)
        except:
            pass

    def eliminar_pelicula(self):

        try:
            self.id = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id)
            self.tabla_pelis()
            self.id = None
        except:
            messagebox.showerror('ELIMINAR', 'ACCION IMPOSIBLE DE REALIZAR')