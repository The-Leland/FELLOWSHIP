


from flask import Blueprint, request, jsonify
from controllers.hero_quest_controller import (
    assign_hero_to_quest,
    get_all_hero_quests,
    get_hero_quests,
    delete_hero_quest
)
from schemas.hero_quest_schema import HeroQuestSchema

hero_quest_bp = Blueprint("hero_quest_bp", __name__)
hero_quest_schema = HeroQuestSchema()
hero_quest_list_schema = HeroQuestSchema(many=True)

@hero_quest_bp.route('/hero-quest', methods=['POST'])
def add_hero_quest():
    return assign_hero_to_quest(request.get_json())

@hero_quest_bp.route('/hero-quests', methods=['GET'])
def list_hero_quests():
    assignments = get_all_hero_quests()
    return jsonify(hero_quest_list_schema.dump(assignments)), 200

@hero_quest_bp.route('/hero-quest/delete', methods=['DELETE'])
def delete_hero_quest_route():
    data = request.get_json()
    hero_id = data.get("hero_id")
    quest_id = data.get("quest_id")
    if not hero_id or not quest_id:
        return {"message": "hero_id and quest_id are required"}, 400
    return delete_hero_quest(hero_id, quest_id)
