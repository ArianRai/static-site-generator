from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        print(f"TextNode({self.text}, {self.text_type.value}, {self.url})")


def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Text type not valid")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, "Just a text value")
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", "Just a text value")
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", "Just a text value")
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", "Just a text value")
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", "Just a text value", {"href": "https://boot.dev"})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": "https://boot.dev", "alt": "image"})
