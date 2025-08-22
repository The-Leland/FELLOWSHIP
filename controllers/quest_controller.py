


import uuid
from sqlalchemy import insert, select, update, delete
from utils.reflection import quests_table
from utils.reflection import get_session

def create_quest(data):
    session = get_session()
    quest_id = str(data.get("quest_id", uuid.uuid4()))

    stmt = insert(quests_table).values(
        quest_id=quest_id,
        location_id=data["location_id"],
        quest_name=data["quest_name"],
        difficulty=data.get("difficulty"),
        reward_gold=data.get("reward_gold", 0),
        is_completed=data.get("is_completed", False)
    )

    session.execute(stmt)
    session.commit()
    return {"message": "Quest created", "quest_id": quest_id}, 201

def get_all_quests():
    session = get_session()
    stmt = select(quests_table)
    result = session.execute(stmt).fetchall()
    return [dict(row._mapping) for row in result]

def get_quests_by_difficulty(difficulty_level):
    session = get_session()
    stmt = select(quests_table).where(quests_table.c.difficulty == difficulty_level)
    result = session.execute(stmt).fetchall()
    return [dict(row._mapping) for row in result]

def get_quest(quest_id):
    session = get_session()
    stmt = select(quests_table).where(quests_table.c.quest_id == quest_id)
    result = session.execute(stmt).first()
    if not result:
        return {"message": "Quest not found"}, 404
    return dict(result._mapping)

def update_quest(quest_id, data):
    session = get_session()
    stmt = update(quests_table).where(quests_table.c.quest_id == quest_id).values(**data)
    result = session.execute(stmt)
    if result.rowcount == 0:
        return {"message": "Quest not found"}, 404
    session.commit()
    return {"message": "Quest updated successfully"}

def mark_quest_completed(quest_id):
    session = get_session()
    stmt = update(quests_table).where(quests_table.c.quest_id == quest_id).values(is_completed=True)
    result = session.execute(stmt)
    if result.rowcount == 0:
        return {"message": "Quest not found"}, 404
    session.commit()
    return {"message": "Quest marked as completed"}

def delete_quest(quest_id):
    session = get_session()
    stmt = delete(quests_table).where(quests_table.c.quest_id == quest_id)
    result = session.execute(stmt)
    if result.rowcount == 0:
        return {"message": "Quest not found"}, 404
    session.commit()
    return {"message": "Quest deleted"}
