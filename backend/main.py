from fastapi import FastAPI
from pydantic import BaseModel

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
    return "Connectivity to db stablished, return things"

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

    
