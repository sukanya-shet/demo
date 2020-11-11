from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query',methods=['GET'])
def question():
    d={}
    d['query'] = request.args['sentence']
    return jsonify(d)


if __name__ == '__main__':
    app.run()
