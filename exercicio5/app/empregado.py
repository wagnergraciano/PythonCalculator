
from sqlalchemy import Column, Integer, String, DateTime, Float, Sequence
from sqlalchemy.ext.declarative import declarative_base
import json
from sqlalchemy import create_engine,update,delete
from sqlalchemy.orm import sessionmaker
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
    session = Session()

    def __repr__(self):
        # emp = {'id':self.id, 'nome':self.nome, 'sexo':self.sexo, 'idade':self.idade, 'data_criacao':self.data_criacao , 'salario':self.salario}
        # return emp
        return "id='%s', nome='%s', sexo='%s', idade= '%s', data_criacao= '%s', salario= '%s'" % (self.id, self.nome, self.sexo, self.idade, self.data_criacao ,self.salario)

    def dict(self):
        emp = {'id':self.id,'nome':self.nome,'sexo':self.sexo,'idade':self.idade,'data_criacao':self.data_criacao.isoformat(),'salario':self.salario}
        return emp

    #atributo de classe
    @classmethod
    def query(cls):
        return cls.session.query(cls)

    #métodos precisa de atributo de uma instancia?
    @classmethod
    def insert(cls,**kargs):
        emp = Empregado()
        for key,value in kargs.items():
            if key in ['nome' , 'sexo', 'idade', 'data_criacao', 'salario'] and value:
                setattr(emp,key,value)
        cls.session.add(emp)
        cls.session.commit()
        
    # @classmethod
    # def update(cls,id,**kargs):
    #     user = cls.query.get(id)
    #     for key,value in kargs.items():
    #         if key in ['nome' , 'sexo', 'idade', 'data_criacao', 'salario'] and value:
    #             user[key] = value
    #     cls.session.commit()

    def update(self,**kargs):
        for key,value in kargs.items():
            if key in ['nome' , 'sexo', 'idade', 'data_criacao', 'salario'] and value:
                setattr(self,key,value)
        self.session.commit()
        self.session.close()

    def delete(self):
        self.session.delete(self)
        self.session.commit()

    @classmethod
    def retrieveAll(cls):
        findAll = cls.query().all()
        empregadoList = []
        for employee in findAll:
            empregadoList.append(employee.dict())
        return empregadoList

    def findByName(self,name):
        findAllByName = self.session.query()(Empregado).filter_by(nome=name).all()
        listEmployee =[]
        for findName in findAllByName:
            listEmployee.append(findName.dict())
        return listEmployee


    def findByID(self):
        emp = self.query().get(self.id)
        if emp:
            empDict = emp.dict()
            return empDict 
        else:
            return None

    def findFirst(self):
        firstRegister = self.session.query()(Empregado).first()
        return firstRegister

c = Empregado(nome='outroTeste', sexo='m', idade= '22', data_criacao= '2020-03-18 14:04:02', salario= '3000')
c1 = Empregado(nome='Teste', sexo='m', idade= '22', data_criacao= '2020-03-18 14:04:02', salario= '3000')
