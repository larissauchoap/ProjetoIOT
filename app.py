from app import app
from app.resources.cadastro_resources import PacientesCreate, PacientesSearch, PacientesDelete, PacientesUpdate
if __name__ == '__main__':  # executar a aplicação flask
    app.run(host='127.0.0.1', debug = True, port = 5000)