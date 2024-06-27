from django.shortcuts import render, get_object_or_404
# from content_blog.models import catalogo_categorias as cat
from content_blog.models import post
from user_profile.models import profile
from django.db.models import Q

# Create your views here.
def home(request):
    """renderiza el home del sistema""" 
    posts = post.objects.all()
    try:
        posts = posts[::-1]
        posts = posts[0:8]
    except:
        pass
    print(post)
    return render(request,'home.html',{'posts':posts})

def autores(request):
    list_autores = profile.objects.all()
    return render(request,"autores.html",{'autores': list_autores})


def busqueda(request):
    if request.method == 'POST':
        busqueda_query = request.POST.get('busqueda', '')  # Obtener la cadena de búsqueda del formulario
        print("Búsqueda:", busqueda_query)

        # Realizar la búsqueda insensible a mayúsculas y minúsculas en el título
        resultados = post.objects.filter(titulo__icontains=busqueda_query)

        if resultados.exists():
            print('Encontré algo:', resultados)
            return render(request, "busqueda.html", {'resultados': resultados})
        else:
            print('No se encontraron resultados para la búsqueda:', busqueda_query)

    # Renderizar la plantilla con un mensaje indicando que no hay resultados
    return render(request, "busqueda.html", {'resultados': None})

def m_puntuados(request):
    return render(request,"m_puntuados.html")

def leer_post(request,id_post):
    try:
        l_post = post.objects.get(id = id_post)
        return render(request,"leer_post.html",{'post':l_post})
    except:
        return render(request,"404.html")

def ver_post_autor(request,id_autor):
    post_user = post.objects.filter(autor=id_autor)
    return render(request,"ver_post_autores.html",{'posts':post_user})

def ver_post(request, post_id):
    post = get_object_or_404(post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

