import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def chargerDonner(path):
    return pd.read_csv(path)

def entrainerModele(X, y):
    # Diviser les données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardiser les données
    scaler = StandardScaler()
    X_train_std = scaler.fit_transform(X_train)
    X_test_std = scaler.transform(X_test)

    # Entraîner le modèle
    model = LinearRegression()
    model.fit(X_train_std, y_train)

    # Retourner tout ce qu'il faut
    return model, scaler, X_train_std, X_test_std, y_train, y_test

