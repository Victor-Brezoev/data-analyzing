from main import main
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


def reg_plot(df):
    # Possitive linear relationship
    sns.regplot(x="engine-size", y= "price", data = df)
    plt.ylim(0,)
    plt.show()

    # Negative linear relationship
    sns.regplot(x = "highway-mpg", y="price", data = df)
    plt.ylim(0,)
    plt.show()

    # Weak relationship
    sns.regplot(x="peak-rpm", y= "price", data = df)
    plt.ylim(0,)
    plt.show()


# Pearson Correlation stats
def pearson(df):
    pearson_coef, p_value = stats.pearsonr(df["horsepower"], df["price"])
    if pearson_coef > 0.8:
        print("Large positive relationship")
    elif pearson_coef < -0.8:
        print("Large negative relationship")
    elif pearson_coef == 0:
        print("No relationship")
    else:
        print("Moderate relationship")
    print(f"Pearson coef: {pearson_coef}\nP_value:{p_value}")
        

    
if __name__ =="__main__":
    df = main()
    pearson(df)
    reg_plot(df)
