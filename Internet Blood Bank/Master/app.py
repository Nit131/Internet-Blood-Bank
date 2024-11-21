from flask import Flask, render_template, request, jsonify
import pandas as pd
from data_processor import filter_data

app = Flask(__name__)

@app.route('/')
def index():
    # Read all data and pass to the template
    data = filter_data()  # Get all data by default
    return render_template('main.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    city = request.form.get('city')
    blood_group = request.form.get('blood_group')
    age = request.form.get('age')
    gender = request.form.get('gender')

    # Filter the data based on the user's input
    filtered_data = filter_data(city=city, blood_group=blood_group, age=age, gender=gender)

    # Return filtered data as JSON to be handled by the frontend
    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(debug=True)
