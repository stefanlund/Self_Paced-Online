#!/usr/bin/env python3.7
# By Lou Reis

"""
A class-based system for rendering html.

def __init__(self, content=None, **kwargs):
"""


# This is the framework for the base class
class Element(object):
    tag = 'html'

    def __init__(self, content=None, **kwargs):
        if content is not None:
            self.contents = [content]
            print("contents is:", self.contents)
        else:
            self.contents = []

    def append(self, new_content):
        self.contents.append(new_content)

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))

class Body(Element):
    tag = 'body'

class Html(Element):
    tag = 'html'

class P(Element):
    tag = 'p'

class Head(Element):
    tag = 'head'

class OneLineTag(Element):
    def render(self, out_file):
        # loop through the list of contents:
        for key, value in self.attributes:
            open_tag = ["<{}".format(self.tag)]
            open_tag.append(">\n")
            out_file.write("".join(open_tag))
        out_file.write("<{}>".format(self.tag))
        out_file.write(self.contents[0])
        out_file.write("</{}>\n".format(self.tag))
    def append(self, content):
        raise NotImplementedError

class Title(OneLineTag):
    tag = 'title'
