import json
from hypothesis import given, strategies as st
import myjson

def nest_data(st_values):
    return st.lists(st_values) | st.dictionaries(st.text(), st_values)

def nested_data():
    return st.none() | st.integers() | st.floats(-1e308, 1e308) | st.text()

@given(st.recursive(nested_data(), nest_data).map(json.dumps))
def test_json_oracle(json_text):
    """
    The new thing behaves the same as the old thing.
    """
    assert json.loads(json_text) == myjson.loads(json_text)
