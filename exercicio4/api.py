from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

lista = [ 'a','b','c']

parser = reqparse.RequestParser()
parser.add_argument('elemento')

class Hello(Resource):
    def get(self):
        nome = request.args.get('nome')
        if(nome):
            return jsonify({'mensagem': 'Ola '+nome+'! Seja bem vindo!'})
        else:
            return jsonify({'mensagem': 'Ola! Como vai?'})

class Lista(Resource):
    def get(self):
        return jsonify({'lista': lista})
    
    def post(self):
        args = parser.parse_args()
        elemento = args['elemento']
        if elemento in lista:
           return jsonify({'sucesso': False, 'mensagem': elemento+'ja esta na lista'}) 
        else:
            lista.append(elemento)
            return jsonify({'sucesso': True})


class ListaID(Resource):
    def get(self,elemento):
        if elemento in lista:
            return jsonify({'inlist': True})
        else:
            return jsonify({'inlist': False}) 
    
    def delete(self, elemento):
        if elemento in lista:
            lista.remove(elemento)
            return jsonify({'sucesso': True})
        else:
            return jsonify({'sucesso': False, 'mensagem':elemento+'nao esta na lista'}) 

api.add_resource(Hello, '/hello')
api.add_resource(Lista, '/lista')
api.add_resource(ListaID, '/lista/<elemento>')
if __name__ == '__main__':
    app.run(debug=True)