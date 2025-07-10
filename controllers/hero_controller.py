


import uuid
from models.reflection_models import Hero
from utils.reflection import get_session

def create_hero(data):
    session = get_session()
    data["hero_id"] = data.get("hero_id", uuid.uuid4())
    new_hero = Hero(**data)
    session.add(new_hero)
    session.commit()
    return {"message": "Hero created successfully", "hero_id": str(data["hero_id"])}, 201

def get_all_heroes():
    return get_session().query(Hero).all()

def get_hero(hero_id):
    return get_session().query(Hero).filter_by(hero_id=hero_id).first()

def update_hero(hero_id, data):
    session = get_session()
    hero = session.query(Hero).filter_by(hero_id=hero_id).first()
    if not hero: return {"message": "Hero not found"}, 404
    for key, value in data.items():
        setattr(hero, key, value)
    session.commit()
    return {"message": "Hero updated"}

def delete_hero(hero_id):
    session = get_session()
    hero = session.query(Hero).filter_by(hero_id=hero_id).first()
    if not hero: return {"message": "Hero not found"}, 404
    session.delete(hero)
    session.commit()
    return {"message": "Hero deleted"}
