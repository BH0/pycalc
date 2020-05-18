import flask
from flask import request
import math 

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['GET'])
def home():
    return f"endpoint: http://whitesmokeremorsefuldeal--five-nine.repl.co/calc/98*9div9+math.ceil(0.2)" 

replacements = {
  "div": "/", "dot": "."
} 

@app.route('/calc/<calc_input>', methods=['GET'])
def calc(calc_input):
    code = calc_input 
    str_code = str(code)
    # to handle division, I will simply replace the word div with "/" - ideally the user should be able to simply type "/" - maybe this would be done on the AHK (client end) 
    final_code = str_code
    for key, value in replacements.items():
      if key in final_code:
        final_code = final_code.replace(key, value)

    output = eval(final_code) 
    return f"output {output}"
    
app.run(host='0.0.0.0', port=8080)
