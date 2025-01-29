from main import main
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Single linear regression
def slr(df):
    lm = LinearRegression()
    X = df[["highway-mpg"]]
    Y = df["price"]
    lm.fit(X, Y)
    Yhat = lm.predict(X)
    lm.intercept_
    lm.coef_
    # print(Yhat)
    return Yhat

# Multiple linear regression
def mlr(df):
    lm = LinearRegression()
    Z = df[["horsepower", "curb-weight", "engine-size", "highway-mpg"]]
    lm.fit(Z, df["price"])
    yhat = lm.predict(Z)
    lm.intercept_
    lm.coef_
    # print(yhat)
    return yhat


# Polynomial reggresion
def poly(df):
    X = df["highway-mpg"]
    Y = df["price"]
    f = np.polyfit(X, Y, 3)
    p = np.poly1d(f)
    print(p)
    return p

# Polynomial features
def poly_feat(df):
    pr = PolynomialFeatures(degree=2, include_bias=False)
    x_poly = pr.fit_transform(df[["horsepower", "curb-weight"]])
    print(x_poly)

if __name__ == "__main__":
    df = main()
    yhat_slr = slr(df)
    yhat_mlr = mlr(df)
    poly_regr = poly(df)
    poly_features  = poly_feat(df)
    
