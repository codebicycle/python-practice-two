
def matching_parens(text):
    parens = '()[]{}<>'
    matching_parens = [parens[i:i+2] for i in range(0, len(parens), 2)]
    matching = dict(matching_parens)
    closing_parens = set(matching.values())

    stack = []
    for char in text:
        if char in matching:
            stack.append(matching[char])
        elif char in closing_parens:
            if not stack or char != stack.pop():
                return False
    return not stack
