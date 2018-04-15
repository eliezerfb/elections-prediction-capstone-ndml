from flask import Flask
from flask import jsonify
from flask import request

app = Flask('elections-prediction')


@app.route('/sera-eleito', methods=['POST'])
def sera_eleito():
    if request.method == 'POST':
        data = request.json
        return data['nome']
    else:
        return request.method


app.run(debug=True, use_reloader=True)
