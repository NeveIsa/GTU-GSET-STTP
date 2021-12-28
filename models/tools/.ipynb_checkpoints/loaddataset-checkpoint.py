import pandas as pd
from sklearn.model_selection import train_test_split as tts

def load(csvpath="../../dataset/coins.csv", test_size=0.1):
    data = pd.read_csv(csvpath)
    # print(data)

    X = data[["reflectance","weight"]]
    y = data.denomination

    
    X_train, X_test, y_train, y_test = tts(X,y, test_size=test_size, random_state=71)
    
    return X_train, X_test, y_train, y_test





if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load()
    
