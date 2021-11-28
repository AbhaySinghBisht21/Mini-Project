import json
from flask import Flask, jsonify    

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/find/<string:key>")   # enter key through url: /find/key
def find(key):
    result = {}
    with open('temp.json','r') as f:   # file comprehension

        mydict = json.load(f)          # converts .json into dict()

        result = {
                "Found": False,
                "Key": key,
                "Value": None
            }

        if key not in mydict.keys() and key not in mydict['sort'].keys():   # if key in not in main dict() or in nested dict()
            return jsonify(result)

            
        if key in mydict['sort']:    # if key is found in nested dict()
            result = {
                    "Found": True,
                    "Key": key,
                    "value": mydict['sort'].get(key)
                }
        else:
                result = {
            "Found": False,
            "Key": key,
            "Value": None
        }



        if key in mydict.keys():   # if key is found in normal dict()
            
            if key in mydict:
                result = {
                        "Found": True,
                        "Key": key,
                        "value": mydict.get(key)
                    }
            else:
                 result = {
                "Found": False,
                "Key": key,
                "Value": None
            }

    return jsonify(result)      # returns result but first converts dict() into .json
    


if __name__ == '__main__':
    app.run(debug=True)