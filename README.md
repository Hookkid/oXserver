oXServer is a Python/MongoDB REST Server.
=====================

A simple CORS enabled rest server. Python and mongo are a great match because both speak json natively so there is no need for conversions when interacting with the database.

At this point we are missing the U in CRUD but updates are to be expected.

This is part of a client/server boilerplate. The client side repository is [here](https://github.com/Hookkid/oX "oX").

Requirements:

1. Python 
	- pip
		1. Flask - `sudo pip install Flask`
		2. Flask cors - `pip install -U flask-cors`
		2. PyMongo - `python -m pip install pymongo`
		3. FlaskPymongo - `pip install Flask-PyMongo`

The Stack:

### Client
1. Webpack
	- Lodash
	- Webpack-dev-server 
	- Babel
		1. Babel-loader
		2. Babel-core
		3. Babel-preset-es2015
		4. Babel-preset-react
2. React
	- React-dom
3. Mobx
	- Mobx-react

### Server
1. Python
2. Pymongo
3. Flask
	- Flask-cors
4. MongoDb


### Run the example

```
python sever.py

it will listen to port 5000
```