from models import *
import itertools


class Torneo:

    def __init__(self):
        self.equipos = []
        self.rivales = []
        self.partidos = []
        self.victoria = 3
        self.empate = 1
    
    def registroEquipo(self, nombre):
        self.equipos.append(Equipo(nombre))

    def encuentros(self):
        self.rivales = list(itertools.combinations(self.equipos, 2))

    def posiciones(self):
        self.equipos.sort(key=lambda eq:(-eq.puntos,-eq.gd,-eq.gf))

    def crearPartido(self,pareja,goles1,goles2):
        pareja[0].gf += goles1
        pareja[1].gf += goles2
        pareja[0].gc += goles2
        pareja[1].gc += goles1

        for i in pareja:
            i.jugados += 1
            i.gd = i.gf - i.gc

        if goles1 == goles2:
            for i in pareja:
                i.empatados += self.empate
                i.puntos += self.empate
        elif goles1 > goles2:
            pareja[0].ganados += 1
            pareja[0].puntos += self.victoria
            pareja[1].perdidos += 1
        else:
            pareja[1].ganados += 1
            pareja[1].puntos += self.victoria
            pareja[0].perdidos += 1

        juego = Partido(pareja[0],pareja[1],goles1,goles2)

        self.partidos.append(juego)

        self.posiciones()
