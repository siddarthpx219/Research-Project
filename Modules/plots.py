import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')  # Use a non-interactive backend for plotting
import matplotlib.dates as mdates


def plot_car_time_series(df,TICKER,sector):
    """
    Plot Graph 1: Time series of Cumulative Abnormal Returns (CAR)
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['CAR'], label='CAR', color='blue')
    plt.title('Graph 1: Time Series of Cumulative Abnormal Returns (CAR) for ' + TICKER + ' (Sector: ' + sector + ')')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Abnormal Returns')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    #plt.show()
    plt.savefig('Graph1_CAR_' + TICKER + '- ' + sector + '.png', dpi=300)  # Save the plot as a PNG file
    plt.close()  # Close the plot to free up memory


def plot_garch_volatility(df, TICKER,sector):
    """
    Plot Graph 2: Volatility estimates via GARCH model
    Assumes that 'GARCH_Volatility' column exists in the DataFrame.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Volatility'], label='Estimated Volatility', color='orange')
    plt.title('Graph 2: Volatility Estimates via GARCH for ' + TICKER + ' (Sector: ' + sector + ')')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    #plt.show()
    plt.savefig('Graph2_GARCH_' + TICKER + '- ' + sector + '.png', dpi=300)  # Save the plot as a PNG file
    plt.close()  # Close the plot to free memory