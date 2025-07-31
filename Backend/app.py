import os
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd
from flask_cors import CORS

# Trouver le chemin absolu vers le dossier "templates" qui est au-dessus de Backend
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
static_dir = os.path.join(base_dir, 'static')
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
CORS(app)

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

#Colonnes pour faire correspondre les noms anglais et FR.
colonnes = ["Surface_m2", "Nb_Chambres", "Distance_Centre"]

@app.route('/')
def home():
    return render_template('index.html')  # Flask cherche dans template_folder défini ci-dessus

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    m2 = float(data["Surface_m2"])
    chambres = int(data["Nb_Chambres"])
    centre = float(data["Distance_Centre"])

    nouvelle_maison = np.array([[m2, chambres, centre]])
    df = pd.DataFrame(nouvelle_maison, columns=colonnes)
    df_std = scaler.transform(df)
    prediction = model.predict(df_std)

    prix_estime = round(prediction[0][0], 2)
    return jsonify({"prix_estime": prix_estime})

if __name__ == '__main__':
    app.run(debug=True)

