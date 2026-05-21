from textnode import TextType, TextNode
from lib.markdown  import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter: str, text_type):
    valid_delimiters = ["`", "*", "_", "**"]

    if delimiter not in valid_delimiters:
        raise Exception("Invalid markdown! Must be `, * or _.")

    new_list = []
    
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_list.append(node)
            continue

        split = node.text.split(delimiter)

        if len(split) % 2 == 0:
            raise Exception("Closing delimiter not provided")
        
        for i in range(0, len(split)):
            if split[i] == "":
                continue

            if i & 1:
                new_list.append(TextNode(split[i], text_type))
            else:
                new_list.append(TextNode(split[i], TextType.PLAIN))

    return new_list

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.PLAIN))
    return new_nodes