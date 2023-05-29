from flask_restful import Resource,request
from database import conexion
from models.modelarea import AreaModel
from dtos.areadto import AreasRequest

class AreasController(Resource):
    def get(self):
            resultado = conexion.session.query(AreaModel).all()
            dto = AreasRequest(many = True)
            data = dto.dump(resultado)
            
            return {
            'content': data
        }