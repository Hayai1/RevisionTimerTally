from flask import Flask
from flask import render_template, url_for, jsonify, session, request

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'your secret key'

import webview

@app.route('/save_hours', methods=['POST'])
def save_hours():
    hours_completed = request.form.get('hoursCompleted')
    session['hoursCompleted'] = hours_completed
    return jsonify({'status': 'success'}), 200


@app.route('/start_revision')
def startRevision():
    hours_completed = session.get('hoursCompleted', 0)
    return render_template('main.html', hours_completed_arg=int(hours_completed), time_limit_arg=3600, break_time_arg=600)

@app.route('/')
def index():
    session.pop('hoursCompleted', None)
    return render_template('revision.html')


webview.create_window('Revision App', app)

if __name__ == '__main__':
    #app.run()
    webview.start()