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


# ============================================
# CORS
# ============================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# ============================================
# DATABASE
# ============================================

SQLModel.metadata.create_all(engine)


# ============================================
# ROUTERS
# ============================================

app.include_router(user_router)

app.include_router(blog_router)


# ============================================
# ROOT
# ============================================

@app.get("/")
def root():

    return {
        "message": "AI Blog Agent API is running"
    }

# from sqlmodel import SQLModel
# from src.model.user import User
# from src.db.db_connection import engine
# from fastapi import FastAPI
# from src.api.router import user_router,blog_router



# SQLModel.metadata.create_all(engine)

# app=FastAPI()
# @app.get("/")
# def home():
#     return "This is Home Screeen !"

# print("Table Created Sucessfully ")

# app.include_router(user_router)
# app.include_router(blog_router)
