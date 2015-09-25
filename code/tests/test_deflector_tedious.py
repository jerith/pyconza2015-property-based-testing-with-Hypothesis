from unittest import TestCase
from deflector import Deflector, recalibrate_deflector


class TestDeflector(TestCase):
    def test_initial_phase_within_range(self):
        """Phase is always in the range [-180, 180]."""
        assert Deflector(361.0).phase == 1.0
        assert Deflector(-361.0).phase == -1.0
        assert Deflector(179.0).phase == 179.0
        assert Deflector(181.0).phase == -179.0

    def test_recalibrate_deflector_in_bounds(self):
        """Recalibration adjusts phase within bounds."""
        deflector = Deflector(1.0)
        recalibrate_deflector(deflector, phase_shift=1.25)
        assert deflector.phase == 2.25

    def test_recalibrate_deflector_out_of_bounds(self):
        """Recalibrated phase is adjused to be within bounds."""
        deflector = Deflector(95.0)
        recalibrate_deflector(deflector, phase_shift=100.0)
        assert deflector.phase == -165.0
