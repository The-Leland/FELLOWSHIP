


from utils.reflection import reflect_db

Base, _ = reflect_db()

Hero = Base.classes.heroes
Race = Base.classes.races
Quest = Base.classes.quests
Location = Base.classes.locations
Realm = Base.classes.realms
Ability = Base.classes.abilities
HeroQuest = Base.classes.hero_quest  
