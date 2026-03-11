import tkinter as tk
from tkinter import ttk
from modelos.vehiculo import 
from servicios.garaje_servicio import GarajeServicio


class AppGaraje:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Garaje")
        self.ventana.geometry("500x400")

        self.servicio = GarajeServicio()

        self.crear_componentes()

    def crear_componentes(self):

        titulo = tk.Label(self.ventana, text="Sistema de Garaje", font=("Arial", 18))
        titulo.pack(pady=10)

        frame_form = tk.Frame(self.ventana)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Placa").grid(row=0, column=0, padx=5, pady=5)
        self.txt_placa = tk.Entry(frame_form)
        self.txt_placa.grid(row=0, column=1)

        tk.Label(frame_form, text="Marca").grid(row=1, column=0, padx=5, pady=5)
        self.txt_marca = tk.Entry(frame_form)
        self.txt_marca.grid(row=1, column=1)

        tk.Label(frame_form, text="Propietario").grid(row=2, column=0, padx=5, pady=5)
        self.txt_propietario = tk.Entry(frame_form)
        self.txt_propietario.grid(row=2, column=1)

        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        btn_agregar = tk.Button(frame_botones, text="Registrar Vehículo", command=self.registrar_vehiculo)
        btn_agregar.grid(row=0, column=0, padx=10)

        btn_limpiar = tk.Button(frame_botones, text="Limpiar Campos", command=self.limpiar)
        btn_limpiar.grid(row=0, column=1, padx=10)

        self.tabla = ttk.Treeview(self.ventana, columns=("Placa", "Marca", "Propietario"), show="headings")

        self.tabla.heading("Placa", text="Placa")
        self.tabla.heading("Marca", text="Marca")
        self.tabla.heading("Propietario", text="Propietario")

        self.tabla.pack(pady=15)

    def registrar_vehiculo(self):

        placa = self.txt_placa.get()
        marca = self.txt_marca.get()
        propietario = self.txt_propietario.get()

        if placa == "" or marca == "" or propietario == "":
            return

        vehiculo = Vehiculo(placa, marca, propietario)
        self.servicio.registrar(vehiculo)

        self.actualizar_tabla()
        self.limpiar()

    def actualizar_tabla(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for v in self.servicio.listar():
            self.tabla.insert("", "end", values=v.obtener_datos())

    def limpiar(self):
        self.txt_placa.delete(0, tk.END)
        self.txt_marca.delete(0, tk.END)

        self.txt_propietario.delete(0, tk.END)
