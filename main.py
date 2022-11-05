from fastapi import FastAPI
from enums import Operation
from pydantic import BaseModel
from fastapi import HTTPException

fastapi = FastAPI()

class Calculate(BaseModel):
    operation_type: Operation
    x: int
    y : int


    

@fastapi.post("/calculate")
async def calculate(value: Calculate):
    value_dict = value.dict()

    if(value.operation_type == Operation.addition) :
        result = calculateAddition(value.x, value.y)
        
    elif(value.operation_type == Operation.subtraction) :
        result = calculate_subtraction(value.x, value.y)
        
    elif(value.operation_type == Operation.multiplication) :
        result = calculate_multiplication(value.x, value.y)
    else :
        raise HTTPException(status_code=404, detail='Operation not found')

    value_dict.update({'slackUsername': 'lonewolve', 'operation_type':value.operation_type, 'result': result})

    return value_dict


# @fastapi.get("/calculate")
# def get_calculate():







def calculateAddition(x: int, y: int):
    return x + y

def calculate_subtraction(x: int, y: int):
    return x - y


def calculate_multiplication(x: int, y: int):
    return x * y






