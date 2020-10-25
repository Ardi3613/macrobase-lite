import click

from mb_lite.pipeline import batch_pipeline


@click.command()
@click.argument("data", type=click.Path(exists=True))
def main(data):
    click.echo(batch_pipeline(data))


if __name__ == "__main__":
    main()
