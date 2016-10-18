import os
from flask import Flask
from booa.main.views import *

app = Flask(__name__)
app.register_blueprint(main)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

@app.context_processor
def set_static_url():
    return dict(STATIC_URL="/static/")
if __name__ == '__main__':
	app.run()