


from marshmallow import Schema, fields

class AbilitySchema(Schema):
    ability_id = fields.UUID(dump_only=True)
    hero_id = fields.UUID(required=True)
    ability_name = fields.Str(required=True)
    power_level = fields.Int()

    
