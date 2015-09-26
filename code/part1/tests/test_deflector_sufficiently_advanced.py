from sufficientlyadvancedtechnology import VerifyCorrectness, number
from deflector import Deflector, recalibrate_deflector


class VerifyDeflectorCorrectness(VerifyCorrectness):
    def verify_initial_phase_within_range(self, initial_phase=number):
        """Phase is always in the range [-180, 180]."""
        assert -180 <= Deflector(initial_phase).phase <= 180

    def verify_recalibration(self, initial_phase=number, phase_shift=number):
        """Recalibration adjusts phase within bounds."""
        deflector = Deflector(initial_phase)
        recalibrate_deflector(deflector, phase_shift)
        assert -180 <= deflector.phase <= 180
        assert deflector.phase % 360 == (initial_phase + phase_shift) % 360

VerifyDeflectorCorrectness.assert_correct()
