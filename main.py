from fastapi import FastAPI
from enums import Operation
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

class Calculate(BaseModel):
    operation_type: Operation
    x: int
    y : int


@app.get("/")
def user ():
    return {'slackUsername': 'lonewolve' , 'backend':True, 'age':24, 'bio':'My name is Abdul Muizz and i am a final year university student and am an aspiring backend developer.' }


@app.post("/calculate")
def calculate(value: Calculate):
    

    if(value.operation_type == Operation.addition) :
        result = calculateAddition(value.x, value.y)
        
    elif(value.operation_type == Operation.subtraction) :
        result = calculate_subtraction(value.x, value.y)
        
    elif(value.operation_type == Operation.multiplication) :
        result = calculate_multiplication(value.x, value.y)
    else :
        raise HTTPException(status_code=404, detail='Operation not found')

    value_dict ={'slackUsername': 'lonewolve', 'result': result,'operation_type':value.operation_type, }

    return value_dict








def calculateAddition(x: int, y: int):
    return x + y

def calculate_subtraction(x: int, y: int):
    return x - y


def calculate_multiplication(x: int, y: int):
    return x * y






