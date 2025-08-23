


from util.reflection import reflect_db
from flask_marshmallow import Marshmallow

Base, engine = reflect_db()

Hero = Base.classes.heroes
Race = Base.classes.races
Quest = Base.classes.quests
Location = Base.classes.locations
Realm = Base.classes.realms
Ability = Base.classes.abilities
HeroQuest = Base.classes.hero_quest

ma = Marshmallow()

class HeroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hero
        load_instance = True

class RaceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Race
        load_instance = True

class QuestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Quest
        load_instance = True

class LocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Location
        load_instance = True

class RealmSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Realm
        load_instance = True

class AbilitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ability
        load_instance = True

class HeroQuestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HeroQuest
        load_instance = True

hero_schema = HeroSchema()
heroes_schema = HeroSchema(many=True)

race_schema = RaceSchema()
races_schema = RaceSchema(many=True)

quest_schema = QuestSchema()
quests_schema = QuestSchema(many=True)

location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)

realm_schema = RealmSchema()
realms_schema = RealmSchema(many=True)

ability_schema = AbilitySchema()
abilities_schema = AbilitySchema(many=True)

hero_quest_schema = HeroQuestSchema()
hero_quests_schema = HeroQuestSchema(many=True)
