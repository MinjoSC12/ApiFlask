from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.modelempleado import EmpleadoModel

class EmpleadoRequest(SQLAlchemyAutoSchema):
    class Meta:
        model = EmpleadoModel
        include_fk = True

class EmpleadoResponse(SQLAlchemyAutoSchema):
    class Meta:
        model = EmpleadoModel
        include_fk = True