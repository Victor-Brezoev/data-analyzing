from main import main
import seaborn as sns
import matplotlib.pyplot as plt

def box_plot():
    drive_wheels_counts = df["drive-wheels"].value_counts()
    sns.boxplot(x= "drive-wheels", y = "price", data = df)
    plt.show()


if __name__=="__main__":
    df = main()
    box_plot()