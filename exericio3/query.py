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
# estagiario = Empregado(nome= 'wagner', sexo= 'a', idade= '22', data_criacao='2020-03-19 02:19:12', salario= '2000')
# session.add(estagiario)
# session.commit()

firstRegister = session.query(Empregado).first()
findAll = session.query(Empregado).all()
findAllByName = session.query(Empregado).filter_by(nome='teste2').all()
print("Primeiro registro: ",firstRegister)
print("Todos os registros:")
for employee in findAll:
    print(employee,"\n")
print("Buscar todos por nome: \n")
for findName in findAllByName:
    print(findName,"\n")
