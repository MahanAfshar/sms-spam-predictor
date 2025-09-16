from sklearn.preprocessing import FunctionTransformer
import pandas as pd
from utils.helpers import clean_text

def create_preprocessor(X):
    return FunctionTransformer(pd.Series(X).fillna("").astype(str).apply(clean_text), validate=False)