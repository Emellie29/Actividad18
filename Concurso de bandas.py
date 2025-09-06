import tkinter as tk
from tkinter import messagebox, simpledialog
from Modelo import BandaEscolar, Concurso

class Septiembre:
    def __init__(self):
        self.concurso = Concurso("Concurso de bandas 14 de Septiembre", "14-09-2025")
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
        nombre = simpledialog.askstring("Nombre", "Nombre de la banda: ")
        institucion = simpledialog.askstring("Institución", "Nombre de la institución: ")
        categoria = simpledialog.askstring("Categoría", "Categoría (Primaria, Básico, Diversificado): ")
        try:
            banda = BandaEscolar(nombre, institucion, categoria)
            self.concurso.inscribir_banda(banda)
            messagebox.showinfo("Banda inscrita correctamente.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def registrar_evaluacion(self):
        nombre = simpledialog.askstring("Nombre", "Nombre de la banda: ")
        puntajes = {}
        for criterio in BandaEscolar.Criterios:
            valor = simpledialog.askfloat("Puntaje", f"{criterio} (0-10): ", minvalue=0, maxvalue=10)
            puntajes[criterio] = valor
            try:
                self.concurso.registrar_evaluacion(nombre, puntajes)
                messagebox.showinfo("Evaluacion registrada correctamente.")
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def listar_bandas(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Lista de Bandas")
        for info in self.concurso.listar_bandas():
            tk.Label(ventana, text=info, anchor="w").pack(fill="x")

    def ver_ranking(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Ranking Final")
        ranking = self.concurso.ranking()
        for i, banda in enumerate(ranking, start=1):
            texto = f"{i}. {banda.nombre} - {banda.institucion} - {banda.categoria} - Total: {banda.total}"
            tk.Label(ventana, text=texto, anchor="w").pack(fill="x")

if __name__ == "__main__":
    Septiembre()