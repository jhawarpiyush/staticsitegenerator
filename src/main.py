from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown_split import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_link, text_to_textnodes
from textnode import TextNode, text_node_to_html_node, TextType


def main():
    # node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # htmlnode = HTMLNode(props={"href": "https://www.google.com","target": "_blank"})
    # print(htmlnode.props_to_html())

    # node = ParentNode("p",[LeafNode("b", "Bold text"),LeafNode(None, "Normal text"),LeafNode("i", "italic text"),LeafNode(None, "Normal text"),LeafNode("a", "ddf", "{'a':'b'}"),],)
    # print(node.to_html())
    # node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
    # print(text_node_to_html_node(node))

    # node = TextNode("This is text with a `code block` word", TextType.TEXT)
    # new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    # print(new_nodes)
    
    # text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # extract_markdown_images(text)

    # text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # print(extract_markdown_links(text))

    # node = TextNode(
    # "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    # TextType.TEXT,)
    # new_nodes = split_nodes_link([node])

    text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")


if __name__ == "__main__":
    main()
