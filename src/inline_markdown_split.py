import re


from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("closing markdown delimiter not found.")
        for i, text in enumerate(split_text):
            if text:
                if i % 2 == 0:
                    new_list.append(TextNode(text, node.text_type))
                else:
                    new_list.append(TextNode(text, text_type))
    return new_list


def extract_markdown_images(text):
    imgaltandsrc = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return imgaltandsrc


def extract_markdown_links(text):
    anchortextandlink = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return anchortextandlink


def split_nodes_image(old_nodes):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_list.append(node)
            continue
        for img in images:
            split_text = node.text.split(f"![{img[0]}]({img[1]})", 1)
            if len(split_text) != 2:
                raise ValueError("invalid markdown image not closed")
            if split_text[0]:
                new_list.append(TextNode(split_text[0], node.text_type))
            new_list.append(TextNode(img[0], TextType.IMAGE, img[1]))
            node.text = split_text[1]
        if node.text:
            new_list.append(TextNode(node.text, TextType.TEXT))
    return new_list

def split_nodes_link(old_nodes):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_list.append(node)
            continue
        for link in links:
            split_text = node.text.split(f"[{link[0]}]({link[1]})", 1)
            if len(split_text) != 2:
                raise ValueError("invalid markdown link not closed")
            if split_text[0]:
                new_list.append(TextNode(split_text[0], node.text_type))
            new_list.append(TextNode(link[0], TextType.LINK, link[1]))
            node.text = split_text[1]
        if node.text:
            new_list.append(TextNode(node.text, TextType.TEXT))
    return new_list


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
