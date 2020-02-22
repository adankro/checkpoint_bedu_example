from flask import Flask, request
import json

app = Flask(__name__)

lista_hoteles = []


@app.route('/hotel/', methods=['POST', 'GET'])
def hoteles():
    if request.method == 'POST':
        try:
            hotel = dict(json.loads(request.data))
            lista_hoteles.append(hotel)
            return 'Hotel {} agregado correctamente'.format(hotel['nombre'])
        except Exception as e:
            return 'verifique que los parametros son validos:  {}'.format(e)
    else:
        return json.dumps(lista_hoteles)


@app.route('/hotel/<name>', methods=['GET'])
def hoteles_get(name):
    return json.dumps(
        [hotel for hotel in lista_hoteles if hotel['nombre'] == name])


if __name__ == '__main__':
    app.run(debug=True)
