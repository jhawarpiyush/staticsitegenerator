from enum import Enum
from inline_markdown_split import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import ParentNode


class BlockType(Enum):
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    PARAGRAPH = "paragraph"


def markdown_to_blocks(markdown):
    blocks_markdown = markdown.split("\n\n")
    block_list = []
    for block in blocks_markdown:
        if block:
            block_list.append(block.strip())
    return block_list


def block_to_block_type(block):
    if (block.startswith("# ") or block.startswith("## ") or block.startswith("### ") or block.startswith("#### ") or block.startswith("##### ") or block.startswith("###### ")):
        return BlockType.HEADING
    if block[0:3] == "```" and block[-3:] == "```":
        return BlockType.CODE
    if block.startswith(">"):
        return BlockType.QUOTE
    if block.startswith("* ") or block.startswith("- "):
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    htmlcode = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        html_node = block_to_html_node(block)
        htmlcode.append(html_node)
    return ParentNode("div", htmlcode, None)


def block_to_html_node(block):
    if block_to_block_type(block) == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_to_block_type(block) == BlockType.CODE:
        return code_to_html_node(block)
    if block_to_block_type(block) == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_to_block_type(block) == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    if block_to_block_type(block) == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)
    if block_to_block_type(block) == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def unordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def ordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children
