from fastapi import FastAPI

router = FastAPI()

@router.get("/")
def hello_world():
    return {"Hello": "world"}

# Probar distintos enrutamientos y respuestas del sistema
@router.get("/idea")
def testing_idea():
    return "This is a test"

@router.post("/submit")
def submit_number(data: str):
    return {"Your data": data}
