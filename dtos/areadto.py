from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.modelarea import AreaModel


class AreasRequest(SQLAlchemyAutoSchema):
    class Meta:
        model = AreaModel

class AreasResponse(SQLAlchemyAutoSchema):
    class Meta:
        model = AreaModel