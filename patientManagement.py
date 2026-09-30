from fastapi import FastAPI
import json
app=FastAPI()
@app.get("/")
def load_data():
    with open ('pateints.json','r') as f:
        data=json.load(f)
    return data
def hello():
    return{f"message : this is a pateint management "}
app.get("/veiw")
def get_view():
    return load_data()
#path parameter
@app.get("/patient/{patient_id}")
def view_point(patient_id: str):
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    return{"error"}
    
    




    