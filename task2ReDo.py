from flask import Flask, jsonify, request,abort
from flask_restful import Api, reqparse, Resource

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
    },
    {
        'id': 3,
        'name': '后窗',
        'company': 'SGM',
        'price': 1800
    }
]

p = reqparse.RequestParser()
p.add_argument("myTask")

class operation(Resource):
    def get(self,id):
        try:
            return jsonify(parts[id-1])
        except:
            abort(404)

    def put(self,id):
        try:
            parts[id-1]['name']=request.form['name']
            parts[id-1]['company']=request.form['company']
            parts[id-1]['price']=request.form['price']
            return jsonify(parts[id-1])
        except:
            abort(404)

    def delete(self,id):
        try:
            print(parts[id-1])
            parts.pop(id-1)
            return jsonify({"result":True})
        except:
            abort(404)

class addPart(Resource):
    def post(self):
        if not request.form or 'name' not in request.form:
            abort(404)
        else:
            try:
                part = {
                    "id": len(parts)+1,
                    "name": request.form["name"],
                    "company": request.form["company"],
                    "price": request.form["price"]
                }
                parts.append(part)
                return jsonify(part)
            except:
                abort(404)

class getAllParts(Resource):
    def get(self):
        return jsonify(parts)

api.add_resource(operation,"/api/part/<int:id>")
api.add_resource(addPart,"/api/addPart")
api.add_resource(getAllParts,"/api/getAllParts")

if __name__ == "__main__":
    app.run(host="localhost",port=5000)