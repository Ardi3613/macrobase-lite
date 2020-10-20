from efficient_apriori import apriori


def filter_non_cat(df):
    """Filter non-categorical columns away."""
    non_cat = [ind for ind, dtype in enumerate(df.dtypes) if dtype != "object"]
    return df[non_cat]


def explain(df):
    df_categorical = filter_non_cat(df)
    itemsets, rules = apriori(df_categorical)
    return rules
