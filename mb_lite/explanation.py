from efficient_apriori import apriori


def filter_non_cat(df):
    """Filter non-categorical columns away."""
    non_cat = [ind for ind, dtype in enumerate(df.dtypes) if dtype == "object"]
    return df[non_cat]


def explain(df):
    """Provide explanations for the ."""
    df_categorical = filter_non_cat(df)
    transactions_from_df = [tuple(row) for row in df_categorical.values.tolist()]
    _, rules = apriori(transactions_from_df)
    return rules
