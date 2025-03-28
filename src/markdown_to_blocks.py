def markdown_to_blocks(markdown):
    lines = markdown.strip().split("\n\n")
    blocks = filter(lambda line: line != "", lines)
    return blocks
