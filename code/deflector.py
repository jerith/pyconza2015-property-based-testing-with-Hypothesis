class Deflector(object):
    """Important starship component. Powered by narrativium."""

    def __init__(self, phase):
        self.phase = _norm_angle(phase)

    def _shift_phase(self, delta):
        """Mumble mumble technobabble."""
        self.phase = _norm_angle(self.phase + delta)

    # Complete implementation is left as an exercise for the audience.


def recalibrate_deflector(deflector, phase_shift):
    """Manually recalibrate a deflector."""
    deflector._shift_phase(phase_shift)


def _norm_angle(phase):
    """Angles are periodic in the range [-180, 180] degrees."""
    return (phase + 180) % 360 - 180
