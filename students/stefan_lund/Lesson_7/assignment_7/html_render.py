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

    def append(self, new_content, **kwargs):
        if self.contents[0] is None:
            self.contents = []
        self.contents.append(new_content)

        if kwargs:
            if self.kwargs:
                self.kwargs.update(**kwargs)
            else:
                self.kwargs = kwargs

    def render(self, out_file):

        out_file.write(self._start_tag())

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
        out_file.write(self._end_tag())

    def _start_tag(self):
        string = self._open_tag() + self._close_tag()
        return string

    def _end_tag(self):
        string = "</{}".format(self.tag) + self._close_tag()
        return string

    def _open_tag(self):

        string = "<{}".format(self.tag)
        for k, v in self.kwargs.items():
            string += ' {}="{}"'.format(k, v)
        return string

    def _close_tag(self):
        close_tag = ">\n"
        return close_tag

class Html(Element):
    tag = "html"
    def __init__(self, content=None, **kwargs):
        super().__init__(content, Html.tag, **kwargs)

class Body(Element):
    tag = "body"
    def __init__(self, content=None):
        super().__init__(content, Body.tag)

class P(Element):
    tag = "p"
    def __init__(self, content=None, **kwargs):
        super().__init__(content, P.tag, **kwargs)

class Head(Element):
    tag = "head"
    def __init__(self, content=None):
        super().__init__(content, Head.tag)


class OneLineTag(Element):

    def append(self, new_content):
        # If the append method is evoked, NotImplementedError is raised
        raise NotImplementedError

    def render(self, out_file):
        # cont = str(*self.contents)

        cont = self.contents[0]
        local_start_tag = self._start_tag()[:-1]

        if self.tag == "a":
            local_start_tag = local_start_tag[:-1]
            cont = ">" + cont

        out_file.write(local_start_tag + cont + self._end_tag())


class Title(OneLineTag):
    tag = "title"
    def __init__(self, content=None):
        super().__init__(content, Title.tag)

class A(OneLineTag):
    tag = "a"
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, A.tag, **kwargs)


class SelfClosingTag(Element):

    def __init__(self, content, tag, **kwargs):
        # SelfClosingTag element raises an exception if someone tries to put in any content
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content, tag, **kwargs)

    def append(self, new_content):
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, out_file):
        out_file.write(self._open_tag() + " /" + self._close_tag())


class Hr(SelfClosingTag):
    tag = "hr"
    def __init__(self, content=None, **kwargs):
        super().__init__(content, Hr.tag, **kwargs)

class Br(SelfClosingTag):
    tag = "br"
    def __init__(self, content=None, **kwargs):
        super().__init__(content, Br.tag, **kwargs)
