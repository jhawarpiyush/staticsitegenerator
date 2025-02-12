# import ast


class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        htmlnode = ""
        # props = ast.literal_eval(props)

        for k, v in self.props.items():
            htmlnode += f' {k}="{v}"'
        return htmlnode
    
    # def props_to_html(self): (Original)
    #     if self.props is None:
    #         return ""
    #     props_html = ""
    #     for prop in self.props:
    #         props_html += f' {prop}="{self.props[prop]}"'
    #     return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    # def __repr__(self): (Original)
    #     return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, None)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: tag is missing.")
        if self.children is None:
            raise ValueError("invalid HTML: children is missing.")
        child_html = ""
        for child in self.children:
            child_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
  

#   class ParentNode(HTMLNode): (Original)
#     def __init__(self, tag, children, props=None):
#         super().__init__(tag, None, children, props)

#     def to_html(self):
#         if self.tag is None:
#             raise ValueError("invalid HTML: no tag")
#         if self.children is None:
#             raise ValueError("invalid HTML: no children")
#         children_html = ""
#         for child in self.children:
#             children_html += child.to_html()
#         return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

#     def __repr__(self):
#         return f"ParentNode({self.tag}, children: {self.children}, {self.props})"