from django.db import models
import uuid
# Create your models here.

class post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    titulo = models.CharField(max_length=60, default='Desconocido')
    contenido = models.TextField()
    fecha_modificacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    img = models.FileField(upload_to='img/')
    status = models.BooleanField(default=False)
    autor = models.ForeignKey('user_profile.profile', on_delete=models.CASCADE, related_name='posts', default=1)
    
    # def __str__(self):
    #     return {
    #         "id": self.id,
    #         "titulo": self.titulo,
    #         "contenido": self.contenido,
    #         "img": self.img,
    #     }

class catalogo_categorias(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    categorias = models.ManyToManyField(post, related_name='posts')

    def __str__(self):
        return self.nombre