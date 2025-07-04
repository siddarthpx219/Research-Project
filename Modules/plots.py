import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_car_time_series(df):
    """
    Plot Graph 1: Time series of Cumulative Abnormal Returns (CAR)
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['CAR'], label='CAR', color='blue')
    plt.title('Graph 1: Time Series of Cumulative Abnormal Returns (CAR)')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Abnormal Returns')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_garch_volatility(df):
    """
    Plot Graph 2: Volatility estimates via GARCH model
    Assumes that 'GARCH_Volatility' column exists in the DataFrame.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['GARCH_Volatility'], label='Estimated Volatility', color='orange')
    plt.title('Graph 2: Volatility Estimates via GARCH')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
