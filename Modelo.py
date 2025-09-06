class Participantes:
    def __init__(self, nombre, institucion):
        self.nombre = nombre
        self.institucion = institucion

    def mostrar_info(self):
        return f"{self.nombre} - {self.institucion}"

class BandaEscolar(Participantes):
    Categorias_Validas = ["Primaria","Básico","Diversificado"]
    Criterios = ["ritmo", "uniformidad", "coreografía", "alineación", "puntualidad"]

    def __init__(self, nombre, institucion, categoria):
        super().__init__(nombre, institucion)
        self._categoria = None
        self._puntajes = {}
        self.set_categoria(categoria)

    def set_categoria(self, categoria):
        if categoria == self.Categorias_Validas:
            self._categoria = categoria
        else:
            raise ValueError("Categoria incorrecta")

    def registrar_puntajes(self, puntajes):
        if set(puntajes.keys()) != set(self.Criterios):
            raise ValueError("Criterios incompletos o inválidos")
        for v in puntajes.values():
            if not (0 <= v <= 10):
                raise ValueError("El puntaje debe ser entre 0 y 10")
            self._puntajes = puntajes
    @property
    def total(self):
        return sum(self._puntajes.values() if self._puntajes else 0)

    def mostrar_info(self):
        base = super().mostrar_info()
        info = f"{base} - {self._categoria}"
        if self._puntajes:
            info += f" - Total: {self.total}"

class Concurso:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha
        self.bandas = {}

    def incribir_banda(self, banda):
        if banda.nombre in self.bandas:
            raise ValueError(f"Nombre de banda duplicado")
        self.bandas[banda.nombre] = banda
        with open("bandas.txt", "a", encoding="utf-8") as f:
            f.write(f"{banda.nombre} - {banda.institucion} - {banda.categoria}\n")

    def registrar_eveluacion(self, nombre_banda, puntajes):
        if nombre_banda not in self.bandas:
            raise ValueError(f"Banda no encontrada")
        banda = self.bandas[nombre_banda]
        banda.registrar_puntajes(puntajes)
        with open ("evaluaciones.txt", "a", encoding="utf-8") as f:
            f.write(f"{banda.nombre} - {','.join(f'{k}:{v}' for k,v in puntajes.items())} - Total:{banda.total}\n")

    def listar_bandas(self):
        return [b.mostrar_info() for b in self.bandas.values()]

    def ranking(self):
        evaluadas = [b for b in self.bandas.values() if b._puntajes]
        return sorted(evaluadas, key=lambda b: (-b.total, b.nombre))