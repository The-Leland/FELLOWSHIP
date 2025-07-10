


import uuid
from models.reflection_models import Location
from utils.reflection import get_session

def create_location(data):
    session = get_session()
    if "location_name" not in data or "realm_id" not in data:
        return {"message": "Missing required fields: location_name and realm_id"}, 400

    data["location_id"] = data.get("location_id", uuid.uuid4())

    new_location = Location(
        location_id=data["location_id"],
        location_name=data["location_name"],
        realm_id=data["realm_id"],
        danger_level=data.get("danger_level", 1)
    )

    session.add(new_location)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {"message": "Location created", "location_id": str(data["location_id"])}, 201


def get_all_locations():
    return get_session().query(Location).all()


def get_location(location_id):
    location = get_session().query(Location).filter_by(location_id=location_id).first()
    if not location:
        return {"message": "Location not found"}, 404
    return location


def update_location(location_id, data):
    session = get_session()
    location = session.query(Location).filter_by(location_id=location_id).first()
    if not location:
        return {"message": "Location not found"}, 404

    for key, value in data.items():
        setattr(location, key, value)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {"message": "Location updated successfully"}


def delete_location(location_id):
    session = get_session()
    location = session.query(Location).filter_by(location_id=location_id).first()
    if not location:
        return {"message": "Location not found"}, 404

    session.delete(location)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Database error: {str(e)}"}, 500

    return {"message": "Location deleted successfully"}
