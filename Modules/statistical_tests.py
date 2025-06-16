from scipy.stats import ttest_ind, mannwhitneyu, kruskal

def run_tests(pre_event, post_event):
    t_stat, t_p = ttest_ind(pre_event, post_event)
    w_stat, w_p = mannwhitneyu(pre_event, post_event,alternative='two-sided')
    k_stat, k_p = kruskal(pre_event, post_event)
    return {'t-test': t_p, 'Mann-Whitney': w_p, 'Kruskal': k_p}

