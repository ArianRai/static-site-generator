from textnode import TextNode, TextType

print("hello world!")


def main():
    my_node = TextNode("This is a test", TextType.LINK, "https://www.boot.dev")
    my_node.__repr__()


main()
