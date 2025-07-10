


from flask import Blueprint, request, jsonify
from controllers.quest_controller import (
    create_quest,
    get_all_quests,
    get_quest,
    get_quests_by_difficulty,
    update_quest,
    mark_quest_completed,
    delete_quest
)
from schemas.quest_schema import QuestSchema

quest_bp = Blueprint("quest_bp", __name__)
quest_schema = QuestSchema()
quest_list_schema = QuestSchema(many=True)

@quest_bp.route('/quest', methods=['POST'])
def add_quest():
    return create_quest(request.get_json())

@quest_bp.route('/quests', methods=['GET'])
def list_quests():
    quests = get_all_quests()
    return jsonify(quest_list_schema.dump(quests)), 200

@quest_bp.route('/quest/<uuid:quest_id>', methods=['GET'])
def get_single_quest(quest_id):
    quest = get_quest(quest_id)
    if not quest:
        return {"message": "Quest not found"}, 404
    return jsonify(quest_schema.dump(quest)), 200

@quest_bp.route('/quests/<difficulty>', methods=['GET'])
def get_quests_by_difficulty_route(difficulty):
    quests = get_quests_by_difficulty(difficulty)
    return jsonify(quest_list_schema.dump(quests)), 200

@quest_bp.route('/quest/<uuid:quest_id>', methods=['PUT'])
def update_quest_route(quest_id):
    return update_quest(quest_id, request.get_json())

@quest_bp.route('/quest/<uuid:quest_id>/complete', methods=['PUT'])
def complete_quest_route(quest_id):
    return mark_quest_completed(quest_id)

@quest_bp.route('/quest/delete/<uuid:quest_id>', methods=['DELETE'])
def delete_quest_route(quest_id):
    return delete_quest(quest_id)
