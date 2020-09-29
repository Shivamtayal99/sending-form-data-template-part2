from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('index.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        result=request.form.to_dict()
        physics=int(request.form['Physics'])
        chemistery = int(request.form['Chemistry'])
        maths = int(request.form['Mathematics'])
        tot=str(physics+chemistery+maths)
        result['Total']=tot

        return render_template('test.html',result=result)
app.run(debug=True)