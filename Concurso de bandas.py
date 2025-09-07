import tkinter as tk
from tkinter import messagebox, simpledialog
from Modelo import BandaEscolar, Concurso

class Septiembre:
    def __init__(self):
        self.concurso = Concurso("Concurso de bandas 14 de Septiembre", "14-09-2025")
        self.concurso.cargar_datos()
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de bandas Quetzaltenango")
        self.ventana.geometry("500x300")
        self.ventana.config(bg="#5A64CC")

        self.menu()
        tk.Label( self.ventana, text="Sistema de Inscripción y Evaluación de Bandas Escolares"
            "\nConcurso 14 de Septiembre - Quetzaltenango", font=("Helvetica", 12, "bold"), fg="#02073B",
            justify="center").pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        self.ventana.option_add("*Menu*Font", "Helvetica 10 bold")
        self.ventana.option_add("*Menu*Background", "#7490C4")
        self.ventana.option_add("*Menu*Foreground", "white")
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Inscripción de Banda")
        ventana.geometry("500x350")
        ventana.config(bg="#8DA4CE")
        fuente = ("Helvetica", 12, "bold")
        color_texto = "#0A0A0A"
        tk.Label(ventana, text="Nombre de la Banda:", font=fuente, fg=color_texto, bg="#8DA4CE").pack(pady=5)
        entrada_nombre = tk.Entry(ventana, font=fuente)
        entrada_nombre.pack(pady=5)
        tk.Label(ventana, text="Institución:", font=fuente, fg=color_texto, bg="#8DA4CE").pack(pady=5)
        entrada_institucion = tk.Entry(ventana, font=fuente)
        entrada_institucion.pack(pady=5)
        tk.Label(ventana, text="Categoría (Primaria, Básico, Diversificado):", font=fuente, fg=color_texto, bg="#8DA4CE").pack(pady=5)
        entrada_categoria = tk.Entry(ventana, font=fuente)
        entrada_categoria.pack(pady=5)

        def registrar():
            nombre = entrada_nombre.get()
            institucion = entrada_institucion.get()
            categoria = entrada_categoria.get()
            try:
                banda = BandaEscolar(nombre, institucion, categoria)
                self.concurso.inscribir_banda(banda)
                messagebox.showinfo("Éxito", "Banda inscrita correctamente.")
                ventana.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        tk.Button(ventana, text="Registrar Banda", font=fuente, bg="#CDD7EA", fg="#0A0A0A", command=registrar).pack(pady=5)
        tk.Button(ventana, text="Regresar al Menú", font=fuente, bg="#CCCCCC", fg="#0A0A0A", command=ventana.destroy).pack(pady=5)

    def registrar_evaluacion(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Registro de Evaluación")
        ventana.geometry("500x500")
        ventana.config(bg="#8DA4CE")
        fuente = ("Helvetica", 12, "bold")
        color_texto = "#0A0A0A"
        tk.Label(ventana, text="Nombre de la Banda:", font=fuente, fg=color_texto, bg="#8DA4CE").pack(pady=5)
        entrada_nombre = tk.Entry(ventana, font=fuente)
        entrada_nombre.pack(pady=5)
        entradas_puntaje = {}
        for criterio in BandaEscolar.Criterios:
            tk.Label(ventana, text=f"{criterio.capitalize()} (0–10):", font=fuente, fg=color_texto, bg="#8DA4CE").pack(pady=5)
            entrada = tk.Entry(ventana, font=fuente)
            entrada.pack(pady=5)
            entradas_puntaje[criterio] = entrada

        def registrar():
            nombre = entrada_nombre.get()
            puntajes = {}
            try:
                for criterio, entrada in entradas_puntaje.items():
                    valor = float(entrada.get())
                    if not (0 <= valor <= 10):
                        raise ValueError(f"Puntaje fuera de rango en {criterio}")
                    puntajes[criterio] = valor
                self.concurso.registrar_evaluacion(nombre, puntajes)
                messagebox.showinfo("Éxito", "Evaluación registrada correctamente.")
                ventana.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        tk.Button(ventana, text="Registrar Evaluación", font=fuente, bg="#CDD7EA", fg="#0A0A0A", command=registrar).pack(pady=5)
        tk.Button(ventana, text="Regresar al Menú", font=fuente, bg="#CCCCCC", fg="#0A0A0A", command=ventana.destroy).pack(pady=5)

    def listar_bandas(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Lista de Bandas")
        ventana.geometry("600x400")
        ventana.config(bg="#5A64CC")

        for info in self.concurso.listar_bandas():
            tk.Label(ventana, text=info, anchor="w", font=("Arial", 12), fg="#0A0A0A",
                bg="#E6F2FF").pack(fill="x", padx=10, pady=5)

    def ver_ranking(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Ranking Final")
        ventana.geometry("600x400")
        ventana.config(bg="#5A64CC")

        ranking = self.concurso.ranking()
        for i, banda in enumerate(ranking, start=1):
            text = f"{i}. {banda.nombre} - {banda.institucion} - {banda.categoria} - Total: {banda.total}"
            tk.Label(ventana, text=text, anchor="w", font=("Arial", 12), fg="#0A0A0A",
                bg="#E6F2FF").pack(fill="x", padx=10, pady=5)

if __name__ == "__main__":
    Septiembre()