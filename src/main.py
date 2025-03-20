from textnode import TextNode, TextType

print("hello world!")


def main():
    my_node = TextNode("This is a test", TextType.LINK_TEXT, "https://www.boot.dev")
    my_node.__repr__()


main()
