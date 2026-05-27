import shutil
import os
import sys

from lib.generator import generate_pages_recursive

def main():
    basepath = ""

    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if os.path.exists("docs/"):
        shutil.rmtree("docs/")

    shutil.copytree("static/", "docs/")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

main()