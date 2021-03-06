"""Main module."""
'''plagirised from https://www.tutorialspoint.com/python3/python_xml_processing.htm'''
from xml import sax

class SAXHandler(sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.xtag = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData in ("refno",'listing_pk',):
            print(self.xtag)
            self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData in ("refno",'listing_pk',):
            self.xtag = content
