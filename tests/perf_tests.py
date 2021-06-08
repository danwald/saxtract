#!/usr/bin/env python3 # noqa: E265

import os
import sys
from timeit import Timer
from xml.dom.minidom import parse
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
        Saxtract(tag, instream, open(os.devnull, 'w'), None, False, False).start()


def dom(filename, tag):
    with open(filename, 'r') as instream:
        stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
        try:
            DOMTree = parse(instream)
            collection = DOMTree.documentElement
            tags = collection.getElementsByTagName(tag)
            for user_tag in tags:
                print(user_tag)
        except Exception as e:
            sys.stderr.write(f'Error occurred: {e}\n')
            pass
        finally:
            sys.stdout = stdout


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
