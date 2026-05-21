import re

def extract_markdown_images(text: str):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text: str):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def markdown_to_blocks(markdown: str):
    delimit_by_newline = markdown.split("\n\n")
    new_list = []

    for i in range(0, len(delimit_by_newline)):
        delimit_by_newline[i] = delimit_by_newline[i].strip()

        if delimit_by_newline[i] != "":
            new_list.append(delimit_by_newline[i])

    
    return new_list