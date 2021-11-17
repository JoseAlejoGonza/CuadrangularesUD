from django.urls import path
from .views import index, registroJuegos, tablaPosiciones

urlpatterns = [
    path("", index, name="index"),
    path("/registroJuegos", registroJuegos, name="registroJuegos"),
    path("/tablaPosiciones", tablaPosiciones, name="tablaPosiciones"),
]