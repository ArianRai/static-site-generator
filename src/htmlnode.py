class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        props_text = ""
        if self.props is None:
            return props_text
        for key, value in self.props.items():
            props_text += f' {key}="{value}"'
        return " ".join(props_text)

    def __repr__(self):
        children = ", ".join(self.children)
        props_text = self.props_to_html()
        print(
            f"tag = {self.tag} value = {self.value} children = {children} props = {props_text}"
        )
