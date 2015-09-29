from hypothesis.strategies import integers, text, lists

def text_line(size):
    return text("1234567890", min_size=size, max_size=size)

def square_lines(size):
    return lists(text_line(size), min_size=size, max_size=size)

square_text = integers(1, 5).flatmap(square_lines).map("\n".join)
