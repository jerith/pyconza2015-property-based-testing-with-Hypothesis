from unittest import TestCase
from hypothesis import given, strategies as st
from mycode import Deflector, recalibrate_deflector


class TestDeflectorProperties(TestCase):
    @given(initial_phase=st.floats(), phase_shift=st.floats())
    def test_recalibration(self, initial_phase, phase_shift):
        """Recalibration is actually more complicated than this."""
        deflector = Deflector(initial_phase)
        recalibrate_deflector(deflector, phase_shift)
        self.assertEqual(deflector.phase, initial_phase + phase_shift)

    @given(initial_phase=st.floats())
    def test_phase_inversion(self, initial_phase):
        """Phase inversion is exactly what it says on the tin."""
        deflector = Deflector(initial_phase)
        deflector.trigger_phase_inversion()
        self.assertEqual(deflector.phase, -initial_phase)
