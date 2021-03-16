"""Console script for saxtract."""
#!/usr/bin/env python3

import sys
import click
from .saxtract import Saxtract


@click.command()
@click.argument('input', type=click.File('-', mode='rb'))
@click.argument('output', type=click.File('-', mode='w'))
@click.argument('tags', nargs=-1, default=None)
def main(input, output, tags):
    """Console script for saxtract."""
    # override the default ContextHandler
    handler = Saxtract(tags=tags, insteam=input, outstream=output)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
