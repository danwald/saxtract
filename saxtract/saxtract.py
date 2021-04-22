import xml.sax

"""Main module."""
'''plagirised from https://www.tutorialspoint.com/python3/python_xml_processing.htm'''


class Saxtract(xml.sax.ContentHandler):
    def __init__(self, tags, instream, outstream, verbose):
        self.tags = tags
        self.instream = instream
        self.outstream = outstream
        self.verbose = verbose

        self.current_tag = ''
        self.current_content = ''
        if self.verbose:
            self._output(f'Tags: {",".join(tags)}')

        self._init_parser()
        self.parser.parse(self.instream)

    def _init_parser(self):
        self.parser = xml.sax.make_parser()
        # turning off namepsaces
        self.parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        self.parser.setContentHandler(self)

    def _output(self, content):
        if self.outstream:
            self.outstream.write(f'\n{content}')

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.current_tag = tag

    # Call when an elements ends
    def endElement(self, tag):
        if self.current_tag and not self.tags or self.current_tag in self.tags:
            self._output(f'{self.current_tag}: {self.current_content}')
        self.current_tag = ''

    # Call when a character is read
    def characters(self, content):
        if not self.tags or self.current_tag in self.tags:
            self.current_content = content
