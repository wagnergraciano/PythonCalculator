from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from .empregado import Empregado
import json

# connect to db and creates the session
from sqlalchemy import create_engine,update,delete
from sqlalchemy.orm import sessionmaker

conn = create_engine("mysql://root:@localhost/desafio-dev-2020")
Session = sessionmaker(bind=conn)

app = Flask(__name__)
api = Api(app)

class EmpregadoAPI(Resource):
    session = Session()
    def get(self):
        f = Empregado.retrieveAll()
        return jsonify(f)
    
    def post(self):
        emp = request.get_json()
        transaction_keys = ['nome' , 'sexo', 'idade', 'data_criacao', 'salario']
        if not all (key in emp for key in transaction_keys):
            return jsonify({'sucesso': False, 'mensagem': 'ocorreu uma falha, parametros incompletos'}, 400)
        else:
            Empregado.insert(**emp)
            return jsonify({'sucesso': True})

class EmpregadoAPIid(Resource):
    session = Session()
    def get(self,id):
        emp = Empregado.query().get(id)
        if emp:
            return jsonify({'inlist': True},emp.dict())
        else:
            return jsonify({'inlist': False}) 

    def delete(self, id):
        emp = Empregado.query().get(id)
        if emp:
            emp.delete()
            return jsonify({'sucesso': True})
        return 404
    
    def put(self, id):
        emp = request.get_json()
        e = Empregado.query().get(id)
        if e:
            e.update(**emp)
            return jsonify({'sucesso': True})
        return 404
        # Empregado.update(id,**emp)
        # return jsonify({'sucesso': True})

api.add_resource(EmpregadoAPI, '/empregado')
api.add_resource(EmpregadoAPIid, '/empregado/<id>')
if __name__ == '__main__':
    app.run(debug=True)