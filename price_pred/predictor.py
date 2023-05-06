import pickle
from pathlib import Path
import pandas as pd
from sklearn.pipeline import Pipeline


# Load pre-processing pipeline and machine learning model
PIPELINE_FILE = Path('price_pred/predict/pipeG.pkl').resolve()


with open(PIPELINE_FILE, 'rb') as f:
    model = pickle.load(f)



def predict_price(features):
    # Pre-process features using pipeline
    #X = Pipeline.transform(features)

    # Make prediction using machine learning model
    price = model.predict(features)

    return price
