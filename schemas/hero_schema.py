


from marshmallow import Schema, fields, validate

class AbilitySchema(Schema):
    ability_id = fields.UUID(dump_only=True)
    ability_name = fields.Str()
    power_level = fields.Int()

class QuestSchema(Schema):
    quest_id = fields.UUID(dump_only=True)
    quest_name = fields.Str()
    is_completed = fields.Bool()

class HeroSchema(Schema):
    hero_id = fields.UUID(dump_only=True)
    hero_name = fields.Str(required=True)
    age = fields.Int(validate=validate.Range(min=0))
    health_points = fields.Int()
    is_alive = fields.Bool()
    race_id = fields.UUID()

    abilities = fields.Nested(AbilitySchema, many=True, dump_only=True)
    quests = fields.Nested(QuestSchema, many=True, dump_only=True)

