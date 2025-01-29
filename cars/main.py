import pandas as pd

def load_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

    df = pd.read_csv(url, na_values="?")

    headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]
    
    if len(df.columns) == len(headers):
        df.columns = headers
    else:
        raise ValueError("Headers lenght do not match columns lenght")
    return df
    
# Checking price for Nan values
# df = load_data()
# print(df.isnull().sum())

def clear_data(df):
    # Delete nan rows in price
    df.dropna(subset = ["price"], axis=0, inplace = True)
    # Change nan values
    df.fillna({
        'num-of-doors': df['num-of-doors'].mode()[0],
        "bore":df["bore"].mean(),
        "stroke":df["stroke"].mean(),
        "horsepower":df["horsepower"].mean(),
        "peak-rpm":df["peak-rpm"].mean(),
        "num-of-cylinders":df["num-of-cylinders"].mode()[0]
    }, inplace=True)
    # Fill normalized-losses by make's mean
    df["normalized-losses"] = df.groupby("make")["normalized-losses"].transform(lambda x:x.fillna(x.mean()))
    df.fillna({"normalized-losses":df["normalized-losses"].mean()}, inplace=True)
    
    return df

def norm_data(df):
    df = df.astype({
        "normalized-losses": int, 
        "bore": float, 
        "stroke": float, 
        "horsepower": int, 
        "peak-rpm": int, 
        "price": int
    })
    # Normalizing the numerical data
    normalize = [
    "normalized-losses", "length",  
    "height","curb-weight",
    "engine-size","bore",
    "stroke", "compression-ratio", 
    "horsepower", "peak-rpm", 
    "city-mpg", "highway-mpg", 
    "price","width"
    ]
    df[normalize] = df[normalize].apply(lambda x:(x - x.min()) / (x.max() - x.min()))

    return df

def dummy(df):
    df = pd.get_dummies(df, columns=["fuel-type", "aspiration", "num-of-doors", "num-of-cylinders", "engine-type","fuel-system", "engine-location"], dtype=int)
    return df

def main():
    df = load_data() 
    df = clear_data(df)
    df = norm_data(df)
    df = dummy(df)
    file_path = r"D:\cars\cars.csv"
    
    df.to_csv(file_path)    

    return df


if __name__=="__main__": 
    df = main()
    
    # pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    print(df)
