


from marshmallow import Schema, fields

class HeroSchema(Schema):
    hero_id = fields.UUID(dump_only=True)
    hero_name = fields.Str()
    age = fields.Int()
    health_points = fields.Int()
    is_alive = fields.Bool()

class RaceSchema(Schema):
    race_id = fields.UUID(dump_only=True)
    race_name = fields.Str(required=True)
    homeland = fields.Str()
    lifespan = fields.Int()

    heroes = fields.Nested(HeroSchema, many=True, dump_only=True)

