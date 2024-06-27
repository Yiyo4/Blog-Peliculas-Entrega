"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from content_blog import views as content_views
from user_profile import views as profile_views

urlpatterns = [
    #urls django
    path('admin/', admin.site.urls),
    #urls para visualizar contenido general
    path('',content_views.home),
    path("autores/",content_views.autores),
    path("busqueda/",content_views.busqueda),
    path("mejor-puntuados/", content_views.m_puntuados),
    path("post/<str:id_post>/", content_views.leer_post),
    path("autor/<str:id_autor>/", content_views.ver_post_autor),
    path('post/<int:post_id>/', content_views.ver_post, name='ver_post'),
    #urls para usuarios
    path("login/", profile_views.login),
    path("registro/", profile_views.registro),
    path("registro/<uuid:id>/", profile_views.confirmacion),
    path("recuperacion/", profile_views.recuperacion),
    path("logout/", profile_views.logout_user),
    path("user/<str:user>",profile_views.profile_user),
    path("user/<str:user>/<str:action>/", profile_views.create_post),
]
