


from marshmallow import Schema, fields
from datetime import datetime

class HeroQuestSchema(Schema):
    hero_id = fields.UUID(required=True)
    quest_id = fields.UUID(required=True)
    date_joined = fields.DateTime()

    
