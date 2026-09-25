from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class User(BaseModel):
    name:str
    age:int
@app.post("/user")
def create_user(user:User):
    return user
@app.get("/user/{user_id}")
def get_user(user_id:int):
    return {f"message : {user_id} of id "}
    