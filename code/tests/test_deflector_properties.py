from unittest import TestCase
from hypothesis import given, strategies as st
from deflector import Deflector, recalibrate_deflector


class TestDeflectorProperties(TestCase):
    @given(initial_phase=st.floats(-1e8, 1e8))
    def test_initial_phase_within_range(self, initial_phase):
        """Phase is always in the range [-180, 180]."""
        assert -180 <= Deflector(initial_phase).phase <= 180

    @given(initial=st.floats(-1e8, 1e8), phase_shift=st.floats(-1e8, 1e8))
    def test_recalibration(self, initial, phase_shift):
        """Recalibration adjusts phase within bounds."""
        deflector = Deflector(initial)
        recalibrate_deflector(deflector, phase_shift)
        assert -180 <= deflector.phase <= 180
        assert approxeq(deflector.phase % 360, (initial + phase_shift) % 360)


def approxeq(a, b, decimals=5):
    return round(a, decimals) == round(b, decimals)
