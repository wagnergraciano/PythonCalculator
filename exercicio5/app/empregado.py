
from sqlalchemy import Column, Integer, String, DateTime, Float, Sequence
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()

class Empregado(Base):
    __tablename__ = 'empregado'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    nome = Column(String(45))
    sexo = Column(String(1))
    idade = Column(Integer)
    data_criacao = Column(DateTime)
    salario = Column(Float)

    def __repr__(self):
        # emp = {'id':self.id, 'nome':self.nome, 'sexo':self.sexo, 'idade':self.idade, 'data_criacao':self.data_criacao , 'salario':self.salario}
        # return emp
        return "id='%s', nome='%s', sexo='%s', idade= '%s', data_criacao= '%s', salario= '%s'" % (self.id, self.nome, self.sexo, self.idade, self.data_criacao ,self.salario)

    def dict(self,c):
        emp = {'id':c.id,'nome':c.nome,'sexo':c.sexo,'idade':c.idade,'data_criacao':c.data_criacao.isoformat(),'salario':c.salario}
        return emp

    def insert(self,session,employee):
        session.add(employee)
        session.commit()
    
    def updateName(self,session, id, newName):
        user = session.query(Empregado).get(id)
        user.nome = newName
        session.commit()

    def delete(self,session, id):
        obj = session.query(Empregado).get(id)
        session.delete(obj)
        session.commit()

    def retrieveAll(self,session):
        findAll = session.query(Empregado).all()
        empregadoList = []
        for employee in findAll:
            empregadoList.append(employee.dict(employee))
        return empregadoList

    def listToDict(self,lst):
        op = { i : lst[i] for i in range(0, len(lst) ) }
        return op

    def findByName(self,session, name):
        findAllByName = session.query(Empregado).filter_by(nome=name).all()
        listEmployee =[]
        for findName in findAllByName:
            listEmployee.append(findName)
        return listEmployee

    def findByID(self,session, id):
        emp = session.query(Empregado).get(id)
        if emp:
            empDict = emp.dict(emp)
            return empDict 
        else:
            return None

    def findFirst(self,session):
        firstRegister = session.query(Empregado).first()
        return firstRegister

    
from sqlalchemy import create_engine,update,delete
from sqlalchemy.orm import sessionmaker
conn = create_engine("mysql://root:@localhost/desafio-dev-2020")
Session = sessionmaker(bind=conn)

session = Session()
c = Empregado(nome='outroTeste', sexo='m', idade= '22', data_criacao= '2020-03-18 14:04:02', salario= '3000')
c1 = Empregado(nome='Teste', sexo='m', idade= '22', data_criacao= '2020-03-18 14:04:02', salario= '3000')

print(c.findByID(session,2))