from flask import Flask, render_template, jsonify, request
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.query import Query
from appwrite.id import ID
from flask_cors import CORS

client = Client()
client.set_endpoint('https://cloud.appwrite.io/v1')
client.set_project('66bbf9cf001d10a8ec84')
client.set_key(
    '55b09cb74b6c6e4dd53c9370b17601c8902257caaaec483162bd185dcc2aca5b256069a1c664af6c5691563c8cd540bdd046b98c6e9746479846d6d27e8476af715d4ff0645d5b8bded87c5b07144fbb722cec3962a722216484ae34a73dd0de9f485233a7596ad2ae84af30dca0e58a2a7046a353c4f6b2c52649ed41c7806c'
)

app = Flask(__name__)
CORS(app)
page_size = 35
collection_id = '66c53bf1002bfac9ff5a'  # Collection
database_id = '66bbfa8d000a16056dd1'  # db questionary
databases = Databases(client)


@app.route("/")
def indexito():
    nombre = "Juan"
    return render_template("index.html", nombre=nombre)

@app.route("/inicio")
def graph():
    nombre = "inicio"
    return render_template("inicio.html", nombre=nombre)

# @app.route("/graph")
# def graph():
#     nombre = "datos"
#     return render_template("graph.html", nombre=nombre)


@app.route("/datos")
def datosdeuser():
    nombre = "datosdeuser"
    return render_template("datos.html", nombre=nombre)


@app.route("/individual")
def individual():
    nombre = "individual"
    return render_template("individual.html", nombre=nombre)


@app.route('/info')
def getinfo():
    page = int(request.args.get("page", 1))
    skip = (page - 1) * page_size
    limit = page_size
    print(skip, limit)
    documents = databases.list_documents(
                                database_id=database_id,
                                collection_id=collection_id,
                                queries=[Query.limit(limit), Query.offset(skip)]
                                    )
    return jsonify(documents['documents'])


@app.route('/add', methods=['GET', 'POST'])
def create():
    data = {
        'name': request.form['name'],
        'document': request.form['document'],
        'age': request.form['age'],
        'service': request.form['service'],
        'identificacion': request.form['identificacion'],
        'pq': request.form['pq'],
        'rp': request.form['rp'],
        'es': request.form['es'],
        'as': request.form['as'],
        'ge': request.form['ge'],
        'sx': request.form['sx'],
        'qpr': request.form['qpr'],
        'fp': request.form['fp'],
        'comment': request.form['comment']
    }
    if request.method == 'POST':
        databases.create_document(database_id=database_id,
                                  collection_id=collection_id,
                                  document_id=ID.unique(),
                                  data=data)
        return render_template('agradecimientos.html')
        # return jsonify(data)
    else:
        return "No se ha recibido ningún dato"


if __name__ == '__main__':
    app.run(port=5000)

