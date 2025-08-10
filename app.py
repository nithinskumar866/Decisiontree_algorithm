from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model
model_path = os.path.join(os.path.dirname(__file__), 'decision_tree_model.pkl')
model = pickle.load(open(model_path, 'rb'))

@app.route('/', methods=['GET', 'POST'])
def predict_crop():
    if request.method == 'POST':
        try:
            N = float(request.form['N'])
            P = float(request.form['P'])
            K = float(request.form['K'])
            temperature = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])
            rainfall = float(request.form['rainfall'])

            # Prepare input
            input_features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            prediction = model.predict(input_features)

            return render_template('index.html', result=prediction[0])
        except Exception as e:
            return render_template('index.html', result=f"Error: {str(e)}")
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
