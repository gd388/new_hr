from flask import Flask,render_template,request,redirect, url_for

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/hr"
# db = SQLAlchemy(app)

# class Form(db.Model):
#     SN = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(20),unique = False, nullable=False)
#     password = db.Column(db.String(20), nullable = False)
    
# class Form(db.Model):
#     SN = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(20),nullable=False)
#     name = db.Column(db.String(10), unique=False, nullable=False)


# @app.route('/', methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form.get['email']
#         password = request.form.get['password']

#         entry = Form(email = email, password = password)
#         db.session.add(entry)
#         db.session.commit()

    # Here you would typically check the username and password against a database or some other authentication mechanism
    # For this example, we'll just assume the username and password are correct
    # if username == 'admin' and password == '1234':
    #     return redirect(url_for('success'))
    # else:
    #     return redirect(url_for('Incorrect Credentials'))
    # return redirect(url_for('success'))



@app.route('/')
def success():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')



if __name__ == '__main__':
    app.run(debug=True)
