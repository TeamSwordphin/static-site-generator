import unittest
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(node, '<a href="https://www.google.com">Click me!</a>')


if __name__ == "__main__":
    unittest.main()