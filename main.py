from flask import Flask, request
import json
import csv
app = Flask(__name__)

@app.route('/get/data', methods=['POST'])
def get_data():
    if request.method == 'POST':
        data_form = request.form
        a = data_form.get('a')
        b = data_form.get('b')
        return {'a': a, 'b': b}
    return 'Invalid request'

        

if __name__ == "__main__":
    app.run(port=5000, debug=True)
