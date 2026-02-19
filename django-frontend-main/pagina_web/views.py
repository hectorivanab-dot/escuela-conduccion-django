from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime

# Base de datos simulada en memoria
ESCUELAS = {}

def registro_escuela(request):
    if request.method == "POST":
        escuela_id = request.POST.get("escuela_id")
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        password = request.POST.get("password")

        if escuela_id in ESCUELAS:
            messages.error(request, "El ID ya está registrado")
        else:
            ESCUELAS[escuela_id] = {
                "nombre": nombre,
                "correo": correo,
                "password": password
            }
            messages.success(request, "Escuela registrada correctamente")
            return redirect("login")

    return render(request, "escuela/registro.html")


def login_usuario(request):
    if request.method == "POST":
        escuela_id = request.POST.get("escuela_id")
        password = request.POST.get("password")

        escuela = ESCUELAS.get(escuela_id)

        if escuela and escuela["password"] == password:
            request.session["escuela_id"] = escuela_id
            request.session["nombre"] = escuela["nombre"]
            request.session["correo"] = escuela["correo"]
            request.session["login_time"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            return redirect("dashboard")
        else:
            messages.error(request, "ID o contraseña incorrectos")

    return render(request, "escuela/login.html")


def dashboard(request):
    if "escuela_id" not in request.session:
        return redirect("login")

    contexto = {
        "escuela_id": request.session.get("escuela_id"),
        "nombre": request.session.get("nombre"),
        "correo": request.session.get("correo"),
        "login_time": request.session.get("login_time"),
    }

    return render(request, "escuela/dashboard.html", contexto)


def cerrar_sesion(request):
    request.session.flush()
    return redirect("login")
