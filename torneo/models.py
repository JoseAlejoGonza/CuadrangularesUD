class Equipo:

    def __init__(self, nombre):
        self.nombre = nombre
        self.jugados = 0
        self.ganados = 0
        self.empatados = 0
        self.perdidos = 0
        self.gf = 0
        self.gc = 0
        self.gd = 0
        self.puntos = 0

class Partido:

    def __init__(self, equipo1, equipo2, goles1, goles2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.goles1 = goles1
        self.goles2 = goles2