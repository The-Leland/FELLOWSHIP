


import uuid
from models.reflection_models import Quest
from utils.reflection import get_session

def create_quest(data):
    session = get_session()
    data["quest_id"] = data.get("quest_id", uuid.uuid4())
    new_quest = Quest(
        quest_id=data["quest_id"],
        location_id=data["location_id"],
        quest_name=data["quest_name"],
        difficulty=data.get("difficulty"),
        reward_gold=data.get("reward_gold", 0),
        is_completed=data.get("is_completed", False)
    )
    session.add(new_quest)
    session.commit()
    return {"message": "Quest created", "quest_id": str(new_quest.quest_id)}, 201

def get_all_quests():
    session = get_session()
    return session.query(Quest).all()

def get_quests_by_difficulty(difficulty_level):
    session = get_session()
    return session.query(Quest).filter_by(difficulty=difficulty_level).all()

def get_quest(quest_id):
    session = get_session()
    return session.query(Quest).filter_by(quest_id=quest_id).first()

def update_quest(quest_id, data):
    session = get_session()
    quest = session.query(Quest).filter_by(quest_id=quest_id).first()
    if not quest:
        return {"message": "Quest not found"}, 404
    for key, value in data.items():
        setattr(quest, key, value)
    session.commit()
    return {"message": "Quest updated successfully"}

def mark_quest_complete(quest_id):
    session = get_session()
    quest = session.query(Quest).filter_by(quest_id=quest_id).first()
    if not quest:
        return {"message": "Quest not found"}, 404
    quest.is_completed = True
    session.commit()
    return {"message": "Quest marked as completed"}

def delete_quest(quest_id):
    session = get_session()
    quest = session.query(Quest).filter_by(quest_id=quest_id).first()
    if not quest:
        return {"message": "Quest not found"}, 404
    session.delete(quest)
    session.commit()
    return {"message": "Quest deleted"}
