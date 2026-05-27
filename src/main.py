import shutil
import os
from lib.generator import generate_pages_recursive

def main():
    if os.path.exists("public/"):
        shutil.rmtree("public/")

    shutil.copytree("static/", "public/")
    generate_pages_recursive("./content", "./template.html", "./public")

main()