


import uuid
from models.reflection_models import Realm
from utils.reflection import get_session

def create_realm(data):
    session = get_session()
    if "realm_name" not in data:
        return {"message": "Missing required field: realm_name"}, 400

    data["realm_id"] = data.get("realm_id", uuid.uuid4())

    new_realm = Realm(
        realm_id=data["realm_id"],
        realm_name=data["realm_name"],
        ruler=data.get("ruler")
    )

    session.add(new_realm)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {"message": "Realm created successfully", "realm_id": str(data["realm_id"])}, 201


def get_all_realms():
    return get_session().query(Realm).all()


def get_realm(realm_id):
    realm = get_session().query(Realm).filter_by(realm_id=realm_id).first()
    if not realm:
        return {"message": "Realm not found"}, 404
    return realm


def update_realm(realm_id, data):
    session = get_session()
    realm = session.query(Realm).filter_by(realm_id=realm_id).first()
    if not realm:
        return {"message": "Realm not found"}, 404

    for key, value in data.items():
        setattr(realm, key, value)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {"message": "Realm updated successfully"}


def delete_realm(realm_id):
    session = get_session()
    realm = session.query(Realm).filter_by(realm_id=realm_id).first()
    if not realm:
        return {"message": "Realm not found"}, 404

    session.delete(realm)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {"message": "Realm deleted successfully"}
