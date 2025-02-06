from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, text_node_to_html_node, TextType


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # htmlnode = HTMLNode(props={"href": "https://www.google.com","target": "_blank"})
    # print(htmlnode.props_to_html())

    # node = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),LeafNode("a", "ddf", "{'a':'b'}"),],)
    # print(node.to_html())
    node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
    print(text_node_to_html_node(node))


if __name__ == "__main__":
    main()
