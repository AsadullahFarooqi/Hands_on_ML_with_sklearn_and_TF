import pandas as pd
import os

def load_housing_data(housing_path="housing_data"):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data()
housing.head()

# housing.info()
