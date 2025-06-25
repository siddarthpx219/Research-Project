import pandas as pd
from Modules.cyclone_fetcher import get_cyclone_data
from Modules.stock_fetcher import get_stock_data
from Modules.cyclone_cleaner import clean_cyclone_data
from Modules.stock_cleaner import compute_returns
from Modules.merger import tag_event_window
from Modules.event_study import compute_ar_car
from Modules.statistical_tests import run_tests
from Modules.garch_volatility import fit_garch
from Modules.granger_test import run_granger
from Modules.anomaly_detection import detect_anomalies
from Modules.plots import plot_returns, plot_car
#from Modules.summary_generator import generate_summary

# --- CONFIG ---
TICKER = 'RELIANCE.NS'
START_DATE = '2018-01-01'
END_DATE = '2022-01-01'
WINDOW = 5
# --- MAIN PIPELINE ---
def run_pipeline():
    # Step 1: Fetch Data
    print("Fetching cyclone and stock data...")
    cyclone_df = get_cyclone_data()
    stock_df = get_stock_data(TICKER, START_DATE, END_DATE)
    stock_df = stock_df[TICKER].copy()

    # Step 2: Preprocess Data
    print("Cleaning and merging data...")
    cyclone_df = clean_cyclone_data(cyclone_df)
    stock_df = compute_returns(stock_df)
    stock_df = tag_event_window(stock_df, cyclone_df, window=WINDOW)

    # Step 3: Event Study
    print("Performing event study...")
    market_return = stock_df['Log_Return'].mean()  # Placeholder
    stock_df = compute_ar_car(stock_df, market_return)

    # Step 4: Statistical Tests
    print("Running statistical tests...")
    pre_event = stock_df[stock_df['Event'] == 0]['Log_Return']
    post_event = stock_df[stock_df['Event'] == 1]['Log_Return']
    test_results = run_tests(pre_event, post_event)
    print("Test Results:\n", test_results)

    # Step 5: Volatility Modeling
    print("Fitting GARCH model...")
    stock_df['Volatility'] = fit_garch(stock_df['Log_Return'])

    # Step 6: Granger Causality
    print("Running Granger Causality...")
    granger_df = pd.concat([stock_df['Log_Return'], stock_df['Event']], axis=1).dropna()
    granger_result = run_granger(granger_df)

    # Step 7: Anomaly Detection
    print("Detecting anomalies...")
    stock_df = detect_anomalies(stock_df)

    # Step 8: Visualization
    print("Plotting results...")
    plot_returns(stock_df)
    plot_car(stock_df)

    # Step 9: Reporting
    #print("Generating summary report...")
    #summary_df = generate_summary(test_results)
    #print(summary_df)

if __name__ == "__main__":
    run_pipeline()