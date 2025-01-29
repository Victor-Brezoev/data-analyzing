from main import main
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Create train_test model
def train_test(df):
    x = df.drop(columns=["price", "make","drive-wheels","body-style"]) 
    y = df["price"]
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

    lm = LinearRegression()
    lm.fit(x_train, y_train)
    y_pred = lm.predict(x_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    
    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")
    print(f"Training data (x_train): {x_train.shape}")
    print(f"Testing data (x_test): {x_test.shape}")
    return x_train, x_test, y_train, y_test


def cross_val(df):
    lr = LinearRegression()
    x_data = df.drop(columns=["price", "make","drive-wheels","body-style"]) 
    y_data = df["price"]
    scores = cross_val_score(lr, x_data, y_data, cv=3)
    np.mean(scores)
    yhat = cross_val_predict(lr, x_data, y_data, cv=3)
    print(scores)
    print(yhat)

if __name__ == "__main__":
    df = main()
    train_test(df)
    cross_val(df)
