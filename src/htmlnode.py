class HTMLNode():
    def __init__(self, tag: str=None, value: str=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Error")
    
    def props_to_html(self):
        formatted = ""

        if self.props is not None:
            for key in self.props:
                formatted = f'{formatted} {key}="{self.props[key]}"'
        
        return formatted
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("No value!")
        
        if self.tag is None:
            return self.value
        
        return f'<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("No value!")
        
        if self.children is None:
            raise ValueError("No children!")
        
        result = ""

        for leaf in self.children:
            result = f"{result}{leaf.to_html()}"
        
        return f'<{self.tag}{super().props_to_html()}>{result}</{self.tag}>'
    
