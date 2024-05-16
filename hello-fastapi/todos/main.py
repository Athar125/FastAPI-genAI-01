from fastapi import FastAPI 
import uvicorn
from typing import Union


app = FastAPI()

@app.get("/")
def hello_world():
    return "Hello, world!"

@app.get("/gettodos")
def getTodos():
    print("Get todos called")
    return "gettodos called"

@app.post("/gettodos")
def getTodosPost():
    print("Get post method todos called")
    return "post gettodos called"

@app.get("/getSingleTodo")
def getSingleTodo():
    print("Get todos called")
    return "getSingleTodo called"

@app.put("/updateTodo")
def updateTodo():
    return "updateTodo called"

# Dynamnic Path

@app.get("/gettodo1/{id}")
def getTodo1(id):
    print("Get todos called, id")
    return id

@app.get("/gettodo2/{userName}/{rollNumber}")
def getTodo2(userName , rollNumber):
    print("Get todos called, userName , rollNumber")
    return userName + rollNumber

# Query Param

@app.get("/getSingleTodo1")
def getSingleTodo1(userName:str, rollNumber:str):
    print("Get todos called, userName , rollNumber")
    return "getSingleTodo called"

students = [{
    "userName" : "Athar",
    "rollNumber" : 125
}, {
    "userName" : "Azhar",
    "rollNumber" : 123
}
]

@app.get("/students")
def getStudents():
    return students

@app.get("/addStudent")
def addStudent(userName, rollNumber):
    global students
    students.append({"userName": userName, "rollNumber": rollNumber})
    return students


def start():
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)  


#  Next Class Work

userName:str = "Athar"
age:int = 25

listOfStudentName:list[str] = ["First", "Second", "Third"]
car: dict[str, Union[int, str]] = {
    "Model": 2025,
    "color": "black"
}


def getUserFullName(firstName:str ,lastName:str, age:int):
    return firstName + " " + lastName 