


from routes.hero_routes import hero_bp
from routes.race_routes import race_bp
from routes.quest_routes import quest_bp
from routes.location_routes import location_bp
from routes.realm_routes import realm_bp
from routes.ability_routes import ability_bp
from routes.hero_quest_routes import hero_quest_bp

def register_blueprints(app):
    app.register_blueprint(hero_bp)
    app.register_blueprint(race_bp)
    app.register_blueprint(quest_bp)
    app.register_blueprint(location_bp)
    app.register_blueprint(realm_bp)
    app.register_blueprint(ability_bp)
    app.register_blueprint(hero_quest_bp)


