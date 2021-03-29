import xml.sax

"""Main module."""
'''plagirised from https://www.tutorialspoint.com/python3/python_xml_processing.htm'''


class Saxtract(xml.sax.ContentHandler):
    def __init__(self, tags, instream, outstream):
        parser = xml.sax.make_parser()
        # turning off namepsaces
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        parser.setContentHandler(self)

        self.tags = tags
        self.instream = instream
        self.outstream = outstream
        self.current_tag = ''
        self.current_content = ''
        parser.parse(self.instream)

    def _output(self, content):
        if self.outstream:
            self.outstream.write(f'\n{content}')

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.current_tag = tag

    # Call when an elements ends
    def endElement(self, tag):
        if not self.tags or self.current_tag in self.tags:
            self._output(f'{self.current_tag}: {self.current_content}')
        self.current_tag = ''

    # Call when a character is read
    def characters(self, content):
        if not self.tags or self.current_tag in self.tags:
            self.current_content = content
