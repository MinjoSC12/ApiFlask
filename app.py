from flask import Flask
from database import conexion
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from models.modelarea import AreaModel
from models.modelempleado import EmpleadoModel
from controller.areacontroller import AreaController
from controller.areascontroller import AreasController
from controller.empleadocontroller import EmpleadoController
from controller.empleadoscontroller import EmpleadosController
from os import environ
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

api = Api(app=app)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DATABASEURI')
conexion.init_app(app)
Migrate(app, conexion)

api.add_resource(AreaController,'/area','/area/<int:id>')
api.add_resource(AreasController,'/areas')
api.add_resource(EmpleadoController,'/empleado')
api.add_resource(EmpleadosController,'/empleados','/empleados/<string:parametros>')