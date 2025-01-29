from main import main
import seaborn as sns
import matplotlib.pyplot as plt

def resid_plot(df):
    sns.residplot(x="highway-mpg", y="price", data = df)
    plt.show()

if __name__ == "__main__":
    df = main()
    resid_plot(df)