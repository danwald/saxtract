"""Console script for saxtract."""
#!/usr/bin/env python3

import sys
import click
from .saxtract import Saxtract


@click.command()
@click.argument('tags', nargs=-1, default=None)
@click.option('--instream', type=click.File('r'), default=sys.stdin)
@click.option('--outstream', type=click.File('w'), default=sys.stdout)
def main(tags, instream, outstream):
    """Console script for saxtract."""
    # override the default ContextHandler
    handler = Saxtract(tags=tags, instream=instream, outstream=outstream)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
