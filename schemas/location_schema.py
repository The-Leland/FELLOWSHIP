


from marshmallow import Schema, fields

class QuestSchema(Schema):
    quest_id = fields.UUID(dump_only=True)
    quest_name = fields.Str()
    is_completed = fields.Bool()

class LocationSchema(Schema):
    location_id = fields.UUID(dump_only=True)
    realm_id = fields.UUID(required=True)
    location_name = fields.Str(required=True)
    danger_level = fields.Int()

    quests = fields.Nested(QuestSchema, many=True, dump_only=True)
