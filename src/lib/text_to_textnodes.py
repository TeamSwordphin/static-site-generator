from textnode import TextNode, TextType
from lib.split_node import split_nodes_image, split_nodes_link, split_nodes_delimiter

def text_to_textnodes(default_text: str):
    node = TextNode(default_text, TextType.PLAIN)
    split_1 = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter([node], "**", TextType.BOLD), "`", TextType.CODE), "_", TextType.ITALIC)

    return split_nodes_image(split_nodes_link(split_1))
    