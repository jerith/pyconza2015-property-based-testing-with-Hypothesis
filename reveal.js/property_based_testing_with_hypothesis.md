## Property-based Testing With Hypothesis

<br/>

#### _Let Your Army of Robots Write Your Tests_

<br/>

<br/>

Jeremy Thurgood

PyconZA 2015

$$$NOTES

I spend a lot of my time writing tests, and I'm not very good at it.
(Measured by bugs that reach production.)

$$$
$$$

## Part 1

<br/>
<br/>
<br/>
<br/>

### What is property-based testing?

$$$NOTES

Demonstrate by example.

$$$

### An example

```python
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

```

$$$NOTES

Some simple code we want to test.

Note that the phase angle is normalised.

Degrees instead of radians to avoid some spiders.

$$$

### How we usually write tests

```python
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

```

$$$NOTES

This is "example-based testing".

A typical unit test suite has lots of little tests that each test one thing.

Ideally, each code path is tested exactly once.

$$$

### Issues with example-based tests

* Tedious to write. <!--{_class="fragment"}-->

* Lots of repetitition. <!--{_class="fragment"}-->

* Painful to maintain. <!--{_class="fragment"}-->

* Focus on low-level details. <!--{_class="fragment"}-->

* ... But infinitely better than no tests at all. <!--{_class="fragment"}-->

$$$NOTES

People are bad at tedious things.

Can't see the forest for the trees.

$$$

### How we want to write tests

<br/>

In a world made of unicorns and kittens and rainbows...

<br/>

```python
import magictest
from deflector import Deflector, recalibrate_deflector

magictest.assert_correct(Deflector)
magictest.assert_correct(recalibrate_deflector)

```
<!-- {_class="fragment"} -->

<br/>

<p class="fragment">...but how does `magictest` know what "correct" is?</p>

$$$NOTES

This is the core of testing: Determining correctness.

$$$

### Maybe without the unicorns

```python
from sufficientlyadvancedtest import VerifyCorrectness, number
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

```

$$$NOTES

We have some methods that test correctness *in general*.

We're only specifying the kind of input, not specific values.

But how does this Sufficiently Advanced Technology work?

$$$

### How property-based tests work

* Properties are assertions about invariants. <!--{_class="fragment"}-->

* Lots of checks with randomly generated input. <!--{_class="fragment"}-->

* Failure case minimisation. <!--{_class="fragment"}-->

* Focus on high-level behaviour. <!--{_class="fragment"}-->

* ... But no silver bullet. <!--{_class="fragment"}-->

$$$NOTES

You like non-deterministic tests, right?

Lots of checks means lots of time.

$$$

### For real, with Hypothesis

```python
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

```

$$$NOTES

This is a real test case that actually runs.

Floating point approximation spiders.


$$$
$$$

## The end of the slides

<br/><br/>

Now you get to ask me hard questions.

<br/>

(Or I can show some more code.)
