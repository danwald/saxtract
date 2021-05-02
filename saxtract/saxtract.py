import xml.sax

"""Main module."""
'''plagirised from https://www.tutorialspoint.com/python3/python_xml_processing.htm'''


class Saxtract(xml.sax.ContentHandler):
    def __init__(self, tags, instream, outstream, child_tag, show_tags, verbose):
        self.tags = set(tags)
        self.instream = instream
        self.outstream = outstream
        self.child_tag = child_tag
        self.show_tags = show_tags
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
            self.outstream.write(f'{content}')

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.current_tag = tag

    def _relevant_data(self, struct, data):
        return True if data in struct or not struct else False

    def _add_newline(self, tag):
        return True if tag == self.child_tag else False

    def _show_tag(self, tag):
        return True if all([tag, self.show_tags, self._relevant_data(self.tags, tag)]) else False

    def _show_content(self):
        return True if self.current_content else False

    # Call when an elements ends
    def endElement(self, tag):
        if self._show_tag(tag):
            self._output(f'{self.current_tag}: ')
        if self._show_content():
            self._output(f'{self.current_content},')
        if self._add_newline(tag):
            self._output('\n')

        self.current_tag = self.current_content = ''

    # Call when a character is read
    def characters(self, content):
        if self._relevant_data(self.tags, self.current_tag):
            self.current_content += content
