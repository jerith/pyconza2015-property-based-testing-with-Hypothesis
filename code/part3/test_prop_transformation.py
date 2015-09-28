from hypothesis import given, strategies as st

@given(st.text())
def test_uppercase_transformation(text):
    """
    Appending a lowercase character before uppercasing is equivalent to
    appending its uppercase equivalent after uppercasing.
    """
    assert text.upper() + 'A' == (text + 'a').upper()
