from utils.io import load_config
from utils.paths import get_base_path
import pandas as pd
from sklearn.model_selection import train_test_split


def loader():
    config = load_config()

    base_path = get_base_path()

    path = base_path / config["data"]["path"]
    target = config["data"]["target"]
    test_size = config["data"]["test_size"]
    random_state = config["data"]["random_state"]

    df = pd.read_parquet(path)
    X = df.drop(columns=[target])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, stratify=y, random_state=random_state
    )

    return X_train, X_test, y_train, y_test, X, y, df