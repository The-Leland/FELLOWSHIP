


from flask import Blueprint, request, jsonify
from controllers.location_controller import (
    create_location,
    get_all_locations,
    get_location,
    update_location,
    delete_location
)
from schemas.location_schema import LocationSchema

location_bp = Blueprint("location_bp", __name__)
location_schema = LocationSchema()
location_list_schema = LocationSchema(many=True)

@location_bp.route('/location', methods=['POST'])
def add_location():
    return create_location(request.get_json())

@location_bp.route('/locations', methods=['GET'])
def list_locations():
    locations = get_all_locations()
    return jsonify(location_list_schema.dump(locations)), 200

@location_bp.route('/location/<uuid:location_id>', methods=['GET'])
def get_single_location(location_id):
    location = get_location(location_id)
    if not location:
        return {"message": "Location not found"}, 404
    return jsonify(location_schema.dump(location)), 200

@location_bp.route('/location/<uuid:location_id>', methods=['PUT'])
def update_location_route(location_id):
    return update_location(location_id, request.get_json())

@location_bp.route('/location/delete/<uuid:location_id>', methods=['DELETE'])
def delete_location_route(location_id):
    return delete_location(location_id)
