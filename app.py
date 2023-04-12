from fastapi import FastAPI, Depends, Request

from api.database import engine, Base
from api.routes import user_routes, auth
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount('/static', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(user_routes.router)
app.include_router(auth.router)

@app.get('/', response_class=HTMLResponse)
async def home(request: Request ):
    return templates.TemplateResponse("index.html", {"request": request})

