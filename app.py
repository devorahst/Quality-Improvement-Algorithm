from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/RVP')
def RVP():
    return render_template('RVP.html')

@app.route('/BloodCulture')
def BC():
    return render_template('BC.html')

@app.route('/CXR')
def CXR():
    return render_template('CXR.html')

@app.route('/RVPAlgorithm')
def tos():
    workingdir = os.path.abspath(os.getcwd())
    filepath = workingdir + '/static/Files/'
    return send_from_directory(filepath, 'RVPAlgorithmv2.pdf')

if __name__ == '__main__':
    app.run(debug=True)
