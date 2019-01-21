import pandas as pd

def test_run():
    df = pd.read_csv("TSLA.csv")
    print( df.tail( 10)[2:4:] )

if __name__ == "__main__":
    test_run()

