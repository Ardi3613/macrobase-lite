from efficient_apriori import apriori


def filter_non_cat(df):
    """Filter non-categorical columns away."""
    non_cat = [ind for ind, dtype in enumerate(df.dtypes) if dtype == "object"]
    non_cat = df.columns[non_cat]
    return df[non_cat]


def explain(df):
    """Provide explanations for the ."""
    df_categorical = filter_non_cat(df)
    transactions_from_df = [tuple(row) for row in df_categorical.values.tolist()]
    _, rules = apriori(transactions_from_df)
    return rules


def risk_ratio(attr_combination: dict, df) -> float:
    """Calculate risk ratio between two sets of attributes."""
    outliers = df[df["outlier"] == "outlier"]
    inliers = df[df["outlier"] == "inlier"]
    out_with_attr = filter_on_attrs(outliers, attr_combination)
    in_with_attr = filter_on_attrs(inliers, attr_combination)
    a0 = len(out_with_attr.index)
    ai = len(in_with_attr.index)
    b0 = len(outliers.index) - a0
    bi = len(inliers.index) - ai
    top = a0 / (a0 + ai)
    denom = b0 / (b0 + bi)
    return top / denom


def filter_on_attrs(df, attrs: dict):
    for column, value in attrs.items():
        df = df[df[column] == value]
    return df
