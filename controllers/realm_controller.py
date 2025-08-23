


import uuid
from sqlalchemy import insert, select, update, delete
from flask import jsonify
from utils.reflection import realms_table, get_session
from models.realms import realm_schema, realms_schema

def create_realm(data):
    session = get_session()

    if "realm_name" not in data:
        return jsonify({"message": "Missing required field: realm_name"}), 400

    realm_id = str(data.get("realm_id") or uuid.uuid4())

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
        return jsonify({"message": f"Database error: {str(e)}"}), 500

    return jsonify({"message": "Realm created successfully", "realm_id": realm_id}), 201

def get_all_realms():
    session = get_session()
    stmt = select(realms_table)
    result = session.execute(stmt).fetchall()
    realms = [dict(row._mapping) for row in result]
    return jsonify(realms_schema.dump(realms)), 200

def get_realm(realm_id):
    session = get_session()
    stmt = select(realms_table).where(realms_table.c.realm_id == realm_id)
    result = session.execute(stmt).first()
    if not result:
        return jsonify({"message": "Realm not found"}), 404
    realm = dict(result._mapping)
    return jsonify(realm_schema.dump(realm)), 200

def update_realm(realm_id, data):
    session = get_session()
    stmt = update(realms_table).where(realms_table.c.realm_id == realm_id).values(**data)
    result = session.execute(stmt)
    if result.rowcount == 0:
        return jsonify({"message": "Realm not found"}), 404
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return jsonify({"message": f"Database error: {str(e)}"}), 500
    return jsonify({"message": "Realm updated successfully"}), 200

def delete_realm(realm_id):
    session = get_session()
    stmt = delete(realms_table).where(realms_table.c.realm_id == realm_id)
    result = session.execute(stmt)
    if result.rowcount == 0:
        return jsonify({"message": "Realm not found"}), 404
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return jsonify({"message": f"Database error: {str(e)}"}), 500
    return jsonify({"message": "Realm deleted successfully"}), 200
