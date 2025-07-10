import pandas as pd

def generate_summary(test_results, granger_result, stock_df):
    """
    Generate a summary DataFrame of the main results.
    """
    summary = {}

    # Statistical Tests
    summary['T-test p-value'] = test_results.get('t-test')
    summary['Mann-Whitney p-value'] = test_results.get('Mann-Whitney')
    summary['Kruskal p-value'] = test_results.get('Kruskal')

    # GARCH Volatility (mean and max)
    if 'Volatility' in stock_df.columns:
        summary['Mean Volatility'] = stock_df['Volatility'].mean()
        summary['Max Volatility'] = stock_df['Volatility'].max()

    # Granger Causality (example: p-value)
    if hasattr(granger_result, 'pvalue'):
        summary['Granger Causality p-value'] = granger_result.pvalue
    elif isinstance(granger_result, dict) and 'pvalue' in granger_result:
        summary['Granger Causality p-value'] = granger_result['pvalue']
    else:
        summary['Granger Causality Result'] = granger_result

    # Anomaly Detection (count)
    if 'Anomaly' in stock_df.columns:
        summary['Number of Anomalies'] = stock_df['Anomaly'].sum()

    # Convert to DataFrame for pretty #printing
    summary_df = pd.DataFrame([summary])
    return summary_df