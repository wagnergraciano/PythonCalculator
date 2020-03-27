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
        f = Empregado()
        rst = f.retrieveAll(self.session)
        rstJson = json.loads(json.dumps(rst))
        return jsonify(rst)

class EmpregadoAPIid(Resource):
    session = Session()
    def get(self,id):
        f = Empregado()
        emp = f.findByID(self.session,id)
        if emp:
            empJson = json.loads(json.dumps(emp))
            return jsonify({'inlist': True},empJson)
        else:
            return jsonify({'inlist': False}) 

    # def delete(self, elemento):
    #     if elemento in lista:
    #         lista.remove(elemento)
    #         return jsonify({'sucesso': True})
    #     else:
    #         return jsonify({'sucesso': False, 'mensagem':elemento+'nao esta na lista'}) 

api.add_resource(EmpregadoAPI, '/empregado')
api.add_resource(EmpregadoAPIid, '/empregado/<id>')
if __name__ == '__main__':
    app.run(debug=True)