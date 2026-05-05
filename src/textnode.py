from enum import Enum 
from htmlnode import LeafNode

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text: str, text_type: TextType=TextType.PLAIN, url: str=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def to_html_node(self): # convert to HTML node
        match self.text_type:
            case TextType.PLAIN:
                return LeafNode(None, self.text)
            case TextType.BOLD:
                return LeafNode("b", self.text)
            case TextType.ITALIC:
                return LeafNode("i", self.text)
            case TextType.CODE:
                return LeafNode("code", self.text)
            case TextType.LINK:
                return LeafNode("a", self.text, {"href": self.url})
            case TextType.IMAGE:
                return LeafNode("img", None, {"src": self.url, "alt": self.text})
            case _:
                raise Exception(f"{self.text_type} not found!")

    def __eq__(self, other):
        return (self.text == other.text and self.text_type == other.text_type and self.url == other.url) 

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"