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

<<<<<<< HEAD
app.config['MONGO_DBNAME'] = env.mongoDbName
app.config['MONGO_URI'] =  env.MongoUri
=======
app.config['MONGO_DBNAME'] = 'Cluster0'
app.config['MONGO_URI'] = 'mongodb://XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

>>>>>>> ac7199e6a640c2d9556deab847bd8fb928396e6c
mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def get_all_records():
  result = mongo.db.stars
  output = []
  for s in result.find():
    output.append({'key': dumps(s['_id']), 'name' : s['name'], 'distance' : s['distance']})
  return jsonify({'result' : output})

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
@app.route('/dbs', methods=['GET'])
def get_all_dbs():
  databases = mongo.db.collection_names()
  return jsonify({'result' : databases})



if __name__ == '__main__':
    app.run(debug=True)
