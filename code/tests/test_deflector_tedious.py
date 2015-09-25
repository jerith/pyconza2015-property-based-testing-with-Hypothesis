import unittest
from mycode import Deflector, recalibrate_deflector

class TestMyCode(unittest.TestCase):
    def test_recalibrate_deflector_positive(self):
        deflector = Deflector(1.0)
        recalibrate_deflector(deflector, phase_shift=1.25)
        self.assertEqual(deflector.phase, 2.25)

    def test_recalibrate_deflector_negative(self):
        deflector = Deflector(1.0)
        recalibrate_deflector(deflector, phase_shift=-0.75)
        self.assertEqual(deflector.phase, 0.25)

    def test_recalibrate_deflector_very_negative(self):
        deflector = Deflector(1.0)
        recalibrate_deflector(deflector, phase_shift=-1.75)
        self.assertEqual(deflector.phase, -0.75)
