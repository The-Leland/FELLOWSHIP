


from flask import Blueprint, request, jsonify
from controllers.hero_controller import (
    create_hero,
    get_all_heroes,
    get_hero,
    update_hero,
    delete_hero,
    get_alive_heroes
)
from controllers.hero_quest_controller import get_hero_quests
from controllers.ability_controller import get_all_abilities

from schemas.hero_schema import HeroSchema
from schemas.quest_schema import QuestSchema
from schemas.ability_schema import AbilitySchema

hero_bp = Blueprint("hero_bp", __name__)
hero_schema = HeroSchema()
hero_list_schema = HeroSchema(many=True)
quest_schema = QuestSchema(many=True)
ability_schema = AbilitySchema(many=True)

@hero_bp.route('/hero', methods=['POST'])
def add_hero():
    return create_hero(request.get_json())

@hero_bp.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = get_all_heroes()
    return jsonify(hero_list_schema.dump(heroes))

@hero_bp.route('/heroes/alive', methods=['GET'])
def get_alive_heroes_route():
    heroes = get_alive_heroes()
    return jsonify(hero_list_schema.dump(heroes))

@hero_bp.route('/hero/<uuid:hero_id>', methods=['GET'])
def get_single_hero(hero_id):
    hero = get_hero(hero_id)
    if not hero:
        return {"message": "Hero not found"}, 404

    quests = get_hero_quests(hero_id)
    all_abilities = get_all_abilities()
    abilities = [a for a in all_abilities if str(a.hero_id) == str(hero_id)]

    hero_data = hero_schema.dump(hero)
    hero_data["quests"] = quest_schema.dump(quests)
    hero_data["abilities"] = ability_schema.dump(abilities)

    return jsonify(hero_data), 200

@hero_bp.route('/hero/<uuid:hero_id>', methods=['PUT'])
def update_hero_route(hero_id):
    return update_hero(hero_id, request.get_json())

@hero_bp.route('/hero/delete/<uuid:hero_id>', methods=['DELETE'])
def delete_hero_route(hero_id):
    return delete_hero(hero_id)

@hero_bp.route('/hero/<uuid:hero_id>/quests', methods=['GET'])
def get_hero_quests_route(hero_id):
    quests = get_hero_quests(hero_id)
    return jsonify(quest_schema.dump(quests)), 200
