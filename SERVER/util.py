import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    if __data_columns is None or __model is None:
        print("Error: Data columns or model is not loaded.")
        return None

    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    try:
        return round(__model.predict([x])[0], 2)
    except Exception as e:
        print("Error predicting price:", e)
        return None


def load_saved_artifacts():
    global __data_columns
    global __locations
    global __model

    print("Loading saved artifacts...")

    try:
        with open("D:/BHP/server/artifacts/columns (1).json", "r") as f:
            data = json.load(f)
            __data_columns = data.get('data_columns')
            if __data_columns is None:
                raise ValueError("Error: 'data_columns' is None")
            __locations = __data_columns[3:]
    except Exception as e:
        print("Error loading data:", e)
        return

    try:
        with open('D:/BHP/server/artifacts/bangalore_home_prices_model (2).pickle', 'rb') as f:
            __model = pickle.load(f)
            if __model is None:
                raise ValueError("Error: 'model' is None")
    except Exception as e:
        print("Error loading model:", e)
        return

    print("Loading saved artifacts done.")

# Rest of your code remains unchanged

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3,))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location