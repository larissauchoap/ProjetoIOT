from app import db
from flask import jsonify

class paciente(db.Model):
    __tablename__ = 'Cadastro_paciente'

    cpf = db.Column(db.String, primary_key=True)
    nome = db.Column(db.String(80))
    data_nascimento = db.Column(db.String(11))
    sexo = db.Column(db.String(9))
    idade=db.Column(db.String)
    telefone=db.Column(db.Integer)
    endereço=db.Column(db.String(8))
    classificacao=db.Column(db.String(8))
    hora_chegada=db.Column(db.String(8))
    unidade=db.Column(db.String)

    def __init__(self, cpf, nome, data_nascimento,sexo,idade,telefone,endereço, classificacao, hora_chegada,unidade):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento =  data_nascimento
        self.sexo= sexo
        self.idade= idade
        self.telefone=telefone
        self.endereço=endereço
        self.classificacao=classificacao
        self.hora_chegada=hora_chegada
        self.unidade=unidade
       

    def json(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'data_nascimento': self.data_nascimento,
            'sexo': self.sexo,
            'idade':self.idade,
            'telefone':self.telefone,
            'endereço': self.endereço,
            'classificacao': self.classificacao,    
            'hora_chegada': self.hora_chegada, 
            'unidade':self.unidade,           
        }

    def save_paciente(self):
        try:
            db.session.add(self) 
            db.session.commit() 
        except Exception as e: 
            print(e)

    def delete_paciente(self):
        try:
            db.session.delete(self)  # Remove o objeto paciente do banco de dados
            db.session.commit()  # Confirma a operação de exclusão
        except Exception as e:
            db.session.rollback()  # Reverte a transação em caso de erro
            raise e  # Lança a exceção para tratamento externo
