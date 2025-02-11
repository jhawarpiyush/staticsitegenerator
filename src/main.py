from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown_split import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_link, text_to_textnodes
from textnode import TextNode, text_node_to_html_node, TextType
from block_markdown_split import markdown_to_blocks, markdown_to_html_node


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

    # text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")

    block = '''
    # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
    '''

#     md = """
# This is **bolded** paragraph
# text in a p
# tag here

# """

md = """
# this is an h1

this is paragraph text

###### this is an h2
"""
    
markdown_to_html_node(md)

if __name__ == "__main__":
    main()
