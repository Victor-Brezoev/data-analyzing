from main import main
import matplotlib.pyplot as plt

def scatter_plot(df):
    y = df["price"]
    x = df["engine-size"]
    plt.scatter(x, y)
    plt.title("Scatterplot of Engine Size vs Price")
    plt.xlabel("Engine Size")
    plt.ylabel("Price")

    plt.show()

if __name__ =="__main__":
    df = main()
    scatter_plot(df)