


import uuid
from sqlalchemy import insert, select, update, delete
from utils.reflection import abilities_table
from utils.reflection import get_session

def create_ability(data):
    session = get_session()

    if "ability_name" not in data or "hero_id" not in data:
        return {"message": "Missing required fields: ability_name and hero_id"}, 400

    ability_id = str(data.get("ability_id", uuid.uuid4()))

    stmt = insert(abilities_table).values(
        ability_id=ability_id,
        hero_id=data["hero_id"],
        ability_name=data["ability_name"],
        power_level=data.get("power_level", 1)
    )

    try:
        session.execute(stmt)
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {"message": "Ability created successfully", "ability_id": ability_id}, 201


def get_all_abilities():
    session = get_session()
    stmt = select(abilities_table)
    result = session.execute(stmt).fetchall()
    return [dict(row._mapping) for row in result]


def get_ability(ability_id):
    session = get_session()
    stmt = select(abilities_table).where(abilities_table.c.ability_id == ability_id)
    result = session.execute(stmt).first()
    if not result:
        return {"message": "Ability not found"}, 404
    return dict(result._mapping)


def update_ability(ability_id, data):
    session = get_session()
    stmt = update(abilities_table).where(abilities_table.c.ability_id == ability_id).values(**data)
    try:
        result = session.execute(stmt)
        if result.rowcount == 0:
            return {"message": "Ability not found"}, 404
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500
    return {"message": "Ability updated successfully"}


def delete_ability(ability_id):
    session = get_session()
    stmt = delete(abilities_table).where(abilities_table.c.ability_id == ability_id)
    try:
        result = session.execute(stmt)
        if result.rowcount == 0:
            return {"message": "Ability not found"}, 404
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500
    return {"message": "Ability deleted successfully"}
