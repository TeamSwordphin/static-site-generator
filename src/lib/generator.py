import os
from pathlib import Path

from blocktype import markdown_to_html_node
from lib.extract_header import extract_title

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = open(from_path, "r")
    markdown_content = markdown.read()
    markdown.close()

    template = open(template_path, "r")
    template_content = template.read()
    template.close()

    node = markdown_to_html_node(markdown_content)
    html_txt = node.to_html()
    title = extract_title(markdown_content)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_txt)

    template_content = template_content.replace('href="/', 'href="' + basepath)
    template_content = template_content.replace('src="/', 'src="' + basepath)

    dest_dir_path = os.path.dirname(dest_path)

    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    to_file = open(dest_path, "w")
    to_file.write(template_content)

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)
