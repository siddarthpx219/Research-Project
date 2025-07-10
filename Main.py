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
from Modules.plots import plot_car_time_series, plot_garch_volatility, plot_net_car_garch
from Modules.summary_generator import generate_summary
#from Modules.maps import plot_cyclone_paths_with_impact

# --- CONFIG ---
tickerTemp= pd.read_csv('Research-Project/ResearchProjectstocks.csv')
##print("Available Tickers DataFrame:\n", tickerTemp)
dic= tickerTemp.groupby('sector')['Ticker_ID'].apply(list).to_dict()
print(dic)
TICKER = tickerTemp['Ticker_ID'].unique()  # This is now a list of tickers
##print("Available Tickers:", TICKER)
sector_wise_results = {}  # To store sector-wise results
START_DATE = '2013-01-01'
END_DATE = '2023-01-01'
WINDOW = 5
# --- MAIN PIPELINE ---
all_results = []  # To store results for each ticker
def run_pipeline():
    # Step 1: Fetch Data
    for sector, tickers in dic.items():
        print(f"Processing sector: {sector}")
        for TICKER in tickers:
            ##print("Fetching cyclone and stock data...", TICKER)
            cyclone_df = get_cyclone_data()
            stock_df = get_stock_data(TICKER, START_DATE, END_DATE)
            stock_df = stock_df[TICKER].copy()
            print(TICKER)


            # Step 2: Preprocess Data
            ##print("Cleaning and merging data...")
            cyclone_df = clean_cyclone_data(cyclone_df)
            ##print(stock_df)
            stock_df = compute_returns(stock_df)
            stock_df = tag_event_window(stock_df, cyclone_df, window=WINDOW)

            # Step 3: Event Study
            ##print("Performing event study...")
            market_return = stock_df['Log_Return'].mean()  # Placeholder
            stock_df = compute_ar_car(stock_df, market_return)

            # Step 4: Statistical Tests
            ##print("Running statistical tests...")
            pre_event = stock_df[stock_df['Event'] == 0]['Log_Return']
            post_event = stock_df[stock_df['Event'] == 1]['Log_Return']
            test_results = run_tests(pre_event, post_event)
            p_values_df=pd.DataFrame(test_results,index=[1,2,3])
            ##print("Test Results:\n", p_values_df)

            # Step 5: Volatility Modeling
            #print("Fitting GARCH model...")
            stock_df['Volatility'] = fit_garch(stock_df['Log_Return'])

            # Step 6: Granger Causality
            #print("Running Granger Causality...")
            granger_df = pd.concat([stock_df['Log_Return'], stock_df['Event']], axis=1).dropna()
            granger_result = run_granger(granger_df)

            # Step 7: Anomaly Detection
            #print("Detecting anomalies...")
            stock_df = detect_anomalies(stock_df)
            
            # Step 8: Visualization
            #print("Plotting results...")
            plot_car_time_series(stock_df, TICKER, sector) 
            ##print(stock_df)
            plot_garch_volatility(stock_df, TICKER, sector)
            #step 8.5: Maps
            ##print("Displaying maps")
            
            #Step 9: Reporting
            #print("Generating summary report...")
            summary_df = generate_summary(test_results, granger_result, stock_df)
            ##print(summary_df)
        
            all_results.append({
            'Ticker': TICKER,
            'Sector': sector,
            't-test': test_results['t-test'],
            'mann-whitney': test_results['Mann-Whitney'],
            'kruskal': test_results['Kruskal'],
            'CAR': stock_df['CAR'].mean(),
            'Volatility': stock_df['Volatility'].mean()
            #'Granger_Causality': granger_result
        })
            #print(f"Completed analysis for {TICKER}")
        
        # Step 10: Final Reporting
        #print("Generating final report...")
    final_summary = pd.DataFrame(all_results)
    print(final_summary)
    print(sector_wise_results)
    print(final_summary.drop(columns=['Ticker','Sector']).mean())
    #print("Plotting results...")
    sector_wise_stats = final_summary.groupby('Sector').mean(numeric_only=True)
    print("Sector-wise Mean Statistics:\n", sector_wise_stats)
    #plot_car_time_series(final_summary) 
    plot_net_car_garch(final_summary)
    ##print(stock_df)

if __name__ == "__main__":
    run_pipeline()