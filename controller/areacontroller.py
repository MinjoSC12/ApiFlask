from flask_restful import Resource, request
from database import conexion
from models.modelarea import AreaModel
from dtos.areadto import AreasRequest, AreasResponse


class AreaController(Resource):
    def post(self):
        data = request.json
        try:
            dto = AreasRequest()
            dataValidada = dto.load(data)
            nuevaArea = AreaModel(**dataValidada)
            conexion.session.add(nuevaArea)
            conexion.session.commit()

            return {
                'message': 'Área creada con exito'
            }

        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'Error al crear',
                'content': error.args
            }, 201

    def get(self, id):

        try:
            resultado = conexion.session.query(AreaModel).filter_by(id=id).first()
            dto = AreasResponse()
            data = dto.dump(resultado)
            status = 200
            if len(data)==0:
                data = 'Id Erroneo'
                status = 400

            return {
                'content': data
            },status
        except Exception as error:
            return {
                'message': 'Error desconocido',
                'content': error.args
            }
