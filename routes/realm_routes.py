


from flask import Blueprint, request, jsonify
from controllers.realm_controller import (
    create_realm,
    get_all_realms,
    get_realm,
    update_realm,
    delete_realm
)
from schemas.realm_schema import RealmSchema

realm_bp = Blueprint("realm_bp", __name__)
realm_schema = RealmSchema()
realm_list_schema = RealmSchema(many=True)

@realm_bp.route('/realm', methods=['POST'])
def add_realm():
    return create_realm(request.get_json())

@realm_bp.route('/realms', methods=['GET'])
def list_realms():
    realms = get_all_realms()
    return jsonify(realm_list_schema.dump(realms)), 200

@realm_bp.route('/realm/<uuid:realm_id>', methods=['GET'])
def get_single_realm(realm_id):
    realm = get_realm(realm_id)
    if not realm:
        return {"message": "Realm not found"}, 404
    return jsonify(realm_schema.dump(realm)), 200

@realm_bp.route('/realm/<uuid:realm_id>', methods=['PUT'])
def update_realm_route(realm_id):
    return update_realm(realm_id, request.get_json())

@realm_bp.route('/realm/delete/<uuid:realm_id>', methods=['DELETE'])
def delete_realm_route(realm_id):
    return delete_realm(realm_id)
