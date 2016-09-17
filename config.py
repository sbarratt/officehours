import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

GMAPS_API_KEY = "AIzaSyDse4VjdQWla0lAbGl5mc0FBMiKuUel8s0"
