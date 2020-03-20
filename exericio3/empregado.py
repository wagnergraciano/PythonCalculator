
from sqlalchemy import Column, Integer, String, DateTime, Float, Sequence
from sqlalchemy.ext.declarative import declarative_base

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
        return "Empregado(id='%s', nome='%s', sexo='%s', idade= '%s', data_criacao= '%s', salario= '%s')" % (self.id, self.nome, self.sexo, self.idade, self.data_criacao ,self.salario)

from sqlalchemy import create_engine,update,delete
from sqlalchemy.orm import sessionmaker
conn = create_engine("mysql://root:@localhost/desafio-dev-2020")
Session = sessionmaker(bind=conn)

session = Session()
c = Empregado(nome='outroTeste', sexo='m', idade= '22', data_criacao= '2020-03-18 14:04:02', salario= '3000')
c1 = Empregado(nome='Teste', sexo='m', idade= '22', data_criacao= '2020-03-18 14:04:02', salario= '3000')

def insert(employee):
    session.add(employee)
    session.commit()

def delete(id):
    obj = session.query(Empregado).get(id)
    session.delete(obj)
    session.commit()

insert(c1)
def findFirst():
    firstRegister = session.query(Empregado).first()
    return firstRegister

def retrieveAll():
    findAll = session.query(Empregado).all()
    empregadoList = []
    for employee in findAll:
        empregadoList.append(employee)
    return empregadoList

def findByName(name):
    findAllByName = session.query(Empregado).filter_by(nome=name).all()
    listEmployee =[]
    for findName in findAllByName:
        listEmployee.append(findName)
    return listEmployee

def findByID(id):
    return session.query(Empregado).get(id)