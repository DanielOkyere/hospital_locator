from fastapi import FastAPI, Depends

from api.database import engine, Base
from api.routes import user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_routes.router)

@app.get('/')
async def home():
    return {"Hello World"}

