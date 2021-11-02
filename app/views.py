from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegisterForm, LoginUser, CasaForm, UpdateDatosPersona, GaleriaForm, CambioGaleriaImg, CambioImgCasa
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Casa, GaleriaCasa, Usuario
from django.urls import reverse_lazy
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


class ViewHome(View):
    def get(self, request, casa = None,*args, **kwargs):
        form = UserRegisterForm()
        formUsuario = LoginUser()
        print(kwargs)
        casas = Casa.objects.all()
        #COMIENZO DE PAGINADOR
        paginador = Paginator(casas,1)
        pagina = request.GET.get("page") or 1
        post = paginador.get_page(pagina)
        paginaActual = int(pagina)
        numeroDePaginas = range(1,post.paginator.num_pages + 1)
        context = {
            'form': form,
            'formUsuario': formUsuario,
            'casas':post,
	        'numeroDePaginas':numeroDePaginas ,
	        'paginaActual':paginaActual 
        }
        return render(request, 'app/index.html', context)

    def post(self, request, *args, **kwargs):
        buscador = request.POST.get("buscador")
        print("EL BUSCADOR ES: ", buscador)
        if request.method == 'POST':
            form = UserRegisterForm(request.POST, request.FILES)
            formUsuario = LoginUser(request.POST)
            if form.is_valid():
                messages.success(request, "Usuario creado con exito")
                form.save()
                return redirect('app:home')
            if formUsuario.is_valid():
                name = formUsuario.cleaned_data.get("email")
                password = formUsuario.cleaned_data.get("password")
                usuario = authenticate(email=name, password=password)
                if usuario is not None:
                    login(request, usuario)
                    #messages.success(request, "bienvenido")
                    return redirect("app:home")
                else:
                    messages.error(request, "Contraseña o usuario incorrecto")
            if buscador is not None:
                casa = Casa.objects.filter(
                Q(titulo__icontains=buscador) | 
                Q(id__icontains=buscador)).distinct()
                print("CASA: ", casa)
                #COMIENZO DE PAGINADOR
                paginador = Paginator(casa,1)
                pagina = request.GET.get("page") or 1
                post = paginador.get_page(pagina)
                paginaActual = int(pagina)
                numeroDePaginas = range(1,post.paginator.num_pages + 1)
                context = {
                    'form': form,
                    'formUsuario': formUsuario,
                    'casa':post,
                    'numeroDePaginas':numeroDePaginas ,
                    'paginaActual':paginaActual 
                }
                return render(request, 'app/index.html', context)
        else: 
            form = UserRegisterForm()
            formUsuario = LoginUser()
        context = {
            'form': form,
            'formUsuario': formUsuario,
            'casas':Casa.objects.all()
        }
        return render(request, 'app/index.html', context)


class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect("app:home")


@method_decorator(login_required(login_url='/'), name='dispatch')
class CrearCasa(View):
    def get(self, request, *args, **kwargs):
        formCasa = CasaForm()
        formGaleriaCasa = GaleriaForm()
        context = {'formCasa': formCasa, 'formGaleriaCasa': formGaleriaCasa}
        return render(request, 'app/crearCasa.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            formCasa = CasaForm(request.POST, request.FILES)
            formGaleriaCasa = GaleriaForm(request.POST, request.FILES)
            if formCasa.is_valid() and formGaleriaCasa.is_valid():
                casa = formCasa.save(commit=False)
                casa.idUsuario = request.user
                casa.save()

                galeriaCasa = request.FILES.getlist('imagenGaleria')
                for image in galeriaCasa:
                    GaleriaCasa.objects.create(
                        imagenGaleria=image, idCasa=casa)
                return redirect('app:home')
        else:
            formCasa = CasaForm()
            formGaleriaCasa = GaleriaForm()
        context = {'formCasa': formCasa, 'formGaleriaCasa': formGaleriaCasa}
        return render(request, 'app/crearCasa.html', context)


class VerCasa(View):
    def get(self, request, id):
        casa = Casa.objects.get(id=id)
        galeria = GaleriaCasa.objects.filter(idCasa=casa)
        if casa is None:
            return redirect('app:home')
        context = {'casa': casa, 'galeria': galeria}
        return render(request, 'app/detalleCasa.html', context)


@method_decorator(login_required(login_url='/'), name='dispatch')
class EliminarCasa(View):
    def get(self, request, id):
        model = Casa.objects.get(id=id)
        if request.user == model.idUsuario:
            model.delete()
        return redirect("app:home")


@method_decorator(login_required(login_url='/'), name='dispatch')
class EditarCasa(View):
    def get(self, request, id, *args, **kwargs):
        casa = Casa.objects.get(id=id)
        galeria = GaleriaCasa.objects.filter(idCasa=casa)
        formularioGaleria = CambioGaleriaImg()
        formularioDatosUsuario = UpdateDatosPersona()
        formCasa = CambioImgCasa()
        context = {'casa': casa, 'galeria': galeria, 'form': formularioGaleria,
                   'formDatos': formularioDatosUsuario, 'formCasa': formCasa}
        return render(request, 'app/editarCasa.html', context)

    def post(self, request, id):
        if request.method == "POST":
            form = CambioGaleriaImg(request.POST, request.FILES)
            formularioDatosUsuario = UpdateDatosPersona(request.POST)
            formCasa = CambioImgCasa(request.POST, request.FILES)
            if form.is_valid():
                idImg = request.POST.get("id")
                if idImg is not None:
                    model = GaleriaCasa.objects.get(id=idImg)
                    if request.user != model.idCasa.idUsuario:
                        return redirect('app:home')
                    form = CambioGaleriaImg(
                        request.POST, request.FILES, instance=model)
                    form.save()
                    return redirect('app:editar', id=model.idCasa.id)

            if formCasa.is_valid():
                idImgCasa = request.POST.get("idCasa")
                if idImgCasa is not None:
                    casa = Casa.objects.get(id=idImgCasa)
                    if request.user != casa.idUsuario:
                        return redirect('app:home')
                    formCasa = CambioImgCasa(
                        request.POST, request.FILES, instance=casa)
                    formCasa.save()
                    return redirect('app:editar', id=idImgCasa)
            # Editar datos del usuario
            if formularioDatosUsuario.is_valid():
                # Cojo los datos
                nombre = formularioDatosUsuario.cleaned_data.get("nombre")
                apellido = formularioDatosUsuario.cleaned_data.get("apellido")
                celular = formularioDatosUsuario.cleaned_data.get(
                    "numeroCelular")
                titulo = formularioDatosUsuario.cleaned_data.get("titulo")
                descripcion = formularioDatosUsuario.cleaned_data.get(
                    "descripcion")
                id = request.POST.get("idUsuarioData")
                # Paso los datos a casa
                casa = Casa.objects.get(id=id)
                casa.titulo = titulo
                casa.descripcion = descripcion
                casa.save()
                # Paso los datos al usuario
                usuario = Usuario.objects.get(id=casa.idUsuario.id)
                usuario.nombre = nombre
                usuario.apellido = apellido
                usuario.numeroCelular = celular
                usuario.save()
                return redirect('app:editar', id=id)
        else:
            return redirect('app:editar', id=id)


@method_decorator(login_required(login_url='/'), name='dispatch')
class EliminarGaleria(View):
    def get(self, request, id):
        model = GaleriaCasa.objects.get(id=id)
        if request.user == model.idCasa.idUsuario:
            model.delete()
        return redirect('app:editar', id=model.idCasa.id)
