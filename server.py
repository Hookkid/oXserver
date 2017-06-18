from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
from bson import Binary, Code
from bson.json_util import dumps
from bson.json_util import loads

app = Flask(__name__)
CORS(app)

app.config['MONGO_DBNAME'] = 'Cluster0'
app.config['MONGO_URI'] = 'mongodb://XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def get_all_stars():
  star = mongo.db.stars
  output = []
  for s in star.find():
    output.append({'key': dumps(s['_id']), 'name' : s['name'], 'distance' : s['distance']})
  return jsonify({'result' : output})

@app.route('/<name>', methods=['GET'])
def get_one_star(name):
  star = mongo.db.stars
  s = star.find_one({'name' : name})
  if s:
    output = {'name' : s['_id'], 'distance' : s['distance']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/', methods=['POST'])
def add_star():
  star = mongo.db.stars  
  name = request.json['name']
  distance = request.json['distance']
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'key': dumps(star_id), 'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

@app.route('/delete', methods=['POST'])
def del_star():
  star = mongo.db.stars  
  key = request.json
  star.remove(loads(key))
  output = {'key': key}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True)
