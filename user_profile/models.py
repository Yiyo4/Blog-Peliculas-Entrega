from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# esta clase define el perfil de usuario y extiende de AbstractUser
# por que solo se necesitaba eliminar los campos de first_name y last_name
# el resto del contenido se podia conservar
class profile(AbstractUser):
    """Define el modelo del usuario, hereda de AbstractUser y elimina algunos campos"""
    
    first_name = None
    last_name = None
    nombre = models.CharField(max_length=100,blank=True)
    a_paterno = models.CharField(max_length=100, blank=True)
    a_materno = models.CharField(max_length=100,blank=True)
    img = models.ImageField(upload_to = 'user/', blank= True, null = True)
    clave_confirmacion = models.UUIDField(default=uuid.uuid4,editable=False)
    genero = models.CharField(max_length=20, default='Prefiero no decirlo',blank=True)
    comentario = models.TextField(blank= True, null = True)

 

    # class Meta(AbstractUser.Meta):
    #     swappable = 'AUTH_USER_MODEL'