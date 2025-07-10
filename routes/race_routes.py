


import uuid
from models.reflection_models import Race, Hero
from utils.reflection import get_session

def create_race(data):
    session = get_session()
    data["race_id"] = data.get("race_id", uuid.uuid4())
    new_race = Race(
        race_id=data["race_id"],
        race_name=data["race_name"],
        homeland=data.get("homeland"),
        lifespan=data.get("lifespan")
    )
    session.add(new_race)
    session.commit()
    return {"message": f"Race {new_race.race_name} created successfully.", "race_id": str(data["race_id"])}, 201

def get_all_races():
    session = get_session()
    return session.query(Race).all()

def get_race(race_id):
    session = get_session()
    return session.query(Race).filter_by(race_id=race_id).first()

def update_race(race_id, data):
    session = get_session()
    race = session.query(Race).filter_by(race_id=race_id).first()
    if not race:
        return {"message": "Race not found"}, 404
    for key, value in data.items():
        setattr(race, key, value)
    session.commit()
    return {"message": "Race updated successfully"}

def delete_race(race_id):
    session = get_session()
    race = session.query(Race).filter_by(race_id=race_id).first()
    if not race:
        return {"message": "Race not found"}, 404

    
    heroes = session.query(Hero).filter_by(race_id=race_id).all()
    if heroes:
        return {"message": "Cannot delete race: heroes are still assigned to this race."}, 400

    session.delete(race)
    session.commit()
    return {"message": "Race deleted successfully"}

