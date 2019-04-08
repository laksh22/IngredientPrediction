# Import libraries
import pandas as pd  # Data manipulation
import numpy as np  # Array and Matrix operations
from sklearn.externals import joblib  # To import custom models
cv = joblib.load('cuisine_count_vectorizer.pkl')
logistic = joblib.load('cuisine_logistic_model.pkl')
enc = joblib.load('cuisine_label_encoder.pkl')


def predict_cuisine(ingredients):
    ingredients = pd.Series(ingredients)
    X_test = cv.transform(ingredients.values)
    result = logistic.predict(X_test)
    result = enc.inverse_transform(result)
    return(result)
# Input example: ["Spaghetti; Cheese"]
