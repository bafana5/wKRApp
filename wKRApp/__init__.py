from flask import Flask
app = Flask(__name__)

# import wKRApp
import wKRApp.views
import wKRApp.models
import wKRApp.config
