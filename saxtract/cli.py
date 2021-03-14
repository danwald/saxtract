"""Console script for saxtract."""
#!/usr/bin/env python3

import sys
import click
from saxtrack.saxtract import Saxtract


@click.command()
def main(args=None):
    """Console script for saxtract."""
    click.echo("Replace this message by putting your code into "
               "saxtract.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    # override the default ContextHandler
    handler = Saxtract()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
