from user_profile.models import profile as user


def create_user(correo, nombre, a_paterno, a_materno,clave, password):
    try:
        new_user = user.objects.create(
            email=correo, 
            nombre = nombre,
            password = password,
            username = nombre, 
            a_paterno = a_paterno,
            a_materno = a_materno,
            clave_confirmacion = clave,
            is_active = False
        )
    except :
        print("[Query user] error usuario existente")
        return False
    return new_user


def confirm_user(data):
    up_user = user.objects.get(email=data['email'])
    up_user.username = data['nickname']
    up_user.set_password(data['password'])
    up_user.genero = data['genero']
    up_user.is_active = True
    # up_user.is_active = True
    up_user.save()


def update_user():
    pass

