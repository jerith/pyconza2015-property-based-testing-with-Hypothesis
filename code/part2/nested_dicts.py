from hypothesis.strategies import text, none, dictionaries, recursive

def nest_dict(values):
    return dictionaries(text("abc", max_size=5), values)

nested_dicts = recursive(text("def", max_size=5) | none(), nest_dict)
