from main import main
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def calc_r2(df):
    x = df.drop(columns=["price", "make"]) 
    y = df["price"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    r_squared = []
    order = [1, 2, 3, 4]

    for n in order:
        pf = PolynomialFeatures(degree = n)
        lr = LinearRegression()
        x_train_pf = pf.fit_transform(x_train[["horsepower"]])
        x_test_pf = pf.fit_transform(x_test[["horsepower"]])
        lr.fit(x_train_pf, y_train)
        r_squared.append(lr.score(x_test_pf, y_test))
        
    print(r_squared)


if __name__ == "__main__":
    df = main()
    calc_r2(df)