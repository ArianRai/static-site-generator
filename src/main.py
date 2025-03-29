from textnode import TextNode, TextType
from copy_files import copy_files

print("hello world!")


def main():
    my_node = TextNode("This is a test", TextType.LINK, "https://www.boot.dev")
    my_node.__repr__()
    copy_files("./static", "./public")


main()
