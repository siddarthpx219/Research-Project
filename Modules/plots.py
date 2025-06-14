import matplotlib.pyplot as plt

def plot_returns(df):
    df['Log_Return'].plot(title='Log Returns Over Time')
    plt.show()

def plot_car(df):
    df['CAR'].plot(title='Cumulative Abnormal Returns')
    plt.show()