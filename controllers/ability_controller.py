


import uuid
from flask import jsonify, request
from db import db
from models.abilities import Abilities, ability_schema, abilities_schema
from util.reflection import populate_object

def create_ability(data):
    if "ability_name" not in data or "hero_id" not in data:
        return jsonify({"message": "Missing required fields: ability_name and hero_id"}), 400

    ability = Abilities(
        ability_id=str(uuid.uuid4()),
        hero_id=data["hero_id"],
        ability_name=data["ability_name"],
        power_level=data.get("power_level", 1)
    )

    try:
        db.session.add(ability)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Database error: {str(e)}"}), 500

    return jsonify({"message": "Ability created successfully", "ability_id": ability.ability_id}), 201

def get_all_abilities():
    abilities = Abilities.query.all()
    return jsonify(abilities_schema.dump(abilities)), 200

def get_ability(ability_id):
    ability = Abilities.query.filter_by(ability_id=ability_id).first()
    if not ability:
        return jsonify({"message": "Ability not found"}), 404
    return jsonify(ability_schema.dump(ability)), 200

def update_ability(ability_id):
    ability = Abilities.query.filter_by(ability_id=ability_id).first()
    if not ability:
        return jsonify({"message": "Ability not found"}), 404

    data = request.form if request.form else request.get_json()
    populate_object(ability, data)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Database error: {str(e)}"}), 500

    return jsonify({"message": "Ability updated successfully", "ability": ability_schema.dump(ability)}), 200

def delete_ability(ability_id):
    ability = Abilities.query.filter_by(ability_id=ability_id).first()
    if not ability:
        return jsonify({"message": "Ability not found"}), 404

    try:
        db.session.delete(ability)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Database error: {str(e)}"}), 500

    return jsonify({"message": "Ability deleted successfully"}), 200
