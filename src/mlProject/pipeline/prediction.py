import joblib
import numpy as np
import pandas as pd 
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts\model_trainer\model.joblib"))


    def predict(self, data):
        #data = pd.read_json(input_data, orient="records")
        prediction = self.model.predict(data)
        return prediction