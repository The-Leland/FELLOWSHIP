


import uuid
from models.reflection_models import Ability
from utils.reflection import get_session

def create_ability(data):
    session = get_session()
    if "ability_name" not in data or "hero_id" not in data:
        return {"message": "Missing required fields: ability_name and hero_id"}, 400

    data["ability_id"] = data.get("ability_id", uuid.uuid4())

    new_ability = Ability(
        ability_id=data["ability_id"],
        hero_id=data["hero_id"],
        ability_name=data["ability_name"],
        power_level=data.get("power_level", 1)
    )

    session.add(new_ability)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {"message": "Ability created successfully", "ability_id": str(data["ability_id"])}, 201


def get_all_abilities():
    return get_session().query(Ability).all()


def get_ability(ability_id):
    ability = get_session().query(Ability).filter_by(ability_id=ability_id).first()
    if not ability:
        return {"message": "Ability not found"}, 404
    return ability


def update_ability(ability_id, data):
    session = get_session()
    ability = session.query(Ability).filter_by(ability_id=ability_id).first()
    if not ability:
        return {"message": "Ability not found"}, 404

    for key, value in data.items():
        setattr(ability, key, value)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {"message": "Ability updated successfully"}


def delete_ability(ability_id):
    session = get_session()
    ability = session.query(Ability).filter_by(ability_id=ability_id).first()
    if not ability:
        return {"message": "Ability not found"}, 404

    session.delete(ability)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {"message": "Ability deleted successfully"}
