from flask import Flask
from flask_jwt_extended import JWTManager
from views import bp
import certifi
from mongoengine import connect
app = Flask(__name__)
app.register_blueprint(bp)
app.config.from_object("config")
jwt = JWTManager(app)
connect( db='api', username='user_name', password='password', host='host',tlsCAFile=certifi.where())
app.run()


