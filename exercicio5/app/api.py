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
    
    def post(self):
        empJson = request.get_json()
        emp = json.loads(empJson)
        # employee = Empregado()
        # employee.nome = emp["nome"]
        # employee.sexo = emp["sexo"]
        # employee.idade = emp["idade"]
        # employee.data_criacao = emp["data_criacao"]
        # employee.salario = emp["salario"]
        # employee.insert(self.session,employee)
        print(emp)
        return jsonify({'sucesso': True})
        # rst = employee.insert(self.session,employee)
        # if rst:
        #     return jsonify({'sucesso': True})
        # else:
        #     return jsonify({'sucesso': False, 'mensagem': 'ocorreu uma falha'}) 

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

    def delete(self, id):
        f = Empregado()
        emp = f.findByID(self.session,id)
        if emp:
            f.delete(self.session,id)
            return jsonify({'sucesso': True})
            # rst = f.delete(self.session,id)
            # if rst:
            #     return jsonify({'sucesso': True})
            # else:
            #     return jsonify({'sucesso': False})
        else:
            return jsonify({'sucesso': False, 'mensagem':id+'nao esta na lista'}) 

api.add_resource(EmpregadoAPI, '/empregado')
api.add_resource(EmpregadoAPIid, '/empregado/<id>')
if __name__ == '__main__':
    app.run(debug=True)