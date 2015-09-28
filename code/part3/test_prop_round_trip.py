from hypothesis import given, strategies as st
import json

def nest_data(st_values):
    return st.lists(st_values) | st.dictionaries(st.text(), st_values)

def nested_data():
    return st.none() | st.integers() | st.floats(-1e308, 1e308) | st.text()


@given(st.recursive(nested_data(), nest_data))
def test_json_round_trip(data):
    """
    Encoding a thing as JSON and decoding it again returns the same thing.

    (This will fail for input that contains tuples, but we don't test that.)
    """
    assert data == json.loads(json.dumps(data))
