import click

from mb_lite.classification import AdrMAD
from mb_lite.explanation import explain
from mb_lite.ingest import ingest
from mb_lite.present import present
from mb_lite.transform import transform


@click.command()
@click.argument(
    "data", help="Tabulated data to be analyzed", type=click.Path(exists=True)
)
def main(data):
    df = ingest(data)
    df = transform(df)
    adr = AdrMAD(df)
    explanations = explain(adr)
    present(explanations)


if __name__ == "__main__":
    main()
