from fastapi import FastAPI
from backend.database import engine, Base
from backend.models import Medicine

app = FastAPI()

@app.on_event("startup")
async def startup():
    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Medicine API"}
