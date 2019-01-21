import pandas as pd 

def get_df(symbol):
    return pd.read_csv(
        "data/{}.csv".format(symbol), 
        index_col="Date", 
        parse_dates=True,
        usecols=["Date","Adj Close"],
        na_values=["nan"])


def test_run():
    start_date="2018-01-22"
    end_date="2019-01-18"
    dates=pd.date_range(start_date, end_date)
    
    df1=pd.DataFrame(index=dates)

    symbols = ["SPY","TSLA","NVDA","AMZN"]
    for symbol in symbols:
        df_buff = get_df(symbol)
        df_buff = df_buff.rename(columns={"Adj Close":symbol})
        df1 = df1.join(df_buff, how="inner")
    #df1 = df1.dropna()
    print(df1)


if __name__ == "__main__":
    test_run()
    print('~~done~~')