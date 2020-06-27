from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.ext.automap import automap_base
from flask_cors import CORS
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost:3306/hikeplanner'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)

# UNCLEAR if Automap is the way to go
# Base = automap_base()
# Base.prepare(db.engine, reflect=True)
# Food = Base.classes.food

class Food(db.Model):
    __tablename__ = 'food'
    idfood = db.Column('idfood', db.Integer, primary_key=True)
    name = db.Column('name', db.String(45))
    brand = db.Column('brand', db.String(45))
    weight = db.Column('weight', db.Integer)
    calories = db.Column('calories', db.Integer)
    protein = db.Column('protein', db.Integer)
    servings = db.Column('servings', db.Integer)
    cooked = db.Column('cooked', db.Boolean)

    def __init__(self, name, brand, weight, calories, protein, servings, cooked):
        self.name = name
        self.brand = brand
        self.weight = weight
        self.calories = calories
        self.protein = protein
        self.servings = servings
        self.cooked = cooked

class Gear(db.Model):
    __tablename__ = 'gear'
    idgear = db.Column('idgear', db.Integer, primary_key=True)
    name = db.Column('name', db.String(45))
    brand = db.Column('brand', db.String(45))
    weight = db.Column('weight', db.Integer)
    gear_type = db.Column('gear_type_type', db.String(45))

    def __init__(self, name, brand, weight, gear_type):
        self.name = name
        self.brand = brand
        self.weight = weight
        self.gear_type = gear_type


@app.route('/food')
def food():
    foods = [{'idfood':food.idfood, 'name': food.name, 'brand': food.brand, 'weight': food.weight,
            'calories': food.calories, 'protein': food.protein, 'servings': food.servings,
            'cooked': int(food.cooked)} for food in db.session.query(Food).all()]
    return jsonify(foods)

@app.route('/food_insert', methods=['POST'])
def food_insert():
    new_row = request.get_json()
    food = Food(name=new_row['name'], brand=new_row['brand'], weight=int(new_row['weight']), calories=int(new_row['calories']), protein=int(new_row['protein']), servings=int(new_row['servings']), cooked=int(new_row['cooked']))
    db.session.add(food)
    db.session.commit()
    return 'Data Saved'

@app.route('/food_delete', methods=['POST'])
def food_delete():
    target_row = request.get_json()
    target = Food.query.filter_by(idfood=target_row['idfood']).first()
    db.session.delete(target)
    db.session.commit()
    return f'Food {target_row} deleted'

@app.route('/food_update', methods=['POST'])
def food_update():
    updated_row = request.get_json()
    target_row = Food.query.filter_by(idfood=updated_row['idfood']).update({Food.name: updated_row['name'], Food.brand: updated_row['brand'], Food.weight: int(updated_row['weight']), Food.calories: int(updated_row['calories']), Food.protein: int(updated_row['protein']), Food.servings: int(updated_row['servings']), Food.cooked: int(updated_row['cooked'])})
    db.session.commit()
    return f'Food {updated_row} updated'

@app.route('/gear')
def gear():
    gears = [{'idgear':gear.idgear, 'name': gear.name, 'brand': gear.brand, 'weight': gear.weight,'gear_type_type': gear.gear_type} for gear in db.session.query(Gear).all()]
    return jsonify(gears)

# @app.route('/gear_insert', methods=['POST'])
# def gear_insert():
#     new_row = request.get_json()
#     food = Food(name=new_row['name'], brand=new_row['brand'], weight=int(new_row['weight']), calories=int(new_row['calories']), protein=int(new_row['protein']), servings=int(new_row['servings']), cooked=int(new_row['cooked']))
#     db.session.add(food)
#     db.session.commit()
#     return 'Data Saved'

# @app.route('/gear_delete', methods=['POST'])
# def gear_delete():
#     target_row = request.get_json()
#     target = Food.query.filter_by(idfood=target_row['idfood']).first()
#     db.session.delete(target)
#     db.session.commit()
#     return f'Food {target_row} deleted'

# @app.route('/gear_update', methods=['POST'])
# def gear_update():
#     updated_row = request.get_json()
#     target_row = Food.query.filter_by(idfood=updated_row['idfood']).update({Food.name: updated_row['name'], Food.brand: updated_row['brand'], Food.weight: int(updated_row['weight']), Food.calories: int(updated_row['calories']), Food.protein: int(updated_row['protein']), Food.servings: int(updated_row['servings']), Food.cooked: int(updated_row['cooked'])})
#     db.session.commit()
#     return f'Food {updated_row} updated'