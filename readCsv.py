import pandas as pd
import matplotlib.pyplot as plt


def get_df(symbol):
    return pd.read_csv("data/{}.csv".format(symbol))

def get_max_close(symbol):
    """Get max close"""
    return get_df(symbol)["Close"].max()

def get_mean_volume(symbol):
    return get_df(symbol)["Volume"].mean()

def plot_data(symbol):
    get_df(symbol)[["Close", "High"]].plot()
    plt.show()

def test_run():
    for symbol in ["AMZN"]:
        print("sample data")
        print(get_df(symbol).tail(10)[4:10])
        print (symbol, "52 weeks high", get_max_close(symbol))
        print(symbol, "52 weeks mean volume", get_mean_volume(symbol))
        plot_data(symbol)

if __name__ == "__main__":
    test_run()


