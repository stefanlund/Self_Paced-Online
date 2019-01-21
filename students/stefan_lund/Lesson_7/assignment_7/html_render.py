#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

class Doctype:
    tag = "<!DOCTYPE html>"

    def render(self, out_file):
        if self.tag == "html":
            out_file.write(Doctype.tag)
            out_file.write("\n")
        Element._render(self, out_file)


# This is the framework for the base class
class Element(Doctype):

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

    def _render(self, out_file):

        out_file.write(self._start_tag())

        # if self.tag == "ul":
        #     print('self.tag == "ul", self.contents: ', self.contents, self.tag)
        #     print(str(**self.kwargs))

        if self.contents[0] is not None:    # added for class Ul
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

class Ul(Element):
    # <ul id="TheList" style="line-height:200%"> </ul>
    tag = "ul"
    def __init__(self, content=None, **kwargs):
        super().__init__(content, Ul.tag, **kwargs)

class Li(Element):
    # <li style="color: red">\ncontent\n</li>\n
    tag = "li"
    def __init__(self, content=None, **kwargs):
        super().__init__(content, Li.tag, **kwargs)

class OneLineTag(Element):

    def append(self, new_content):
        # If the append method is evoked, NotImplementedError is raised
        raise NotImplementedError

    def render(self, out_file):
    #     # cont = str(*self.contents)

        cont = self.contents[0]
        local_start_tag = self._start_tag()[:-1]
    #     local_end_tag = self._end_tag()

        if self.tag == "a":
            local_start_tag = local_start_tag[:-1]
            cont = ">" + cont
    #
        out_file.write(local_start_tag + cont + self._end_tag())

    #     if self.tag == "h":
    #         print(self.kwargs.items())
    #         levl = str(self.kwargs["level"])
    #         local_start_tag = local_start_tag[:2] + levl + local_start_tag[-1:]
    #         local_end_tag = local_end_tag[:3] + levl + local_end_tag[3:]
    #
    #     out_file.write(local_start_tag + cont + local_end_tag)

class Title(OneLineTag):
    # <title>Python Class Sample page</title>
    tag = "title"
    def __init__(self, content=None):
        super().__init__(content, Title.tag)

class A(OneLineTag):
    # <a href="http://google.com">link</a>
    tag = "a"
    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, A.tag, **kwargs)

class H(OneLineTag):
    # <h2>Python Class - Html rendering example</h2>
    tag = "h"

    def __init__(self, level, content=None, **kwargs):
        if not (isinstance(level, int) and 0 < level < 7):
            raise ValueError("'level' has to be an integer between 1 and 6")

        self.level = level
        self.tag = H.tag + str(self.level)
        # self.level = level
        # kwargs['level'] = level
        super().__init__(content, self.tag, **kwargs)

    # Not realizing the benefit of making the class attribute "tag" to an instance
    # variable I wrote this instead. Works with the out commented lines in render method.
    # def __init__(self, level, content=None, **kwargs):
    #     if not (isinstance(level, int) and 0 < level < 7):
    #         raise ValueError("'level' has to be an integer between 1 and 6")
    #     self.level = level
    #     kwargs['level'] = level
    #     super().__init__(content, H.tag, **kwargs)


class SelfClosingTag(Element):

    def __init__(self, content, tag, **kwargs):
        # SelfClosingTag element raises an exception if someone tries to put in any content
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content, tag, **kwargs)

    def append(self, new_content):
        raise TypeError("SelfClosingTag can not contain any content")

    def render(self, out_file):
        out_file.write(self._open_tag() + " /" + self._close_tag())


class Hr(SelfClosingTag):
    # <hr />
    tag = "hr"
    def __init__(self, content=None, **kwargs):
        super().__init__(content, Hr.tag, **kwargs)

class Br(SelfClosingTag):
    tag = "br"
    def __init__(self, content=None, **kwargs):
        super().__init__(content, Br.tag, **kwargs)

class Meta(SelfClosingTag):
    # <meta charset="UTF-8" />
    tag = "meta"
    def __init__(self, content=None, **kwargs):
        super().__init__(content, Meta.tag, **kwargs)
