from flask import Flask,render_template


app=Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    p1=10
    p2=20
    context = {
        'greeting': 'Hello, World!',
        'name': 'Alice'
    }
    return render_template('base.html',p1=p1,p2=p2)

app.run('0.0.0.0',debug=True)