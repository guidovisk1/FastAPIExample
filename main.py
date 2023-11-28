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

@app.get('/get-by-name')
def get_student_by_name(name: str):
    for student_id, student_data in students.items():
        if student_data["name"] == name:
            return student_data
    return {"Data": "Name not found"}