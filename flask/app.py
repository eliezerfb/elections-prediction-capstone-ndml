from flask import Flask
from flask import jsonify
from flask import request


app = Flask('elections-prediction')


@app.route('/sera-eleito', methods=['POST'])
def sera_eleito():
    if request.method == 'POST':
        return jsonify(request.json), 200
    else:
        return request.method


app.run(debug=True, use_reloader=True)
