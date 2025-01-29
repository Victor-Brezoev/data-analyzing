from main import main
import pandas as pd
import matplotlib.pyplot as plt

# Utilizing Heatmap
def hmap_plot():
    df_group = df.groupby(["drive-wheels", "body-style"], as_index=False)["price"].agg("mean")
    df_pivot = df_group.pivot(index="drive-wheels", columns="body-style")
    print(df_pivot)

    plt.xlabel("Body Style") 
    plt.ylabel("Drive Wheels")
    plt.pcolor(df_pivot, cmap="RdBu")
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    df = main()
    hmap_plot()