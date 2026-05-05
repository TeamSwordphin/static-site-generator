import unittest
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("p", "I'm a paragraph text!", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()