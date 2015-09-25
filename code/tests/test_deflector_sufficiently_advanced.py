from sufficientlyadvancedtest import VerifyCorrectness
from mycode import Deflector, recalibrate_deflector


class VerifyDeflectorCorrectness(VerifyCorrectness):
    def verify_recalibration(self, initial_phase, phase_shift):
        """Recalibration is actually more complicated than this."""
        deflector = Deflector(initial_phase)
        recalibrate_deflector(deflector, phase_shift)
        self.assertEqual(deflector.phase, initial_phase + phase_shift)

    def verify_phase_inversion(self, initial_phase):
        """Phase inversion is exactly what it says on the tin."""
        deflector = Deflector(initial_phase)
        deflector.trigger_phase_inversion()
        self.assertEqual(deflector.phase, -initial_phase)

VerifyDeflectorCorrectness.assert_correct()
