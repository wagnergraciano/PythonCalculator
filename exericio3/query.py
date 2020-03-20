from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence
from sqlalchemy import Column, Integer, String, DateTime, Float

conn = create_engine("mysql://root:@localhost/desafio-dev-2020")
Session = sessionmaker(bind=conn)
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

session = Session()
# inserir
c = Empregado(nome='outroTeste', sexo='m', idade= '22', data_criacao= '2020-03-18 14:04:02', salario= '3000')
session.add(c)
session.commit()

# retornar primeiro
firstRegister = session.query(Empregado).first()
print("Primeiro registro: ",firstRegister)

# def retornarTodos():
findAll = session.query(Empregado).all()
empregadoList = []
for employee in findAll:
    empregadoList.append(employee)
print(empregadoList)

# def encontrarPorNome(name):
findAllByName = session.query(Empregado).filter_by(nome='wagner').all()
listEmployee =[]
for findName in findAllByName:
    listEmployee.append(findName)
print(listEmployee)