


from datetime import datetime
from sqlalchemy import insert, select
from utils.reflection import hero_quests_table
from utils.reflection import get_session

def assign_hero_to_quest(data):
    session = get_session()
    if "hero_id" not in data or "quest_id" not in data:
        return {"message": "Missing hero_id or quest_id"}, 400

    stmt = select(hero_quests_table).where(
        hero_quests_table.c.hero_id == data["hero_id"],
        hero_quests_table.c.quest_id == data["quest_id"]
    )
    existing = session.execute(stmt).first()
    if existing:
        return {"message": "Hero already assigned to this quest"}, 409

    stmt = insert(hero_quests_table).values(
        hero_id=data["hero_id"],
        quest_id=data["quest_id"],
        date_joined=data.get("date_joined", datetime.utcnow())
    )

    try:
        session.execute(stmt)
        session.commit()
    except Exception as e:
        session.rollback()
        return {"message": f"Error assigning hero to quest: {str(e)}"}, 500

    return {"message": "Hero assigned to quest successfully"}, 201

def get_hero_quests(hero_id):
    session = get_session()
    stmt = select(hero_quests_table).where(hero_quests_table.c.hero_id == hero_id)
    result = session.execute(stmt).fetchall()
    return [dict(row._mapping) for row in result]
