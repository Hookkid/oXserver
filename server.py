from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
from bson import Binary, Code
from bson.json_util import dumps
from bson.json_util import loads
import env #Create your own env.py with your mongodb credencials

app = Flask(__name__)
CORS(app)

app.config['MONGO_DBNAME'] = env.mongoDbName
app.config['MONGO_URI'] =  env.MongoUri
mongo = PyMongo(app)

@app.route('/get/<collection_name>', methods=['GET'])
def get_all_records(collection_name):
  result = mongo.db[collection_name]
  output = []
  for s in result.find():
    print(s.keys())
    output.append({'key': dumps(s['_id']),'name': dumps(s['_id'])})

  return jsonify({'result' :output})

@app.route('/key/<name>', methods=['GET'])
def get_one_record(name):
  result = mongo.db.stars
  s = result.find_one(loads(name))
  if s:
    output = {'key': name, 'name' : s['name'], 'distance' : s['distance']}
  else:
    output = "No such name"
  return jsonify({'result' : output})

@app.route('/', methods=['POST'])
def add_record():
  result = mongo.db.stars  
  name = request.json['name']
  distance = request.json['distance']
  star_id = result.insert({'name': name, 'distance': distance})
  new_star = result.find_one({'_id': star_id })
  output = {'key': dumps(star_id), 'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

@app.route('/update/', methods=['POST'])
def update_record():
  result = mongo.db.stars  
  key = request.json['key']
  name = request.json['name']
  distance = request.json['distance']
  result.replace_one( {'_id': loads(key)} , {'name': name, 'distance': distance})
  output = {'key': key}
  return jsonify({'result' : output})

@app.route('/delete', methods=['POST'])
def del_record():
  result = mongo.db.stars  
  key = request.json
  result.remove(loads(key))
  output = {'key': key}
  return jsonify({'result' : output})

  ## RETRIEVEING LIST OF DBS
@app.route('/util/dbs', methods=['GET'])
def get_all_dbs():
  response = mongo.db.collection_names()
  output = []
  for s in response:
    output.append({'key': s,'name': s})
  return jsonify({'result' : output})


if __name__ == '__main__':
    app.run(debug=True)