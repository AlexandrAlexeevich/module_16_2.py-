from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import constr, conint

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "Главная страница"

@app.get("/user/admin", response_class=HTMLResponse)
async def read_admin():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}", response_class=HTMLResponse)
async def read_user(
    user_id: Annotated[conint(ge=1, le=100), Path(description="Enter User ID")]
):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user/{username}/{age}", response_class=HTMLResponse)
async def read_user_info(
    username: Annotated[constr(min_length=5, max_length=20), Path(description="Enter username")],
    age: Annotated[conint(ge=18, le=120), Path(description="Enter age")]
):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

uvicorn main:app --reload
