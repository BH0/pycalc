import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['GET'])
def home():
    return f"endpoint: http://whitesmokeremorsefuldeal--five-nine.repl.co/calc/98*9div9+math.ceil(0.2)" 

@app.route('/calc/<calc_input>', methods=['GET'])
def calc(calc_input):
    code = calc_input 
    str_code = str(code)
    # to handle division, I will simply replace the word div with "/" - ideally the user should be able to simply type "/" - maybe this would be done on the AHK (client end) 
    div = "div"
    if div in str_t:
        final_code = str_code.replace("div", "/")
        print ('word found')
    else:
      final_t = str_code
    output = eval(final_code) 
    return f"output {output}"

app.run(host='0.0.0.0', port=8080)
