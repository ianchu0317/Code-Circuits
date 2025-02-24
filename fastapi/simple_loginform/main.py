from fastapi import FastAPI
from schema import UserIn, UserOut
from controller import create_user, list_users, check_user, view_db

app = FastAPI()

# Devuelve datos de login pero sin la contraseña
@app.post("/api/login")
def login(user: UserIn) -> str:
    return check_user(user)


# Crear un usuario si no está en base de datos
@app.post("/api/signup")
def sign_up(user: UserIn):
    return create_user(user)


# Crear un apartado para ver los usuarios ingresados
@app.get("/api/view/users")
def view_users(user: UserIn):
    return list_users(user)


# Ver la base de datos para debug
@app.get("/api/db")
def debug() -> list[UserIn]:
    return view_db()
