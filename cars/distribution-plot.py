from main import main
import seaborn as sns
import matplotlib.pyplot as plt
from regression import slr

def dis_plot(df):
    Yhat = slr(df)
    sns.kdeplot(df["price"], color = "r", label="Actual value")
    sns.kdeplot(Yhat, color="b", label = "Fitted values")
    plt.legend()
    plt.show()

if __name__=="__main__":
    df = main()
    dis_plot(df)