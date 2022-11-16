from flask import Flask, jsonify, abort, request
import json
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
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

@app.route('/api/parts', methods=['GET'])
def get_tasks():
    return jsonify( parts)
    # return json.dumps(parts,ensure_ascii=False)


@app.route('/api/part/<int:id>', methods=['GET'])
def get_task(id):
    try:
        return jsonify( parts[id-1])
    except IndexError:
        abort(404)


@app.route('/api/part/', methods=['POST'])
def create_task():
    if not request.form or not 'name' in request.form:
        abort(400)
    part = {
        'id': parts[-1]['id'] + 1,
        'name': request.form['name'],
        'company': request.form['company'],
        'price': request.form['price'],
    }
    parts.append(part)
    return jsonify({'part': part}), 201


@app.route('/api/part/<int:id>', methods=['PUT'])
def update_part(id):
    for part in parts:
        if part['id'] == id:
            part["name"] = request.form['name']
            part["company"] = request.form['company']
            part["price"] = request.form['price']
            return jsonify({'part': parts})
    abort(400)


@app.route('/api/part/<int:id>', methods=['DELETE'])
def delete_task(id):
    for part in parts:
        if part['id'] == id:
            parts.remove(part)
            return jsonify({'result': True})
    abort(404)

    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)