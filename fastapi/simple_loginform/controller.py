from hashlib import sha256
from schema import UserIn

# Variables globales
db = []
# Cuenta administrador
admin = UserIn
admin.username = "admin"
admin.password = "password"
db.append(admin)


## Funciones auxiliares
# Encriptar contraseña
def _hash(pass_text: str):
    bytes_pass_text = pass_text.encode("utf-8")

    m = sha256()
    m.update(bytes_pass_text)
    hashed_pass = m.hexdigest()

    return hashed_pass


## Funciones importantes
# Ver si usuario está en db
def check_user(user: UserIn):
    hash_pass = _hash(user.password)
    for signed_user in db:
        if user.username == signed_user.username and hash_pass == signed_user.password:
            return "User in DB"
    return "User not in DB"


# Crear usuario si no existe
def create_user(user: UserIn):
    # Chequear cada nombre de usuario
    for signed_users in db:
        if user.username == signed_users.username:
            return "User already in database"
    # Añadir usuario a base de datos
    user.password = _hash(user.password)
    db.append(user)
    return "Sign Up success !!"


# Devolver lista de usuarios al admin
def list_users(user: UserIn):
    if user.username != admin.username or user.password != admin.password:
        return "ONLY ADMiN ACCESS"
    return [_.username for _ in db]  # Devuelve lista de ingresados


# Devolver base de datos para debug
def view_db():
    return db
