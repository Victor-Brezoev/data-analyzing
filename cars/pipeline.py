from main import main
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline


def buid_pipe(df):
    steps = [
        ("polinomial", PolynomialFeatures(degree=2)), 
        ("scale", StandardScaler()), 
        ("Model", LinearRegression())
    ]
    pipe = Pipeline(steps)
    pipe.fit(df[["horsepower", "curb-weight", "engine-size", "highway-mpg"]], df["price"])
    yhat = pipe.predict(df[["horsepower", "curb-weight", "engine-size", "highway-mpg"]])
    
    return yhat


if __name__ == "__main__":
    df = main()
    buid_pipe(df)
    yhat = buid_pipe(df)