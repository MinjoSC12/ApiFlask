from flask_restful import Resource, request
from database import conexion
from models.modelempleado import EmpleadoModel
from dtos.empleadodto import EmpleadoRequest

class EmpleadoController(Resource):
    def post(self):
        data = request.json
        try:
            dto = EmpleadoRequest()
            dataValidada = dto.load(data)
            nuevoempleado = EmpleadoModel(**dataValidada)
            conexion.session.add(nuevoempleado)
            conexion.session.commit()

            return {
                'message': 'Empleado creado con exito'
            },201

        except Exception as error:
            conexion.session.rollback()
            return {
                'message': 'error al crear',
                'content': error.args
            }, 400