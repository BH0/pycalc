import flask
from flask import request
import math 

def replaceForUrl(before, after, string):
    if before in string:
        return string.replace(before, after)
        print(f"s {string}")
    else:
      return string

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['GET'])
def home():
    return f"endpoint: http://whitesmokeremorsefuldeal--five-nine.repl.co/calc/98*9div9+math.ceil(0.2)" 

replacements = {
  "div": "/",
  "dot": "."
} 

@app.route('/calc/<calc_input>', methods=['GET'])
def calc(calc_input):
    code = calc_input 
    str_code = str(code)
    # to handle division, I will simply replace the word div with "/" - ideally the user should be able to simply type "/" - maybe this would be done on the AHK (client end) 
    final_code = str_code
    # for key, value in replacements.items():
    # print (key, value)
    # final_code = replaceForUrl("div", "/", str_code) 
    dot_final_code = replaceForUrl("dot", ".", str_code) 
    div_final_code = replaceForUrl("div", "/", dot_final_code)
    # output = eval(str(2/2)) # eval(final_code)      
    final_code = div_final_code 
    output = eval(final_code) # eval(final_code)      
    return f"output {output}"
    
app.run(host='0.0.0.0', port=8080)
