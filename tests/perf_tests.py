#!/usr/bin/env python3 # noqa: E265

from timeit import Timer
import sys

import click

from saxtract.saxtract import Saxtract

@click.command()
@click.option('--filename', prompt='Enter your test xml file')
@click.option('--tag', prompt='Enter the tag you wish to extract')
def main(filename, tag):
    runs = 1
    sax_time = Timer('sax(filename, tag)',
                     setup=(f'from __main__ import sax, dom;filename="{filename}"; tag="{tag}";'),
                     globals=globals(),
                     ).timeit(number=runs)
    dom_time = Timer('dom(filename, tag)',
                     setup=(f'from __main__ import sax, dom;filename="{filename}"; tag="{tag}";'),
                     globals=globals(),
                     ).timeit(number=runs)
    print(f'Sax run took ~{sax_time}ms Dom run took ~{dom_time}ms')


def sax(filename, tag):
    print(f'{filename} {tag}')
    with open(filename, 'r') as instream:
        Saxtract(tag, instream, open('/dev/null', 'w'), None, False, False).start()


def dom(filename, tag):
    with open(filename, 'r') as instream:
        pass
    pass


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
