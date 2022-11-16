from flask import Flask, jsonify, abort, request
from flask_restful import reqparse, Api, Resource

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app)
parts = [
    {
        'id': 1,
        'name': '前灯总成',
        'company': 'abc',
        'price': 1800
    },
    {
        'id': 2,
        'name': '轮胎',
        'company': 'horse',
        'price': 850
    }
]

parser = reqparse.RequestParser()
parser.add_argument('task')


class Todo(Resource):
    def get(self, id):
        for part in parts:
            if part['id'] == id:
                return jsonify({'part': part})
        abort(404)

    def delete(self, id):
        for part in parts:
            if part['id'] == id:
                parts.remove(part)
                return jsonify({'result': True})
        abort(404)

    def put(self, id):
        for part in parts:
            if part['id'] == id:
                part["name"] = request.form['name']
                part["company"] = request.form['company']
                part["price"] = request.form['price']
                return jsonify({'part': parts})
        abort(400)


class AddPart(Resource):
    def post(self):
        if not request.form or not 'name' in request.form:
            abort(400)
        part = {
            'id': parts[-1]['id'] + 1,
            'name': request.form['name'],
            'company': request.form['company'],
            'price': request.form['price'],
        }
        parts.append(part)
        return jsonify({'part': part})


class getParts(Resource):
    def get(self):
        return jsonify({'parts': parts})


api.add_resource(getParts, '/api/parts')
api.add_resource(Todo, '/api/part/<int:id>')
api.add_resource(AddPart, '/api/part')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)