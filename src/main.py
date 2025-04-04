import os
import shutil
import sys

from textnode import TextNode, TextType
from copy_files import copy_files
from generate_page import generate_pages_recursive

static_path = "./static"
docs_path = "./docs"
content_path = "./content"
template_path = "./template.html"


def main():
    basepath = sys.argv[1]
    if basepath == None:
        basepath = "/"
    if os.path.exists(docs_path):
        shutil.rmtree(docs_path)
    copy_files(static_path, docs_path)
    generate_pages_recursive(content_path, template_path, docs_path, basepath)


main()
