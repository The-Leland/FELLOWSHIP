


import uuid
from sqlalchemy import insert, select, update, delete
from utils.reflection import races_table
from utils.reflection import get_session

def create_race(data):
    session = get_session()

    if "race_name" not in data:
        return {"message": "Missing required field: race_name"}, 400

    race_id = str(data.get("race_id", uuid.uuid4()))

    stmt = insert(races_table).values(
        race_id=race_id,
        race_name=data["race_name"],
        homeland=data.get("homeland"),
        lifespan=data.get("lifespan")
    )

    try:
        session.execute(stmt)
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {
        "message": f"Race {data['race_name']} created successfully.",
        "race_id": race_id
    }, 201

def get_all_races():
    session = get_session()
    stmt = select(races_table)
    result = session.execute(stmt).fetchall()
    return [dict(row._mapping) for row in result]

def get_race(race_id):
    session = get_session()
    stmt = select(races_table).where(races_table.c.race_id == race_id)
    result = session.execute(stmt).first()
    if not result:
        return {"message": "Race not found"}, 404
    return dict(result._mapping)

def update_race(race_id, data):
    session = get_session()
    stmt = update(races_table).where(races_table.c.race_id == race_id).values(**data)
    result = session.execute(stmt)
    if result.rowcount == 0:
        return {"message": "Race not found"}, 404
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500
    return {"message": "Race updated successfully."}

def delete_race(race_id):
    session = get_session()
    stmt = delete(races_table).where(races_table.c.race_id == race_id)
    result = session.execute(stmt)
    if result.rowcount == 0:
        return {"message": "Race not found"}, 404
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500
    return {"message": f"Race deleted successfully."}
