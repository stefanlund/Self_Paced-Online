#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    # tag = "html"

    def __init__(self, content=None, tag="html"):
        self.contents = [content]
        self.tag = tag

    def append(self, new_content):
        if self.contents[0] is None:
            self.contents = []
        self.contents.append(new_content)
        return self.contents

    def render(self, out_file):
    # loop through the list of contents:
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

    # def render(self, out_file):
    #     # out_file.write("just something as a place holder...")
    #     # print("self.__dict__: ", self.__dict__)
    #     # print("self.tag: ", self.tag)
    #     out_file.write("<{}>\n".format(self.tag))
    #     for content in self.contents:
    #         print("content: ", content, type(content))
    #         out_file.write(content + "\n")
    #
    #     out_file.write("</{}>\n".format(self.tag))



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

    def __init__(self, content=None, tag="p"):
        # self.content = content
        self.tag = tag
        Element.__init__(self, content, tag)

class Head(Element):

    def __init__(self, content=None, tag="head"):
        self.tag = tag
        Element.__init__(self, content, tag)

class Title(Element):

    def __init__(self, content=None, tag="title"):
        self.tag = tag
        Element.__init__(self, content, tag)



# under class Element
        # def render(self, out_file):
        #     # and the class objects in the same order
        #     class_obj = []
        #
        #     # start from the top
        #     current_class = self
        #     while hasattr(current_class, 'tag'):
        #         class_obj.append(current_class)
        #         current_class = current_class.contents[0]
        #
        #     for obj in class_obj[:-1]:
        #         # strings to print are in the content of oject next to last one
        #         out_file.write("<{}>\n".format(obj.tag))
        #
        #     for content_list in class_obj[-2].contents:
        #         str_cont = content_list.contents[0]
        #         tg = content_list.tag
        #         out_file.write("<{tg}>\n{str_cont}\n</{tg}>\n".
        #                        format(tg=tg, str_cont=str_cont))
        #     # revers tags to close
        #     r_class_obj = class_obj[-1]
        #     r_class_obj.reverse()
        #     for obj in r_class_obj:
        #         out_file.write("<{}>\n".format(obj.tag))
