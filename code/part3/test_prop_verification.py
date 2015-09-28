from hypothesis import given, strategies as st

@given(st.text("abcd \t\r\n"))
def test_no_tabs_after_expandtabs(text):
    """
    Expanding tabs replaces all tab characters.
    """
    assert "\t" not in text.expandtabs()
