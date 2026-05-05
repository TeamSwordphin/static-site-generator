from textnode import TextType, TextNode

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
