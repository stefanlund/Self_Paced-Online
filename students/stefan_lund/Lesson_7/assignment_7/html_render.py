#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""

class Doctype:
    tag = "<!DOCTYPE html>"

    def render(self, out_file, cur_ind=""):
        if self.tag == "html":
            out_file.write(Doctype.tag)
            out_file.write("\n")

        if cur_ind:
            Element.cur_ind = cur_ind

        Element._render(self, out_file, cur_ind="")


# This is the framework for the base class
class Element(Doctype):

    indent = "    "
    cur_ind = ""

    def __init__(self, content=None, tag=None, **kwargs): # tag="html"
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

    def _render(self, out_file, cur_ind=""):

        change_tag = self._render_default_tag()

        out_file.write(self._start_tag())

        if self.contents[0] is not None:    # added for class Ul
            for content in self.contents:

                if hasattr(content, 'tag'):
                    Element.cur_ind += Element.indent
                    content.render(out_file, self.cur_ind)
                else:
                    out_file.write(self.cur_ind + self.indent)
                    out_file.write(content)
                    out_file.write("\n")
        out_file.write(self.cur_ind + self._end_tag())
        Element.cur_ind = Element.cur_ind[:-len(Element.indent)]

        if change_tag:
            self.tag = None

    def _render_default_tag(self):
        """ Used only if an object Element is created. Element doesn't have it's
            own tag for instance so we give it the html tag just for the render
            exercise. It could be set a a default in the __init__ method but the
            render method would generate the <!DOCTYPE html> before the html
            menaing we would have to change the tests using the Element object
            to pass in some content.
        """
        change_tag = False
        if self.tag is None:
            self.tag = "html"
            change_tag = True
        return change_tag

    def _start_tag(self):
        string = self._open_tag() + self._close_tag()
        return string

    def _end_tag(self):
        string = "</{}".format(self.tag) + self._close_tag()
        return string

    def _open_tag(self):

        string = self.cur_ind + "<{}".format(self.tag)
        for k, v in self.kwargs.items():
            string += ' {}="{}"'.format(k, v)
        return string

    @classmethod
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

    def render(self, out_file, cur_ind=""):
    #     # cont = str(*self.contents)

        cont = self.contents[0]
        local_start_tag = self._start_tag()[:-1]
    #     local_end_tag = self._end_tag()

        if self.tag == "a":
            local_start_tag = local_start_tag[:-1]
            cont = ">" + cont

        out_file.write(local_start_tag + cont + self._end_tag())
        Element.cur_ind = Element.cur_ind[:-len(Element.indent)]


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


class SelfClosingTag(Element):

    def __init__(self, content, tag, **kwargs):
        # SelfClosingTag element raises an exception if someone tries to put in any content
        if content is not None:
            raise TypeError("SelfClosingTag can not contain any content")
        super().__init__(content, tag, **kwargs)

    def append(self, new_content):
        raise TypeError("SelfClosingTag can not contain any content")

    def render(self, out_file, cur_ind=""):
        out_file.write(self._open_tag() + " /" + self._close_tag())
        Element.cur_ind = Element.cur_ind[:-len(Element.indent)]


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
