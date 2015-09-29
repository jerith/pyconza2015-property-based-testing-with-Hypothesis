from string import ascii_uppercase as uc, ascii_lowercase as lc, digits
from hypothesis import given, strategies as st

st_upperlower = st.sampled_from(zip(uc + digits, lc + digits))

@given(st_upperlower, st.text())
def test_uppercase_transformation(upperlower, text):
    """
    Appending a lowercase character before uppercasing is equivalent to
    appending its uppercase equivalent after uppercasing.
    """
    (upper, lower) = upperlower
    assert text.upper() + upper == (text + lower).upper()
