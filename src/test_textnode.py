import unittest
from textnode import TextNode, TextType
from split_node_delimiter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_urlnone(self):
        node = TextNode("This is a text node with URL none", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_text_img(self):
        node = TextNode("This is a img node", TextType.IMAGE, "https://boots.dev/")
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "https://boots.dev/", "alt": "This is a img node"})

    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.PLAIN),
        ])

        node_2 = TextNode("This is text with a **code block** word", TextType.PLAIN)
        new_nodes_2 = split_nodes_delimiter([node_2], "**", TextType.BOLD)
        self.assertEqual(new_nodes_2, [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("code block", TextType.BOLD),
            TextNode(" word", TextType.PLAIN),
        ])

if __name__ == "__main__":
    unittest.main()