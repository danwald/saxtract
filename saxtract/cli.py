"""Console script for saxtract."""
#!/usr/bin/env python3

import sys
import click
from saxtrack.saxtract import SAXHandler


@click.command()
def main(args=None):
    """Console script for saxtract."""
    click.echo("Replace this message by putting your code into "
               "saxtract.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
     # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    handler = SAXHandler()
    parser.setContentHandler(handler)
    parser.parse(sys.stdin)
	return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
