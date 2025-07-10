


from marshmallow import Schema, fields

class HeroSchema(Schema):
    hero_id = fields.UUID(dump_only=True)
    hero_name = fields.Str()

class LocationSchema(Schema):
    location_id = fields.UUID()
    location_name = fields.Str()

class QuestSchema(Schema):
    quest_id = fields.UUID(dump_only=True)
    location_id = fields.UUID(required=True)
    quest_name = fields.Str(required=True)
    difficulty = fields.Str()
    reward_gold = fields.Int()
    is_completed = fields.Bool()

    assigned_heroes = fields.Nested(HeroSchema, many=True, dump_only=True)
    location = fields.Nested(LocationSchema, dump_only=True)
