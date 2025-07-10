


from datetime import datetime
from models.reflection_models import HeroQuest
from utils.reflection import get_session

def assign_hero_to_quest(data):
    session = get_session()
    required_fields = ["hero_id", "quest_id"]
    if not all(field in data for field in required_fields):
        return {"message": "Missing hero_id or quest_id"}, 400

    existing = session.query(HeroQuest).filter_by(
        hero_id=data["hero_id"], quest_id=data["quest_id"]
    ).first()
    if existing:
        return {"message": "Hero already assigned to this quest"}, 409

    new_assignment = HeroQuest(
        hero_id=data["hero_id"],
        quest_id=data["quest_id"],
        date_joined=data.get("date_joined", datetime.utcnow())
    )

    session.add(new_assignment)
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Error assigning hero to quest: {str(e)}"}, 500

    return {"message": "Hero assigned to quest successfully"}, 201


def get_hero_quests(hero_id):
    return get_session().query(HeroQuest).filter_by(hero_id=hero_id).all()
