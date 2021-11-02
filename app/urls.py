from django.urls import path
from .views import ViewHome,LogoutUser,CrearCasa,VerCasa, EliminarCasa, EditarCasa, EliminarGaleria
app_name="app"

urlpatterns=[
    path('',ViewHome.as_view(),name="home"),
    path('logout/',LogoutUser.as_view(),name="logout"),
    path('crearCasa/',CrearCasa.as_view(),name="crearCasa"),
    path('detalle/<int:id>/',VerCasa.as_view(),name="detalle"),
    path('eliminar/<int:id>/',EliminarCasa.as_view(),name="eliminar"),
    path('editar/<int:id>/',EditarCasa.as_view(),name="editar"),
    path('eliminar/galeria/<int:id>/',EliminarGaleria.as_view(),name="eliminarGaleria"),
]
