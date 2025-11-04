from fastapi import FastAPI
from pydantic import BaseModel, Field

app=FastAPI()

class BMI(BaseModel):
    height:float=Field(...,gt=0, description="Height in metres")
    weight:float=Field(...,gt=0, description="Weight in kilograms")

class BMIOutput(BaseModel):
    bmi:float
    category:str

@app.post('/bmi',response_model=BMIOutput)
def calculate_bmi(data:BMI):
    bmi=round(data.weight/(data.height**2),2)

    if bmi<18.5:
        category="Underweight"
    elif bmi<25:
        category="Normal Weight"
    elif bmi<30:
        category="Overweight"
    else:
        category="Obese"

    return {"bmi":bmi, "category":category}            

