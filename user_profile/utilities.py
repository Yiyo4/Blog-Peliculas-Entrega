from user_profile.models import profile as user
import re

def validar_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

def datos_completos(data):
    for valor in data.values():
        if not valor:
            return False
    return True

def validar_email(valor):
    if user.objects.filter(email=valor):
        return True
    else:
        return False

def validar_nickname(valor):
    if not user.objects.filter(username=valor):
        return True
    else:
        return False

# def is_complete(clave):
#     res = user.objects.filter(clave_confirmacion=clave)
#     return res.is_active