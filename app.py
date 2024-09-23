from flask import Flask, render_template, request
import joblib
import sqlite3

# Load the trained model
model = joblib.load('models/randomforestregression.lb')  # Ensure the path is correct

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/output')
def satisfy():
    return render_template('output.html')

@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        try:
            # Extract and process data from form submission
            try:
                brand = float(request.form.get("brand", 0))
                type = float(request.form.get("type", 0))
                ram = int(request.form.get("ram", 0))
                weight = float(request.form.get("weight", 0))
                touchscreen = int(request.form.get("touchscreen", 0))
                ips = int(request.form.get("ips", 0))
                cpu_brand = float(request.form.get("cpu-brand", 0))
                ssd = int(request.form.get("ssd", 0))
                hdd = int(request.form.get("hdd", 0))
                gpu = float(request.form.get("gpu", 0))
                os = float(request.form.get("os", 0))
                extra_feature = int(request.form.get("extra_feature", 0))  # Add this line
                
            except ValueError as e:
                return f"Invalid input data: {e}"

            # Process the data to match the model's expected feature count
            unseen_data = [[brand, type, ram, weight, touchscreen, ips, cpu_brand, ssd, hdd, gpu, os, extra_feature]]

            # Make prediction
            prediction = "{:.2f}".format(model.predict(unseen_data)[0])

            # Save the prediction and input data to the SQLite database
            conn = sqlite3.connect('predictions_1.db')
            cursor = conn.cursor()

            # Create table if not exists
            cursor.execute('''CREATE TABLE IF NOT EXISTS predictions
                              (brand REAL, type REAL, ram INTEGER, weight REAL, touchscreen INTEGER, 
                              ips INTEGER, cpu_brand REAL, ssd INTEGER, hdd INTEGER, gpu REAL, os REAL, 
                              extra_feature INTEGER, prediction REAL)''')

            # Insert data into the database
            cursor.execute('''INSERT INTO predictions (brand, type, ram, weight, touchscreen, ips, 
                              cpu_brand, ssd, hdd, gpu, os, extra_feature, prediction) 
                              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                         (brand, type, ram, weight, touchscreen, ips, cpu_brand, ssd, hdd, gpu, os, extra_feature, prediction))
            conn.commit()
            conn.close()

            return render_template('output.html', output=prediction)
        except Exception as e:
            return f"An error occurred: {e}"

    return "Invalid request method."

if __name__ == "__main__":
    app.run(debug=True)