#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element(object):

    tag = "html"

    def __init__(self, content=None):
        self.contents = [content]

    def append(self, new_content):
        if self.contents[0] is None:
            self.contents = []
        self.contents.append(new_content)
        return self.contents

    def render(self, out_file):
        # out_file.write("just something as a place holder...")
        out_file.write("<{}>\n".format(self.tag))
        for strng in self.contents:
            out_file.write(strng + "\n")

        out_file.write("</{}>\n".format(self.tag))
