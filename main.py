from fastapi import FastAPI, Path,HTTPException

app = FastAPI()


students = {
    1: {
        "name" : "Fe",
        "age" : 19,
        "class" : 2022
    },
    2: {
        "name" : "Ana",
        "age" : 17,
        "class" : 2024
    }
}

@app.get("/")
def index():
    return {"message": "hello-world"}

@app.get("/get-student/{id}")
def get_student(id: int):
    if id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[id]