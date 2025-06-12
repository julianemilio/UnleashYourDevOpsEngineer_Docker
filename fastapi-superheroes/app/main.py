from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Data models
class SuperHero(BaseModel):
    id: int
    name: str
    power: str
    universe: str

# In-memory DB (for demo)
superheroes_db = [
    SuperHero(id=1, name="Spider-Man", power="Agility and spider-sense", universe="Marvel"),
    SuperHero(id=2, name="Batman", power="High intelligence and gadgets", universe="DC"),
]

# Routes
@app.get("/superheroes", response_model=List[SuperHero])
def get_superheroes():
    return superheroes_db

@app.get("/superheroes/{hero_id}", response_model=SuperHero)
def get_hero(hero_id: int):
    for hero in superheroes_db:
        if hero.id == hero_id:
            return hero
    return {"error": "Hero not found"}

@app.post("/superheroes", response_model=SuperHero)
def create_hero(hero: SuperHero):
    superheroes_db.append(hero)
    return hero