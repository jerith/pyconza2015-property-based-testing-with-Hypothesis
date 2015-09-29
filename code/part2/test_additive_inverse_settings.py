from hypothesis import given, Settings, Verbosity, strategies as st

with Settings(max_examples=5, verbosity=Verbosity.verbose):
    @given(st.integers(-10, 10))
    def test_additive_inverse(x):
        """Double additive inverse has no effect."""
        assert x == -(-x)

if __name__ == "__main__":
    test_additive_inverse()
