from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from src.db.db_connection import engine

from src.model.user import User
from src.model.blog import Blog

from src.api.router.user import user_router
from src.api.router.blogs import blog_router


app = FastAPI(
    title="AI Blog Agent API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


SQLModel.metadata.create_all(engine)



app.include_router(user_router)

app.include_router(blog_router)




@app.get("/")
def root():

    return {
        "message": "AI Blog Agent API is running"
    }
