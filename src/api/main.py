from sqlmodel import SQLModel
from src.model.user import User
from src.db.db_connection import engine
from fastapi import FastAPI
from src.api.router import user_router



SQLModel.metadata.create_all(engine)

app=FastAPI()
@app.get("/")
def home():
    return "This is Home Screeen !"

print("Table Created Sucessfully ")

app.include_router(user_router)