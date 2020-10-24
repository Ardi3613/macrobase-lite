"""Produce human readable interpretation of the data."""


def present(outliers, rules) -> str:
    human_str = "Outliers\n"
    human_str += outliers.to_string()
    human_str += "\nCauses\n"
    human_str += _format_rules(rules)
    return human_str


def _format_rules(rules):
    causes = [str(r) for r in rules if "outlier" in r.rhs]
    return "\n".join(causes)
