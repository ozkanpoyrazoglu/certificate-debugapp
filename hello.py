
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask



def get_shell_script_output_using_communicate():
    session = subprocess.Popen(['/bin/sh /flask-project/test.sh'], stdout=PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')

# def get_shell_script_output_using_check_output():
#     stdout = check_output(['./test.sh']).decode('utf-8')
#     return stdout

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello World!"

@app.route('/',methods=['GET',])
def home():
    return '<pre>'+get_shell_script_output_using_communicate()+'</pre>'
app.run(debug=True, host='0.0.0.0')    


