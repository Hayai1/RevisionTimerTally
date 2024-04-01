from flask import Flask
from flask import render_template, url_for, jsonify
import time
app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
    hour = time.localtime(3600)
    return render_template('main.html', time_limit_arg=20, break_time_arg=20)


if __name__ == '__main__':
    app.run(debug=True,)