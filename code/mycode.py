"""
Some toy code suitable for demonstrating testing stuff.
"""


def add(a, b):
    return a + b


def query_engine_status(engine):
    return engine.status


class Deflector(object):
    def __init__(self, phase):
        self.phase = phase

    def shift_phase(self, delta):
        # Mumble mumble technobabble
        self.phase += delta

    def trigger_phase_inversion(self):
        # Mumble mumble technobabble
        self.phase = -self.phase


def recalibrate_deflector(deflector, phase_shift):
    deflector.shift_phase(phase_shift)


class Diagnostic(object):
    def run(self):
        return "failed"

    def cleanup(self):
        print "cleaned up"
