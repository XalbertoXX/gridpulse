from fastapi import FastAPI, HTTPException
from datetime import datetime
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

class create_asset(SQLModel):
    name: str
    type: str
    location: str

class patch_asset(SQLModel):
    name: str | None = None
    type: str | None = None
    location: str | None = None
    status: str | None = None

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

#table=true si representa a la tabla real
class measurement(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    asset_id: int
    timestamp: datetime 
    temperature: float | None = None
    voltage: float | None = None
    current: float | None = None
    load_percentage: float | None = None
    frequency: float | None = None

class create_measure(SQLModel):
    asset_id: int
    timestamp: datetime 
    temperature: float | None = None
    voltage: float | None = None
    current: float | None = None
    load_percentage: float | None = None
    frequency: float | None = None

app = FastAPI()

# Get Methods
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/assets")
def get_asset():
    with Session(engine) as session:
        statement = select(assets)
        resultado = session.exec(statement)
        return resultado

@app.get("/assets/{item_id}")
def get_asset_id(item_id: int):
    with Session(engine) as session:
        statement = select(assets).where(assets.id == item_id)
        resultado = session.exec(statement).first()
        return resultado

@app.get("/measurements")
def get_asset():
    with Session(engine) as session:
        statement = select(measurement)
        resultado = session.exec(statement)
        return resultado

@app.get("/alerts")
def get_asset():
    return "Connectivity to db stablished, return things"

# Post Methods
@app.post("/assets") # Se pide que se pase lo que se establece en el modelo de datos
def make_asset(item: create_asset):
    #Se crea un asset nuevo con la información mandada del create_asset 
    new_asset = assets(
        name=item.name,
        type=item.type,
        location=item.location,
        status="active"
    )

    with Session(engine) as session:
        session.add(new_asset)
        session.commit()
        session.refresh(new_asset)

    return new_asset

@app.post("/measurements/{item_id}")
def make_asset(item: measurement):
    with Session(engine) as session:
        statement = select(assets).where(assets.id == item.asset_id)
        resultado = session.exec(statement).first()
        if resultado != None:
            new_measurement = measurement(

            )
            session.add(new_measurement)
            session.commit()
        else:
            raise HTTPException(status_code=404, detail="Item not found")
        

    with Session(engine) as session:
        statement = select(measurement)
        resultado = session.exec(statement)
    return re

# Patch Methods
@app.patch("/assets/{item_id}")
def update_asset(item_id: int, asset_update: patch_asset):
    with Session(engine) as session:
        statement = select(assets).where(assets.id == item_id)
        resultado = session.exec(statement).first()

        if resultado != None:
            update_data = asset_update.model_dump(exclude_unset=True)

            if not update_data:
                raise HTTPException(status_code=404, detail="Item not found")
            
            for field, value in update_data.items():
                setattr(resultado, field, value)

            session.add(resultado)
            session.commit()
            session.refresh(resultado)

            return resultado
        
        else:
            raise HTTPException(status_code=404, detail="Item not found")

# Delete Methods
@app.delete("/assets/{item_id}")
def remove_item(item_id: int):
    with Session(engine) as session:
        statement = select(assets).where(assets.id == item_id)
        resultado = session.exec(statement).first()
        if resultado != None:
            session.delete(resultado)
            session.commit()
            return {"message": "Deleted"}
        else:
            raise HTTPException(status_code=404, detail="Item not found")