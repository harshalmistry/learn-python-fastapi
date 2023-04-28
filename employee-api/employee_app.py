from fastapi import FastAPI
from pydantic import BaseModel

# creating application
app = FastAPI()

# this is fake data
fake_employees_data = [
    {
        "id": 1,
        "first_name": "Torrin",
        "last_name": "Conibear",
        "email": "tconibear0@geocities.jp",
        "gender": "Male",
        "age": 47,
        "city": "São José dos Pinhais"
    }, {
        "id": 2,
        "first_name": "Shelbi",
        "last_name": "Risbridger",
        "email": "srisbridger1@globo.com",
        "gender": "Female",
        "age": 72,
        "city": "Tuxi"
    }, {
        "id": 3,
        "first_name": "Nikki",
        "last_name": "Chritchley",
        "email": "nchritchley2@multiply.com",
        "gender": "Female",
        "age": 89,
        "city": "Muqui"
    }, {
        "id": 4,
        "first_name": "Kendall",
        "last_name": "Kelson",
        "email": "kkelson3@jiathis.com",
        "gender": "Male",
        "age": 14,
        "city": "Rantau"
    }, {
        "id": 5,
        "first_name": "Daisey",
        "last_name": "Benns",
        "email": "dbenns4@about.me",
        "gender": "Female",
        "age": 20,
        "city": "Sheffield"
    }, {
        "id": 6,
        "first_name": "Glenn",
        "last_name": "Parkisson",
        "email": "gparkisson5@walmart.com",
        "gender": "Male",
        "age": 65,
        "city": "Meedhoo"
    }, {
        "id": 7,
        "first_name": "Marshall",
        "last_name": "Cicci",
        "email": "mcicci6@admin.ch",
        "gender": "Male",
        "age": 36,
        "city": "Añatuya"
    }, {
        "id": 8,
        "first_name": "Delmar",
        "last_name": "Heimann",
        "email": "dheimann7@jugem.jp",
        "gender": "Male",
        "age": 17,
        "city": "Noebesa"
    }, {
        "id": 9,
        "first_name": "Marika",
        "last_name": "Message",
        "email": "mmessage8@reuters.com",
        "gender": "Agender",
        "age": 54,
        "city": "Ambatolampy"
    }, {
        "id": 10,
        "first_name": "Juliet",
        "last_name": "Reitenbach",
        "email": "jreitenbach9@miitbeian.gov.cn",
        "gender": "Female",
        "age": 51,
        "city": "Masape"
    }
]


# domain model
class Employee(BaseModel):
    id: int | None = None
    first_name: str
    last_name: str
    email: str | None = None
    gender: str | None = None
    age: int
    city: str


# db placeholder for model objects
EMPLOYEES_DB = []


# load data on application startup
@app.on_event("startup")
def load_employees():
    # iterating through json data and creating model objects
    for employee in fake_employees_data:
        EMPLOYEES_DB.append(Employee.parse_obj(employee))
    print("Employees data loaded successfully!")


# creating /employees path handler
@app.get("/employees")
def get_employees():
    return EMPLOYEES_DB
