from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from db import get_db


app = FastAPI()


# --- Schemas ---
class UserCreate(BaseModel):
    name: str
    email: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return {"users": []}

@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return {"user": {"name": user.name, "email": user.email}}

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return {"user": {"id": user_id}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
