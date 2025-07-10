


import uuid
from models.reflection_models import Race
from utils.reflection import get_session

def create_race(data):
    session = get_session()

    # Validate required fields
    if "race_name" not in data:
        return {"message": "Missing required field: race_name"}, 400

    # Assign UUID if not provided
    data["race_id"] = data.get("race_id", uuid.uuid4())

    new_race = Race(
        race_id=data["race_id"],
        race_name=data["race_name"],
        homeland=data.get("homeland"),
        lifespan=data.get("lifespan")
    )

    session.add(new_race)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {
        "message": f"Race {new_race.race_name} created successfully.",
        "race_id": str(data["race_id"])
    }, 201


def get_all_races():
    session = get_session()
    return session.query(Race).all()


def get_race(race_id):
    session = get_session()
    race = session.query(Race).filter_by(race_id=race_id).first()
    if not race:
        return {"message": "Race not found"}, 404
    return race


def update_race(race_id, data):
    session = get_session()
    race = session.query(Race).filter_by(race_id=race_id).first()

    if not race:
        return {"message": "Race not found"}, 404

    for key, value in data.items():
        setattr(race, key, value)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {"message": "Race updated successfully."}


def delete_race(race_id):
    session = get_session()
    race = session.query(Race).filter_by(race_id=race_id).first()

    if not race:
        return {"message": "Race not found"}, 404

    session.delete(race)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {"message": f"Race {race.race_name} deleted successfully."}

