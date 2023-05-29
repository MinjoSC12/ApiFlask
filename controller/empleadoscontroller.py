from flask_restful import Resource, request
from database import conexion
from models.modelempleado import EmpleadoModel
from dtos.empleadodto import EmpleadoResponse

class EmpleadosController(Resource):
    def get(self,parametros=''):

        try:
            iscorreo = parametros.find("@") 
            status = 200
            if parametros == '':
                resultado = conexion.session.query(EmpleadoModel).all()
                dto = EmpleadoResponse(many=True)
                data = dto.dump(resultado)
                return {
                    'content': data
                },status
            elif iscorreo > 0:
                resultado = conexion.session.query(EmpleadoModel).filter_by(email=parametros).first()
                dto = EmpleadoResponse()
                data = dto.dump(resultado)
                if len(data)==0:
                    data = 'no existe ese correo'
                    status = 400
                return {
                    'content': data
                    },status
                
            else:
                resultado = conexion.session.query(EmpleadoModel).filter_by(nombre=parametros).first()
                dto = EmpleadoResponse()
                data = dto.dump(resultado)
                if len(data)==0:
                    data = 'no existe'
                    status = 400
                return {
                    'content': data
                },status
        except Exception as error:
            return {
                'message': 'Error desconocido',
                'content': error.args
            }
