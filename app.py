from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        form_data = [float(x) for x in request.form.values()]
        # Convert to numpy array
        features = np.array(form_data).reshape(1, -1)
        # Predict using the model
        prediction = model.predict(features)
        output = 'Malignant' if prediction[0] == 1 else 'Benign'
        return render_template('result.html', prediction_text=f'The predicted diagnosis is: {output}')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
