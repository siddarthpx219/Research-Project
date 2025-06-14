from arch import arch_model

def fit_garch(returns):
    model = arch_model(returns, vol='Garch', p=1, q=1)
    res = model.fit(disp='off')
    return res.conditional_volatility
