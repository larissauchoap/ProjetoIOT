from flask import jsonify, request
from flask_restful import Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from app import db
import json

from app.models.Cadastro_paciente import paciente

class Index(Resource):
    def get(self): # vai mostrar a mensagem abaixo
        return jsonify({"message": "Informacao dos pacientes"})

    
#Definir os argumentos
argumentos = reqparse.RequestParser()
argumentos.add_argument('cpf', type=int)
argumentos.add_argument('nome', type=str)
argumentos.add_argument('data_nascimento', type=str)
argumentos.add_argument('sexo', type=str)
argumentos.add_argument('idade', type=str)
argumentos.add_argument('telefone',type=str)
argumentos.add_argument('endereço',type=str)

class PacientesCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            user = paciente(**datas)
            user.save_paciente()

            return {"message": 'Paciente inserido com sucesso!'}, 201

        except Exception as error:
            return {'error': str(error)}, 500
        

class PacientesSearch(Resource):
    def get(self, cpf=None):
        if cpf is None:
            return self.get_all()
        else:
            return self.get_by_cpf(cpf)

    def get_all(self):
        try:
            # Obtenha todos os pacientes
            pacientes = paciente.query.all()
            Cadastro_pacientes = [p.json() for p in pacientes]
            return {'cadastro_paciente': Cadastro_pacientes}
        except Exception as e:
            return {'status': 500, 'msg': str(e)}, 500

    def get_by_cpf(self, cpf):
        try:
            # Busque o paciente pelo CPF
            paciente_encontrado = paciente.query.filter_by(cpf=cpf).first()

            if paciente_encontrado:
                return paciente_encontrado.json(), 200
            else:
                return {"message": "Paciente não encontrado"}, 404
        except Exception as e:
            return {"error": str(e)}, 500


class PacientesDelete(Resource):
    def delete(self, cpf):
        try:
            # Procurar o paciente pelo CPF
            paciente_a_deletar = paciente.query.get(cpf)

            if paciente_a_deletar is not None:
                # Deletar o paciente do banco de dados
                paciente_a_deletar.delete_paciente()
                return {"message": 'Paciente deletado com sucesso!'}, 200
            else:
                return {"message": 'Paciente não encontrado'}, 404

        except Exception as error:
            return {'error': str(error)}, 500

class PacientesUpdate(Resource):
    def put(self, cpf):
        try:
            paciente_a_atualizar = paciente.query.get(cpf)

            if paciente_a_atualizar is not None:
                dados_atualizados = reqparse.RequestParser()
                dados_atualizados.add_argument('nome', type=str)
                dados_atualizados.add_argument('data_nascimento', type=str)
                dados_atualizados.add_argument('sexo', type=str)
                dados_atualizados.add_argument('telefone', type=int)
                dados_atualizados.add_argument('endereço', type=str)

                novos_dados = dados_atualizados.parse_args()

                # Atualize apenas os campos fornecidos na solicitação
                if 'nome' in novos_dados:
                    paciente_a_atualizar.nome = novos_dados['nome']
                if 'data_nascimento' in novos_dados:
                    paciente_a_atualizar.data_nascimento = novos_dados['data_nascimento']
                if 'sexo' in novos_dados:
                    paciente_a_atualizar.sexo = novos_dados['sexo']
                if 'telefone' in novos_dados:
                    paciente_a_atualizar.telefone = novos_dados['telefone']
                if 'endereço' in novos_dados:
                    paciente_a_atualizar.endereço = novos_dados['endereço']

                # Salve as alterações no banco de dados
                paciente_a_atualizar.save_paciente()

                return {"message": 'Paciente atualizado com sucesso!'}, 200
            else:
                return {"message": 'Paciente não encontrado'}, 404

        except Exception as error:
            return {'error': str(error)}, 500

class PacientesUpdate(Resource):
    def put(self, cpf):
        try:
            paciente_a_atualizar = paciente.query.get(cpf)

            if paciente_a_atualizar is not None:
                dados_atualizados = argumentos.parse_args()

                # Atualize apenas os campos fornecidos na solicitação PUT
                if dados_atualizados['nome'] is not None:
                    paciente_a_atualizar.nome = dados_atualizados['nome']
                if dados_atualizados['data_nascimento'] is not None:
                    paciente_a_atualizar.data_nascimento = dados_atualizados['data_nascimento']
                if dados_atualizados['sexo'] is not None:
                    paciente_a_atualizar.sexo = dados_atualizados['sexo']
                if dados_atualizados['idade'] is not None:
                    paciente_a_atualizar.idade = dados_atualizados['idade']
                if dados_atualizados['telefone'] is not None:
                    paciente_a_atualizar.telefone = dados_atualizados['telefone']
                if dados_atualizados['endereço'] is not None:
                    paciente_a_atualizar.endereço = dados_atualizados['endereço']

                db.session.commit()  # Salve as alterações no banco de dados

                return {"message": 'Paciente atualizado com sucesso!'}, 200
            else:
                return {"message": 'Paciente não encontrado'}, 404

        except Exception as error:
            return {'error': str(error)}, 500
