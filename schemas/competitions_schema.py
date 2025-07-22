from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Related
from models.competitions import Competition

class CompetitionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Competition
        ordered = True
        load_instance = True
    category = Related(["title"])
    

competition_schema = CompetitionSchema()
competitions_schema = CompetitionSchema(many=True)