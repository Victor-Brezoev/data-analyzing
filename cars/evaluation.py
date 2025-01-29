from main import main
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from pipeline import buid_pipe

lm = LinearRegression()

# Mean squared error
def mse(df):
    yhat = buid_pipe(df)
    actual_value = df["price"]
    predicted_value = yhat
    mse = mean_squared_error(actual_value, predicted_value)
    print(f"Mean Squared Error: {mse}")

# R squared value
def r_squared(df):
    x = df[["highway-mpg"]]
    y = df["price"]
    lm.fit(x, y)
    r2 = lm.score(x, y)
    print(f"Coefficient of Determination is {r2}")


if __name__ == "__main__":
    df = main()
    mse(df)
    r_squared(df)