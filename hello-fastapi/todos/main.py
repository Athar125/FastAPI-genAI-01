from fastapi import FastAPI , Body, Path , Query
import uvicorn
from typing import Union , Optional , Annotated
from pydantic import BaseModel , Field

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
    uvicorn.run("todos.main:app",host="localhost", port=8080, reload=True)  


# Class 2   31 march

userName:str = "Athar"
age:int = 25

listOfStudentName:list[str] = ["First", "Second", "Third"]
car: dict[str, Union[int, str]] = {
    "Model": 2025,
    "color": "black"
}


def getUserFullName(firstName:str ,lastName:str, age:int):
    return firstName + " " + lastName 


class Todo(BaseModel):
    id : int
    title : str  ="any default title value"
    description : str

# path Parameters

@app.get("/students")
def MainRoute():
    return "Server is up and running"  # any type of data wwill send in response.

@app.get("/students/{id}")
def MainRoute1(id):
    print(id)
    return {
        "message":"Server is up and running",
        "output":id
    }


@app.get("/students/{id}/assignments")
def MainRoute2(id):
    print(id)
    return {
        "message":"Server is up and running",
        "output":id
    }

@app.get("/students/{id}/assignments/{assignment_id}")
def MainRoute3(id, assignment_id):
    print(id, assignment_id)
    return {
        "message":"Server is up and running",
        "output":id,
        "assignment":assignment_id
    }
# Predefined values create  in response.

# Query parameters 
# after ? data is query parameters

@app.get("/students/{id}/assignments/{assignment_id}")
def MainRoute4(id, assignment_id, data):
    print(id, assignment_id)
    return {
        "message":"Server is up and running",
        "output":id,
        "assignment":assignment_id
    }

@app.get("/student/{id}/assignments/{assignment_id}")
def MainRoute5(id,assignment_id, data:int, userName:str, count:int):
    print(data)
    return {
        "message":"Server is up and running",
        "output":id,
        "data":data
    }

@app.get("/student1/{id}/assignments/{assignment_id}")
def MainRoute6(id,assignment_id, data:int, userName:str, count:int | None = None):
    print(data)
    return {
        "message":"Server is up and running",
        "output":id,
        "data":data
    }

# the query is the set of key-value pais that go after the ? in a URL, separated by & character.
# http://localhost:8080/student/15/assignments/13?data=123&userName=Athar&count=12
          
# Request body

# class Item(BaseModel):
#     id:int
#     title:str
#     description:str

# @app.get("/student2/{id}/assignments/{assignment_id}")
# def MainRoute7(id,assignment_id, data:int, item:Item):
#     print(data)
#     return item 

# Query parameters and String Validation

@app.get("/blog")
# def getblog(item:Annotated[int, Body()]):
# def getblog(item:Annotated[str, "label"]):
def getblog(item:Annotated[str, Query(max_length=10, min_length=4, pattern="^fix[a-zA-Z0-9]")]):    
    return item

@app.get("/blog1")
def getblog1(item_sf:Annotated[str, Query(title="Saf", description="Sfa", alias="item-test", max_length=10, min_length=4, pattern="^fix[a-zA-Z0-9]")]):    
    return item_sf

# Path parameters and Numeric Validations

@app.get("/admin/{id}")
def home(id:Annotated[int, Path(le=5, ge=3)]):
    return id

# Body - Multiple Parameters

# class Item(BaseModel):
#     id:int
#     title:str
#     description:str

# class User(BaseModel):
#     userName:str

# @app.get("/Admin")
# def office(item:Item, user:User):
#     print(user)    
#     return item

# @app.get("/Admin")
# def office(item:Item, user:User, count:Annotated[int, Body()]):
#     print(user)    
#     return item

# Body Fields

class Item(BaseModel):
    id:int
    title:str
    description:str

class User(BaseModel):
    userName:str = Field(max_length= 10)

