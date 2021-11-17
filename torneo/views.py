from django.http.response import HttpResponse
from django.shortcuts import render
from .torneo import Torneo
import pickle
import base64

maxEquipos = 4
minEquipos = 2

# Create your views here.
def index(request):
    if request.method == "POST":
        
        campeonato = Torneo()

        campeonato.equipos = []
        campeonato.partidos = []
        campeonato.rivales = []
        
        camp = pickle.dumps(campeonato)
        request.session["campeonato"] = base64.b64encode(camp).decode()
        
        n = int(request.POST["teams"])
        
        context = {
            "n": n,
            "range_l": range(1, n+1)
        }
        
        if n > maxEquipos:
            context["msg"] = f"{str(maxEquipos)} es la cantidad máxima de equipos que se pueden registrar."
            return render(request, "form.html", context=context)
        elif n < minEquipos:
            context["msg"] = f"Error: el número mínimo de equipos debe ser {str(minEquipos)}"
            return render(request, "form.html", context=context)
        return render(request, "registroEquipos.html", context=context)

        
    return render(request, "form.html")


def registroJuegos(request):
    if request.method == "POST":

        camp = base64.b64decode(request.session.get("campeonato").encode())
        campeonato = pickle.loads(camp)
        
        equipos = [request.POST[equipo] for equipo in request.POST if "team" in equipo]
        
        for j in equipos:
            campeonato.registroEquipo(j)

        campeonato.encuentros()

        juegos = []

        for pareja in campeonato.rivales:
            par = (pareja[0].nombre,pareja[1].nombre)
            juegos.append(par)
        
        camp = pickle.dumps(campeonato)
        request.session["campeonato"] = base64.b64encode(camp).decode()

        context = {
            "matches": juegos
        }

        return render(request, "registroJuegos.html", context=context)

    return render(request, "registroEquipos.html")


def tablaPosiciones(request):
    if request.method == "POST":
        camp = base64.b64decode(request.session.get("campeonato").encode())
        campeonato = pickle.loads(camp)
        
        for i in range(len(campeonato.rivales)):
            campeonato.crearPartido(campeonato.rivales[i],int(request.POST["goalsT1M"+str(i)]),int(request.POST["goalsT2M"+str(i)]))
        
        data = []
        for equ in campeonato.equipos:
            cabecera = vars(equ)
            d = []
            for item in cabecera:
                d.append(cabecera[item])
            data.append(d)
        
        request.session["campeonato"] = str(pickle.dumps(campeonato))
        
        context = {
            "head": cabecera,
            "data": data,
        }

        return render(request, "tablaPosiciones.html",context=context)

    return render(request, "form.html")  