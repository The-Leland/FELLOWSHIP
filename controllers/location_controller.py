


import uuid
from sqlalchemy import insert, select, update, delete
from utils.reflection import locations_table
from utils.reflection import get_session

def create_location(data):
    session = get_session()

    if "location_name" not in data or "realm_id" not in data:
        return {"message": "Missing required fields: location_name and realm_id"}, 400

    location_id = str(data.get("location_id", uuid.uuid4()))

    stmt = insert(locations_table).values(
        location_id=location_id,
        location_name=data["location_name"],
        realm_id=data["realm_id"],
        danger_level=data.get("danger_level", 1)
    )

    try:
        session.execute(stmt)
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {"message": "Location created", "location_id": location_id}, 201

def get_all_locations():
    session = get_session()
    stmt = select(locations_table)
    result = session.execute(stmt).fetchall()
    return [dict(row._mapping) for row in result]

def get_location(location_id):
    session = get_session()
    stmt = select(locations_table).where(locations_table.c.location_id == location_id)
    result = session.execute(stmt).first()
    if not result:
        return {"message": "Location not found"}, 404
    return dict(result._mapping)

def update_location(location_id, data):
    session = get_session()
    stmt = update(locations_table).where(locations_table.c.location_id == location_id).values(**data)
    result = session.execute(stmt)
    if result.rowcount == 0:
        return {"message": "Location not found"}, 404
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500
    return {"message": "Location updated successfully"}

def delete_location(location_id):
    session = get_session()
    stmt = delete(locations_table).where(locations_table.c.location_id == location_id)
    result = session.execute(stmt)
    if result.rowcount == 0:
        return {"message": "Location not found"}, 404
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500
    return {"message": "Location deleted successfully"}
