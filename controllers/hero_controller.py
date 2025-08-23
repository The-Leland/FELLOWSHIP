


import uuid
from flask import jsonify, request
from db import db
from models.heroes import Heroes, hero_schema, heroes_schema
from util.reflection import populate_object

def create_hero(data):
    if "hero_name" not in data:
        return jsonify({"message": "Missing required field: hero_name"}), 400

    hero = Heroes(
        hero_id=str(uuid.uuid4()),
        hero_name=data["hero_name"],
        race_id=data.get("race_id"),
        age=data.get("age"),
        health_points=data.get("health_points"),
        is_alive=data.get("is_alive", True)
    )

    try:
        db.session.add(hero)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Database error: {str(e)}"}), 500

    return jsonify({"message": "Hero created successfully", "hero_id": hero.hero_id}), 201

def get_all_heroes():
    heroes = Heroes.query.all()
    return jsonify(heroes_schema.dump(heroes)), 200

def get_hero(hero_id):
    hero = Heroes.query.filter_by(hero_id=hero_id).first()
    if not hero:
        return jsonify({"message": "Hero not found"}), 404
    return jsonify(hero_schema.dump(hero)), 200

def update_hero(hero_id):
    hero = Heroes.query.filter_by(hero_id=hero_id).first()
    if not hero:
        return jsonify({"message": "Hero not found"}), 404

    data = request.form if request.form else request.get_json()
    populate_object(hero, data)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Database error: {str(e)}"}), 500

    return jsonify({"message": "Hero updated successfully", "hero": hero_schema.dump(hero)}), 200

def delete_hero(hero_id):
    hero = Heroes.query.filter_by(hero_id=hero_id).first()
    if not hero:
        return jsonify({"message": "Hero not found"}), 404

    try:
        db.session.delete(hero)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Database error: {str(e)}"}), 500

    return jsonify({"message": "Hero deleted successfully"}), 200
