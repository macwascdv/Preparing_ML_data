import seaborn as sns
import os


SAVE_DIR = os.path.join(os.getcwd(), "Anscombe's_quartet")

def anscombe_data():
    """
    This function loads the Anscombe's quartet from the Seaborn's library resources
    and calculates mean, standard deviation and variance
    Args:
        None

    Returns:
          df - dataframe with Anscombe's x and y values
          description - statistical description of Anscombe's datasets
    """
    #Loading data from seaborn resources
    data = sns.load_dataset('anscombe')

    #Creating data frame with calculated mean and standard deviation
    description = data.groupby('dataset').describe().loc[:,(slice(None),['mean','std'])]

    #Calculating variance and merging both dataframes
    variance = data.groupby('dataset').var()
    variance.rename(columns={'x': '(x, var)', 'y': '(y,var)'}, inplace=True)
    description = description.join(variance).round(2)

    return data, description

def anscombe_chart(data):
    """
    This function creates chart for each dataset
    Args:
        data: pd.DataFrame
    Returns:
         charts: subplot of 4 graphs
    """
    charts = sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=data,
                        col_wrap=2, ci=None, palette="muted", height=4,
                        scatter_kws={"s": 50, "alpha": 1})

    return charts

if __name__ == "__main__":
    try:
        os.mkdir(SAVE_DIR)
    except:
        pass
    data, description = anscombe_data()
    charts = anscombe_chart(data)
    description.to_csv(os.path.join(SAVE_DIR, "Description.csv"))
    charts.savefig(os.path.join(SAVE_DIR, "Charts.jpeg"))
