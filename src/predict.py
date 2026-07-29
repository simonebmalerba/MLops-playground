import joblib
import numpy as np

model = joblib.load("iris_model.pkl")


def predict(features: list) -> str:
    class_names = ["setosa", "versicolor", "virginica"]
    prediction = model.predict(np.array(features).reshape(1, -1))
    return class_names[prediction[0]]
