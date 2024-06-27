from django import template
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_mail(nombre,a_paterno,a_materno,mail,clave):
    """configura el servicio de envio de mails de django"""
    

    #guardar clave en base de datos

    context = {
        'nombre' : nombre,
        'a_paterno' : a_paterno,
        'a_materno' : a_materno,
        'url': settings.DOMINIO,
        'clave': clave,
    }

    template = get_template('mail.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Correo de confirmación',
        'Blog de Peliculas',
        settings.EMAIL_HOST_USER,
        [mail],
    )

    email.attach_alternative(content,'text/html')
    
    email.send()

def send_recovery_email(nombre, a_paterno, a_materno, mail, new_password):
    """Envía un correo de recuperación de contraseña al usuario"""
    
    context = {
        'nombre': nombre,
        'a_paterno': a_paterno,
        'a_materno': a_materno,
        'url': settings.DOMINIO,
        'new_password': new_password,
    }

    template = get_template('recovery_mail.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Recuperación de contraseña',
        'Blog de Peliculas',
        settings.EMAIL_HOST_USER,
        [mail],
    )

    email.attach_alternative(content, 'text/html')
    email.send()
