#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    def __init__(self, content=None, tag="html", **kwargs):
        self.contents = [content]
        self.tag = tag
        self.kwargs = kwargs
        # print("self.kwargs: ", self.kwargs)
        # print("self.kwargs.items(): ", self.kwargs.items())
        # for k in self.kwargs.keys():
            # print("k: ", k, type(k))
        # print("self.kwargs.keys(): ", self.kwargs.keys())

    def append(self, new_content):
        if self.contents[0] is None:
            self.contents = []
        self.contents.append(new_content)
        return self.contents

    def render(self, out_file):
        # loop through the list of contents:
        if self.kwargs:
            out_file.write("<{}".format(self.tag))
            out_file.write(self.render_with_kwargs())       #######
            # for k, v in self.kwargs.items():
            #     out_file.write(' {}="{}"'.format(k, v))
            out_file.write(">\n")
        else:
            out_file.write("<{}>\n".format(self.tag))

        for content in self.contents:
            # out_file.write("<{}>\n".format(self.tag))
            # try:
            #     content.render(out_file)
            # except AttributeError:
            #     out_file.write(content)
            if hasattr(content, 'tag'):
                content.render(out_file)
            else:
                out_file.write(content)
                out_file.write("\n")
        out_file.write("</{}>\n".format(self.tag))

    def render_with_kwargs(self):                       #######
        string = ""
        for k, v in self.kwargs.items():
            string += ' {}="{}"'.format(k, v)
        return string

    def _open_tag(self):
        pass

    def _close_tag(self):
        pass

class Html(Element):

    # def __init__(self, content=None, tag="html"):
    #     self.content = content
    #     self.tag = tag
    #     Element.__init__(self, content, tag)

    def __init__(self, content=None):
        Element.__init__(self, content)

class Body(Element):

    def __init__(self, content=None, tag="body"):
        # self.content = content
        self.tag = tag
        Element.__init__(self, content, tag)

class P(Element):

    def __init__(self, content=None, tag="p", **kwargs):
        # self.content = content
        self.tag = tag
        self.kwargs = kwargs
        Element.__init__(self, content, tag, **kwargs)

class Head(Element):

    def __init__(self, content=None, tag="head"):
        self.tag = tag
        Element.__init__(self, content, tag)


class OneLineTag(Element):

    def render(self, out_file):
        # cont = str(*self.contents)
        cont = self.contents[0]
        out_file.write("<{}>{}</{}>\n".format(self.tag, cont, self.tag))

    def append(self, new_content):
        # If the append method is evoked, NotImplementedError is raised
        raise NotImplementedError


class Title(OneLineTag):
    # tag = "title"
    def __init__(self, content=None, tag="title"):
        self.tag = tag
        OneLineTag.__init__(self, content, tag)


class SelfClosingTag(Element):

    def render(self, out_file):

        if self.kwargs:
            out_file.write("<{}".format(self.tag))
            out_file.write(self.render_with_kwargs())       ########
            # for k, v in self.kwargs.items():
            #     out_file.write(' {}="{}"'.format(k, v))
            out_file.write(" />\n")
        else:
            out_file.write("<{} />\n".format(self.tag))


class Hr(SelfClosingTag):

    def __init__(self, content=None, tag="hr", **kwargs):
        self.tag = tag
        self.kwargs = kwargs
        SelfClosingTag.__init__(self, content, tag, **kwargs)
