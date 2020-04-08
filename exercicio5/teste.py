
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
        try:
            session.add(employee)
            session.commit()
            return True
        except:
            session.rollback()
            return False
            raise "Erro"
        finally:
            session.close()
    
    def updateName(self,session, id, newName):
        try:
            user = session.query(Empregado).get(id)
            user.nome = newName
            session.commit()
            return True
        except:
            session.rollback()
            return False
            raise "Erro"
        finally:
            session.close()

    def delete(self,session, id):
        try:
            obj = session.query(Empregado).get(id)
            session.delete(obj)
            session.commit()
            return True
        except:
            session.rollback()
            return False
            raise "Erro"
        finally:
            session.close()

    def retrieveAll(self,session):
        try:
            findAll = session.query(Empregado).all()
            empregadoList = []
            for employee in findAll:
                empregadoList.append(employee.dict(employee))
            return empregadoList
        except:
            session.rollback()
            return False
            raise "Erro"
        finally:
            session.close()

    def findByName(self,session, name):
        try:
            findAllByName = session.query(Empregado).filter_by(nome=name).all()
            listEmployee =[]
            for findName in findAllByName:
                listEmployee.append(findName.dict(findName))
            return listEmployee
        except:
            session.rollback()
            return False
            raise "Erro"
        finally:
            session.close()

    def findByID(self,session, id):
        try:
            emp = session.query(Empregado).get(id)
            if emp:
                empDict = emp.dict(emp)
                return empDict 
            else:
                return None
        except:
            session.rollback()
            return False
            raise "Erro"
        finally:
            session.close()

    def findFirst(self,session):
        try:
            firstRegister = session.query(Empregado).first()
            return firstRegister
        except:
            session.rollback()
            return False
            raise "Erro"
        finally:
            session.close()

    
from sqlalchemy import create_engine,update,delete
from sqlalchemy.orm import sessionmaker
conn = create_engine("mysql://root:@localhost/desafio-dev-2020")
Session = sessionmaker(bind=conn)
#instancia uma classe fabrica
session = Session()

c = Empregado(nome='outroTeste', sexo='m', idade= '22', data_criacao= '2020-03-18 14:04:02', salario= '3000')
c1 = Empregado(nome='Teste', sexo='m', idade= '22', data_criacao= '2020-03-18 14:04:02', salario= '3000')
