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

        # out_file.write(self._open_tag() + self._close_tag())
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
        # out_file.write("</{}".format(self.tag) + self._close_tag())
        out_file.write(self._end_tag())

    # def render_with_kwargs(self):
    #
    #     string = ""
    #     if self.kwargs:
    #         for k, v in self.kwargs.items():
    #             string += ' {}="{}"'.format(k, v)
    #     return string

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

    def __init__(self, content=None, tag="html", **kwargs):
        self.content = content
        self.tag = tag
        self.kwargs = kwargs
        # Element.__init__(self, content, tag, **kwargs)
        super().__init__(content, tag, **kwargs)

class Body(Element):

    def __init__(self, content=None, tag="body"):
        # self.content = content
        self.tag = tag
        super().__init__(content, tag)

class P(Element):

    def __init__(self, content=None, tag="p", **kwargs):
        # self.content = content
        self.tag = tag
        self.kwargs = kwargs
        super().__init__(content, tag, **kwargs)

class Head(Element):

    def __init__(self, content=None, tag="head"):
        self.tag = tag
        super().__init__(content, tag)


class OneLineTag(Element):

    def render(self, out_file):
        # cont = str(*self.contents)

        cont = self.contents[0]
        local_start_tag = self._start_tag()[:-1]
        # out_file.write("<{}>{}</{}>\n".format(self.tag, cont, self.tag))
        # if self.tag == "title":
        #     out_file.write(self._start_tag()[:-1] + cont + self._end_tag())
        if self.tag == "a":
            local_start_tag = local_start_tag[:-1]
            cont = ">" + cont
            # out_file.write(self._start_tag()[:2] + cont + self._end_tag())

        out_file.write(local_start_tag + cont + self._end_tag())

    def append(self, new_content):
        # If the append method is evoked, NotImplementedError is raised
        raise NotImplementedError


class Title(OneLineTag):
    # tag = "title"
    def __init__(self, content=None, tag="title"):
        self.tag = tag
        super().__init__(content, tag)

class A(OneLineTag):

    def __init__(self, link, content=None, **kwargs):
        self.content = content
        tag = "a"
        kwargs['href'] = link
        super().__init__(content, tag, **kwargs)

    # def render(self, out_file):
    #     # <a href="http://google.com">link</a>
    #
    #     cont = self.contents[0]
    #     out_file.write(self._open_tag() + ">" + cont + "</" + self.tag + self._close_tag())


class SelfClosingTag(Element):

    def __init__(self, content, tag, **kwargs):
        self.tag = tag
        self.kwargs = kwargs
        # SelfClosingTag element raises an exception if someone tries to put in any content
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content, tag, **kwargs)

    def append(self, new_content):
        raise TypeError("You can not add content to a SelfClosingTag")

    def render(self, out_file):
        out_file.write(self._open_tag() + " /" + self._close_tag())


class Hr(SelfClosingTag):

    def __init__(self, content=None, tag="hr", **kwargs):
        self.tag = tag
        self.kwargs = kwargs
        super().__init__(content, tag, **kwargs)

class Br(SelfClosingTag):

    def __init__(self, content=None, tag="br", **kwargs):
        self.tag = tag
        self.kwargs = kwargs
        super().__init__(content, tag, **kwargs)
