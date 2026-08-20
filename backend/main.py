from fastapi import FastAPI
from pydantic import BaseModel
from sqlmodel import create_engine, SQLModel, Session, select, Field
from dotenv import load_dotenv
import os

load_dotenv("../.env")

POSTGRES_ROUTE = os.getenv("POSTGRES_ROUTE")

if not POSTGRES_ROUTE:
    raise RuntimeError("POSTGRES_ROUTE environment variable is not set")

# Engine creation to connect to PostgreSQL
engine = create_engine(POSTGRES_ROUTE)

class assets(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    type: str
    location: str
    status: str

class Asset(BaseModel):
    id: int
    name: str
    type: str
    location: str
    status: str

app = FastAPI()

# Get Methods
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/assets")
def get_asset():
    with Session(engine) as session:
        statement = select(assets)
        resultado = session.exec(statement).first()
        return resultado

@app.get("/assets/{item_id}")
def get_asset_id(item_id: int):
    return {"item_id": item_id}

@app.get("/measurements")
def get_asset():
    return "Connectivity to db stablished, return things"

@app.get("/alerts")
def get_asset():
    return "Connectivity to db stablished, return things"

# Post Methods
@app.post("/assets")
def make_asset(item: Asset):
    return item

@app.post("/measurements")
def make_asset(item: Asset):
    return item
