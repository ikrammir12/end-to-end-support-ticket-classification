from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

database = ['']

def read_numbers():
    numbers = []
    with open("database.txt", "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                numbers.append(int(line))
    return numbers

def write_number(number: int):
    with open('database.txt','w') as f:
        json.dump(number,f)

@app.get('/')
def read_root():
    return {"message": "Welcome to the Support Ticket Classification API!"}

@app.post('/add_number/{number}')
def add_number(number: int):
    write_number(number)
    return {'message': f'{number} added to the database'}
    

@app.get("/get_numbers/{number}")
def get_number(number: int):
    numbers = read_numbers()

    if number in numbers:
        return {"message": f"{number} is in database"}
    else:
        return {"message": f"{number} not found"}
   