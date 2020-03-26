from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from .empregado import Empregado
import json

# connect to db and creates the session
from sqlalchemy import create_engine,update,delete
from sqlalchemy.orm import sessionmaker

conn = create_engine("mysql://root:@localhost/desafio-dev-2020")
Session = sessionmaker(bind=conn)
session = Session()

app = Flask(__name__)
api = Api(app)

# class EmpregadoAPIid(Resource):
#     def get(self,elemento):
#         if elemento in lista:
#             return jsonify({'inlist': True})
#         else:
#             return jsonify({'inlist': False}) 

#     def delete(self, elemento):
#         if elemento in lista:
#             lista.remove(elemento)
#             return jsonify({'sucesso': True})
#         else:
#             return jsonify({'sucesso': False, 'mensagem':elemento+'nao esta na lista'}) 

class EmpregadoAPI(Resource):
    def get(self):
        f = Empregado()
        rst = f.retrieveAll(session)
        rstJson = json.dumps(rst)
        return jsonify(rst)

class EmpregadoAPIid(Resource):
    def get(self,id):
        if session.query(Empregado).get(id):
            return jsonify({'inlist': True})
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