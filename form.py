from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to the MongoDB server
client = MongoClient('mongodb://mongodb0.example.com:27017/hr')
db = client['hr']
collection = db['form']

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        image = request.files['image']
        adhar = request.form.get('adhar')
        pan = request.form.get('pan')
        c4 = request.files['c4']
        health_declaration = request.form.get('health-declaration')
        email = request.form.get('email')
        phone = request.form.get('phone')
        bank_details = request.form.get('bank-details')
        
        # Save the form data to the database
        data = {
            'name': name,
            'adhar': adhar,
            'pan': pan,
            'health_declaration': health_declaration,
            'email': email,
            'phone': phone,
            'bank_details': bank_details
        }
        collection.insert_one(data)

        # Return a response to the user
        return "Thanks for submitting the form!"

    # If the request method is GET, show the form
    return render_template('form.html')

if __name__ == '__main__':
    app.run()
