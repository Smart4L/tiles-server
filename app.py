import flask
from flask import Response, send_file
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/tile/<zoom>/<x>/<y>.png')
def get_img(zoom = None, x = None, y = None):
    if(os.path.isfile(f'tiles/{zoom}-{x}-{y}.png')):
        return send_file(f'tiles/{zoom}-{x}-{y}.png', mimetype='image/png')
        with open(f'tiles/{zoom}-{x}-{y}.png', 'r') as handler:
            return(handler)
    else:
        return send_file(f'tiles/{0}-{0}-{0}.png', mimetype='image/png')

app.run(host="0.0.0.0")