


import uuid
from sqlalchemy import insert, select, update, delete
from utils.reflection import realms_table
from utils.reflection import get_session

def create_realm(data):
    session = get_session()

    if "realm_name" not in data:
        return {"message": "Missing required field: realm_name"}, 400

    realm_id = str(data.get("realm_id", uuid.uuid4()))

    stmt = insert(realms_table).values(
        realm_id=realm_id,
        realm_name=data["realm_name"],
        ruler=data.get("ruler")
    )

    try:
        session.execute(stmt)
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {"message": "Realm created successfully", "realm_id": realm_id}, 201

def get_all_realms():
    session = get_session()
    stmt = select(realms_table)
    result = session.execute(stmt).fetchall()
    return [dict(row._mapping) for row in result]

def get_realm(realm_id):
    session = get_session()
    stmt = select(realms_table).where(realms_table.c.realm_id == realm_id)
    result = session.execute(stmt).first()
    if not result:
        return {"message": "Realm not found"}, 404
    return dict(result._mapping)

def update_realm(realm_id, data):
    session = get_session()
    stmt = update(realms_table).where(realms_table.c.realm_id == realm_id).values(**data)
    result = session.execute(stmt)
    if result.rowcount == 0:
        return {"message": "Realm not found"}, 404
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500
    return {"message": "Realm updated successfully"}

def delete_realm(realm_id):
    session = get_session()
    stmt = delete(realms_table).where(realms_table.c.realm_id == realm_id)
    result = session.execute(stmt)
    if result.rowcount == 0:
        return {"message": "Realm not found"}, 404
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500
    return {"message": "Realm deleted successfully"}
