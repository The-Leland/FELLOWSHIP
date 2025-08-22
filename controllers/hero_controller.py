


import uuid
from sqlalchemy import insert, select, update, delete
from utils.reflection import heroes_table
from utils.reflection import get_session

def create_hero(data):
    session = get_session()
    hero_id = str(data.get("hero_id", uuid.uuid4()))
    stmt = insert(heroes_table).values(
        hero_id=hero_id,
        hero_name=data["hero_name"],
        origin_world=data.get("origin_world")
    )
    session.execute(stmt)
    session.commit()
    return {"message": "Hero created successfully", "hero_id": hero_id}, 201

def get_all_heroes():
    session = get_session()
    stmt = select(heroes_table)
    result = session.execute(stmt).fetchall()
    return [dict(row._mapping) for row in result]

def get_hero(hero_id):
    session = get_session()
    stmt = select(heroes_table).where(heroes_table.c.hero_id == hero_id)
    result = session.execute(stmt).first()
    if not result:
        return {"message": "Hero not found"}, 404
    return dict(result._mapping)

def update_hero(hero_id, data):
    session = get_session()
    stmt = update(heroes_table).where(heroes_table.c.hero_id == hero_id).values(**data)
    result = session.execute(stmt)
    if result.rowcount == 0:
        return {"message": "Hero not found"}, 404
    session.commit()
    return {"message": "Hero updated"}

def delete_hero(hero_id):
    session = get_session()
    stmt = delete(heroes_table).where(heroes_table.c.hero_id == hero_id)
    result = session.execute(stmt)
    if result.rowcount == 0:
        return {"message": "Hero not found"}, 404
    session.commit()
    return {"message": "Hero deleted"}
