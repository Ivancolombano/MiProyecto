from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Pasteleria, Cocina, Promociones, Avatar, Usuario, Pedido
from .forms import Pasteleriaformulario, Cocinaformulario, Promocionesformulario, UserEditForm, AvatarFormulario, UsuarioFormulario, PedidoCocinaFormulario, PedidoPasteleriaFormulario, PedidoPromocionesFormulario

# Create your views here.

#Funciones pasteleria

def pasteleria(req, nombre, descripcion, precio):

    pasteleria = Pasteleria(nombre=nombre, descripcion=descripcion, precio=precio)
    pasteleria.save()

    return HttpResponse(f"""
    <p>Pastelería: {pasteleria.nombre} {pasteleria.descripcion} - Precio: $ {pasteleria.precio} agregado con éxito!</p>""")


def lista_pasteleria(req):

    lista = Pasteleria.objects.all()

    return render(req, "lista_pasteleria.html", {"lista_pasteleria": lista})



#Funciones cocina


def cocina(req, nombre, descripcion, precio):

    cocina = Cocina(nombre=nombre,descripcion=descripcion, precio=precio)
    cocina.save()

    return HttpResponse(f"""
    <p>Cocina: {cocina.nombre} {cocina.descripcion} - Precio: $ {cocina.precio} agregado con éxito!</p>""")


def lista_cocina(req):

    lista = Cocina.objects.all()

    return render(req, "lista_cocina.html", {"lista_cocina": lista})


#Funciones promociones


def promociones(req, nombre, descripcion, precio):

    promociones = Promociones(nombre=nombre, descripcion=descripcion, precio=precio)
    promociones.save()

    return HttpResponse(f"""
    <p>Promociones: {promociones.nombre} {promociones.descripcion} - Precio: $ {promociones.precio} agregado con éxito!</p>""")


def lista_promociones(req):

    lista = Promociones.objects.all()

    return render(req, "lista_promociones.html", {"lista_promociones": lista})



#Vistas

def inicio(req):
    try:
     avatar = Avatar.objects.get(user=req.user.id)
     return render(req, "inicio.html", {"url_avatar": avatar.imagen.url})
    except:
        return render(req, "inicio.html")


def pasteleria(req):

    return render(req, "pasteleria.html")

def cocina(req):

    return render(req, "cocina.html")

def promociones(req):

    return render(req, "promociones.html")

def inicio_de_sesion(req):

    return render(req, "iniciar_sesion.html")

#Formularios


@staff_member_required(login_url='/app-proyecto/login')
def pasteleriaFormulario(req):

    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':

       miFormulario = Pasteleriaformulario(req.POST)

       if miFormulario.is_valid():

          data = miFormulario.cleaned_data 
          pasteleria = Pasteleria(nombre=data["pasteleria"], descripcion=data["descripcion"], precio=data["precio"])                                             
          pasteleria.save()

          return render(req, "inicio.html")
    else:
     
        miFormulario = Pasteleriaformulario()
        return render(req, "pasteleriaFormulario.html", {"miFormulario": miFormulario})
    
    

@staff_member_required(login_url='/app-proyecto/login')
def cocinaFormulario(req):

    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':

       miFormulario = Cocinaformulario(req.POST)

       if miFormulario.is_valid():

          data = miFormulario.cleaned_data 
          cocina = Cocina(nombre=data["cocina"], descripcion=data["descripcion"], precio=data["precio"])                                             
          cocina.save()

          return render(req, "inicio.html")
    else:
     
        miFormulario = Cocinaformulario()
        return render(req, "cocinaFormulario.html", {"miFormulario": miFormulario})
     


@staff_member_required(login_url='/app-proyecto/login')    
def promocionesFormulario(req):

    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':

        miFormulario = Promocionesformulario(req.POST)

        if miFormulario.is_valid():
           
           data = miFormulario.cleaned_data 
           promociones = Promociones(nombre=data["promociones"], descripcion=data["descripcion"], precio=data["precio"])                                             
           promociones.save()

           return render(req, "inicio.html")
    else:
     
        miFormulario = Promocionesformulario()
        return render(req, "promocionesFormulario.html", {"miFormulario": miFormulario})     
    

#Busquedas    
    

def  busquedaPasteleria(req):

    return render(req, "busquedaPasteleria.html")

def buscar_pasteleria(req: HttpRequest):

   if req.GET["nombre"]:
      nombre = req.GET["nombre"]
      precios = Pasteleria.objects.filter(nombre=nombre)
      return render(req, "resultadosBusquedaPasteleria.html", {"precios": precios})
   else:
       return HttpResponse(f"No se encontraron resultados")
   
   




def  busquedaCocina(req):

    return render(req, "busquedaCocina.html")

def buscar_cocina(req: HttpRequest):

   if req.GET["nombre"]:
      nombre = req.GET["nombre"]
      precios = Cocina.objects.filter(nombre=nombre)
      return render(req, "resultadosBusquedaCocina.html", {"precios": precios})
   else:
       return HttpResponse(f"No se encontraron resultados")



def  busquedaPromociones(req):

    return render(req, "busquedaPromociones.html")

def buscar_promociones(req: HttpRequest):

   if req.GET["nombre"]:
      nombre = req.GET["nombre"]
      precios = Promociones.objects.filter(nombre=nombre)
      return render(req, "resultadosBusquedaPromociones.html", {"precios": precios})
   else:
       return HttpResponse(f"No se encontraron resultados")
   

#Eliminar y editar



class PasteleriaList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Pasteleria
    template_name = "pasteleria_list.html"
    context_object_name = "pasteleria"

    def test_func(self):       
     return self.request.user.is_staff
    
    def handle_no_permission(self):
        
        return redirect('/app-proyecto/')



class PasteleriaDetail(LoginRequiredMixin, DetailView):
    model = Pasteleria
    template_name = "pasteleria_detail.html"
    context_object_name = "listado"


class PasteleriaCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Pasteleria
    template_name = "pasteleria_create.html"
    fields = ["nombre", "precio", "descripcion"]
    success_url = '/app-proyecto/'
    login_url='/app-proyecto/login'
    

    def test_func(self):       
     return self.request.user.is_staff
    
    def handle_no_permission(self):
        
        return redirect('/app-proyecto/')



class PasteleriaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pasteleria
    template_name = "pasteleria_update.html"
    fields = ('__all__')
    context_object_name = "listado"
    success_url = '/app-proyecto/listapasteleria'
    login_url='/app-proyecto/login'

    def test_func(self):       
     return self.request.user.is_staff
    
    def handle_no_permission(self):
        
        return redirect('/app-proyecto/')


class PasteleriaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pasteleria
    template_name = "pasteleria_delete.html"
    success_url = '/app-proyecto/listapasteleria'
    context_object_name = "listado"
    login_url='/app-proyecto/login'


    def test_func(self):       
     return self.request.user.is_staff
    
    def handle_no_permission(self):
        
        return redirect('/app-proyecto/')




class CocinaList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Cocina
    template_name = "cocina_list.html"
    context_object_name = "cocina"

    def test_func(self):       
     return self.request.user.is_staff
    
    def handle_no_permission(self):
        
        return redirect('/app-proyecto/')



class CocinaDetail(LoginRequiredMixin, DetailView):
    model = Cocina
    template_name = "cocina_detail.html"
    context_object_name = "listado"


class CocinaCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Cocina
    template_name = "cocina_create.html"
    fields = ["nombre", "precio", "descripcion"]
    success_url = '/app-proyecto/'
    login_url='/app-proyecto/login'

    def test_func(self):       
     return self.request.user.is_staff
    
    def handle_no_permission(self):
        
        return redirect('/app-proyecto/')


class CocinaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cocina
    template_name = "cocina_update.html"
    fields = ('__all__')
    context_object_name = "listado"
    success_url = '/app-proyecto/listacocina'
    login_url='/app-proyecto/login'


    def test_func(self):       
     return self.request.user.is_staff
    
    def handle_no_permission(self):
        
        return redirect('/app-proyecto/')


class CocinaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cocina
    template_name = "cocina_delete.html"
    success_url = '/app-proyecto/listacocina'
    context_object_name = "listado"
    login_url='/app-proyecto/login'


    def test_func(self):       
     return self.request.user.is_staff
    
    def handle_no_permission(self):
        
        return redirect('/app-proyecto/')






class PromocionesList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Promociones
    template_name = "promociones_list.html"
    context_object_name = "promociones"

    def test_func(self):       
     return self.request.user.is_staff
    
    def handle_no_permission(self):
        
        return redirect('/app-proyecto/')



class PromocionesDetail(LoginRequiredMixin, DetailView):
    model = Promociones
    template_name = "promociones_detail.html"
    context_object_name = "listado"


class PromocionesCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Promociones
    template_name = "promociones_create.html"
    fields = ["nombre", "precio", "descripcion"]
    success_url = '/app-proyecto/'
    login_url='/app-proyecto/'


    def test_func(self):
        return self.request.user.is_staff
    

    def handle_no_permission(self):
        
        return redirect('/app-proyecto/')


class PromocionesUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Promociones
    template_name = "promociones_update.html"
    fields = ('__all__')
    context_object_name = "listado"
    success_url = '/app-proyecto/listapromociones'
    login_url='/app-proyecto/login'


    def test_func(self):       
     return self.request.user.is_staff
    
    def handle_no_permission(self):
        
        return redirect('/app-proyecto/')


class PromocionesDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Promociones
    template_name = "promociones_delete.html"
    success_url = '/app-proyecto/listapromociones'
    context_object_name = "listado"
    login_url='/app-proyecto/login'


    def test_func(self):       
     return self.request.user.is_staff
    
    def handle_no_permission(self):
        
        return redirect('/app-proyecto/')
    

#Login

def loginView(req):


    if req.method == 'POST':

       miFormulario = AuthenticationForm(req, data=req.POST)

       if miFormulario.is_valid():
           
           data = miFormulario.cleaned_data 
           usuario = data["username"]
           psw = data["password"]                                    
           
           user = authenticate(username=usuario, password=psw)
           if user:
               login(req, user)
               return render(req, "inicio.html", {"mensaje": f'Bienvenido {usuario}!'} )                   
       return render(req, "inicio.html", {"mensaje": f'Nombre de usuario o contraseña incorrecta'}) 
    else:
        miFormulario = AuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})
    
    

def register(req):    

    if req.method == 'POST':

       miFormulario = UserCreationForm(req.POST)

       if miFormulario.is_valid():
           
           data = miFormulario.cleaned_data 
           usuario = data["username"]
           miFormulario.save()                                                     
           return render(req, "inicio.html", {"mensaje": f'Usuario {usuario} creado con éxito!'}) 
       
       return render(req, "inicio.html", {"mensaje": f'Intente con otro usuario'}) 
    
    else:
        miFormulario = UserCreationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})
    

@login_required
def editar_perfil(req):

    usuario = req.user 
    if req.method == 'POST':

       miFormulario = UserEditForm(req.POST, instance=req.user)

       if miFormulario.is_valid():       
           data = miFormulario.cleaned_data 
           usuario.first_name = data["first_name"]
           usuario.last_name = data["last_name"]
           usuario.email = data["email"]
           usuario.set_password(data["password1"])                                   
           usuario.save()

           return render(req, "inicio.html", {"mensaje": "Actualización éxitosa"})
       else:
           return render(req, "editarPerfil.html", {"miFormulario": miFormulario})
       
    else:    
        miFormulario = UserEditForm(instance=usuario)
        return render(req, "editarPerfil.html", {"miFormulario": miFormulario})
    


@login_required
def agregar_avatar(req):    

    if req.method == 'POST':

       miFormulario = AvatarFormulario(req.POST, req.FILES)

       if miFormulario.is_valid():       

           data = miFormulario.cleaned_data

           avatar = Avatar(user=req.user, imagen=data["imagen"])                            
           avatar.save()

           return render(req, "inicio.html", {"mensaje": "Actualización éxitosa"})
       
    else:    
        miFormulario = AvatarFormulario()
        return render(req, "agregarAvatar.html", {"miFormulario": miFormulario})




    
def crea_usuario(req):    

    if req.method == 'POST':
       
       info = req.POST

       miFormulario = UsuarioFormulario({
           "nombre": info["nombre"],
           "apellido": info["apellido"],
           "email": info["email"],})
       
       userForm = UserCreationForm({
           "username": info["username"],
           "password1": info["password1"],
           "password2": info["password2"],})
       

       if miFormulario.is_valid() and userForm.is_valid():
           
           data = miFormulario.cleaned_data 
           data.update(userForm.cleaned_data)

           user = User(username=data["username"])
           user.set_password(data["password1"])
           user.save()



           usuario = Usuario(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], user=user)
           usuario.save()                                                     
           return render(req, "inicio.html", {"mensaje": f'Usuario creado con éxito!'}) 
    
    else:
        miFormulario = UsuarioFormulario()
        userForm = UserCreationForm()
        return render(req, "usuarioFormulario.html", {"miFormulario": miFormulario, "userForm": userForm})




@login_required
def pedidoPasteleria(req):
    

    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':

       miFormulario = PedidoPasteleriaFormulario(req.POST)

       if miFormulario.is_valid():

          data = miFormulario.cleaned_data 
          pasteleria = Pedido(comentario=data["comentario"], cantidad=data["cantidad"])                                             
          pasteleria.save()

          return render(req, "inicio.html", {"mensaje": f'Gracias por tu compra!'})
    else:
     
        miFormulario = PedidoPasteleriaFormulario()
        return render(req, "pedidoPasteleria.html", {"miFormulario": miFormulario})



@login_required
def pedidoCocina(req):
    

    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':

       miFormulario = PedidoCocinaFormulario(req.POST)

       if miFormulario.is_valid():

          data = miFormulario.cleaned_data 
          cocina = Pedido(comentario=data["comentario"], cantidad=data["cantidad"])                                             
          cocina.save()

          return render(req, "inicio.html", {"mensaje": f'Gracias por tu compra!'})
    else:
     
        miFormulario = PedidoCocinaFormulario()
        return render(req, "pedidoCocina.html", {"miFormulario": miFormulario})
    





@login_required
def pedidoPromociones(req):
    

    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':

       miFormulario = PedidoPromocionesFormulario(req.POST)

       if miFormulario.is_valid():

          data = miFormulario.cleaned_data 
          promociones = Pedido(comentario=data["comentario"], cantidad=data["cantidad"])                                             
          promociones.save()

          return render(req, "inicio.html", {"mensaje": f'Gracias por tu compra!'})
    else:
     
        miFormulario = PedidoPromocionesFormulario()
        return render(req, "pedidoPromociones.html", {"miFormulario": miFormulario})    
    



def nosotros(req):

    return render(req, "nosotros.html")    



def contacto(req):

    return render(req, "contacto.html")    
