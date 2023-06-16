from flask import Flask,jsonify
from data.json_prog import read

app=Flask(__name__) 

@app.route('/api/printHello')
def hello_world():
    data={'value':'Hello World'}
    return jsonify(data)

@app.route('/api/modifiedRecepie')
def modifiedRecepie():
    data=read()
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True,port=8000)