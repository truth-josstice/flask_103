from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Related, RelatedList
from models.categories import Category

class CategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        include_fk = True
        load_instance = True
        ordered = True
    competitions = RelatedList(Related(["title", "year"]))

    

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)