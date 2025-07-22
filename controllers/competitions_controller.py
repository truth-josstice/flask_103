from flask import Blueprint, jsonify, request, abort
from main import db
from models.competitions import Competition
from schemas.competitions_schema import competition_schema, competitions_schema
from models.categories import Category
from schemas.categories_schema import category_schema, categories_schema

competitions = Blueprint('competitions', __name__, url_prefix="/competitions")

# Get route
@competitions.route('/')
def get_competitions():
    stmt = db.select(Competition)
    competitions_list = db.session.scalars(stmt)
    result = competitions_schema.dump(competitions_list)
    return jsonify(result)

# Post route
@competitions.route('/', methods=["POST"])
def create_competition():
    competition_fields = request.get_json()
    new_competition = Competition(
        title=competition_fields.get("title"),
        description=competition_fields.get("description"),
        prize=competition_fields.get("prize"),
        year=competition_fields.get("year"),
        category_id=competition_fields.get("category_id")
    )
    db.session.add(new_competition)
    db.session.commit()
    return jsonify(competition_schema.dump(new_competition)), 201

# Delete route
@competitions.route('/<int:id>/', methods=["DELETE"])
def delete_competition(id):
    stmt = db.select(Competition).where(Competition.id == id)
    competition = db.session.scalar(stmt)
    #error:
    if not competition:
        return abort (400, description="Competition doesn't exist")
    db.session.delete(competition)
    db.session.commit()
    return jsonify(competition_schema.dump(competition))

#Get one competition
@competitions.route("/<int:id>/", methods=["GET"])
def get_competition(id):
    stmt = db.select(Competition).filter_by(id=id)
    competition = db.session.scalar(stmt)

    if not competition:
        return abort(400, description= "Competition does not exist")
    
    result = competition_schema.dump(competition)
    return jsonify(result)

# Update route
@competitions.route('/<int:id>', methods=["PUT","PATCH"])
def update_competion(id):
    competition_fields = request.get_json()

    stmt = db.select(Competition).where(Competition.id==id)
    competition = db.session.scalar(stmt)

    if not competition:
        return abort(400, description="Competition does not exist")
    
    competition.title=competition_fields.get("title")
    competition.description=competition_fields.get("description")
    competition.prize=competition_fields.get("prize")
    competition.year=competition_fields.get("year")

    db.session.commit()
    return jsonify(competition_schema.dump(competition))

# search route
@competitions.route("/search", methods=["GET"])
def search_competitions():
    if request.args.get('year'):
        stmt = db.select(Competition).where(Competition.year==request.args.get('year'))
        competitions_list = db.session.scalars(stmt)
    elif request.args.get('title'):
        stmt = db.select(Competition).where(Competition.title==request.args.get('title'))
        competitions_list = db.session.scalars(stmt)
    elif request.args.get('prize'):
        stmt = db.select(Competition).where(Competition.prize==request.args.get('prize'))
        competitions_list = db.session.scalars(stmt)
    
    result = competitions_schema.dump(competitions_list)
    if result != []:
        return jsonify(result)
    else:
        return abort (400, description="No competitions match your search, please try another search")
    
@competitions.route("/categories", methods=["GET"])
def get_categories():
    # get all the categories from the database table
    stmt = db.select(Category)
    categories_list = db.session.scalars(stmt)
    # Convert the categories from the database into a JSON format and store them in result
    result = categories_schema.dump(categories_list)
    # return the data in JSON format
    return jsonify(result)
    