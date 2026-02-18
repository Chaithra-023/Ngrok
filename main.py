from fastapi import FastAPI
import model
from db import engine
from routes import user_routes

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
