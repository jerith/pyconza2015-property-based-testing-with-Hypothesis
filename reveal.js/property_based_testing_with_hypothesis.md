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

### How we usually write tests

<br/>

```python
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

```

$$$NOTES

A typical unit test suite has lots of little tests that each test one thing.

This is good, but tedious to write. People are bad at tedious things.

Focus on low-level things.

$$$

### How we want to write tests

<br/>

In a world made of unicorns and kittens and rainbows...

<br/>

```python
import magictest
from mycode import Deflector, recalibrate_deflector

magictest.assert_correct(Deflector)
magictest.assert_correct(recalibrate_deflector)

```
<!-- {_class="fragment"} -->

<br/>

<span class="fragment">
...but how does `magictest` determine *correctness*?
</span>

$$$NOTES

This is the core of testing: Determining correctness.


$$$

### Maybe without the unicorns

<br/>

```python
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

```

$$$NOTES

We have some methods that test correctness *in general*.

But we still need Sufficiently Advanced Technology to use them.


$$$

### A little less magic, perhaps

```python
from somewhatadvancedtest import VerifyCorrectness, inputs, number
from mycode import Deflector, recalibrate_deflector


class VerifyDeflectorCorrectness(VerifyCorrectness):
    @inputs(initial_phase=number, phase_shift=number)
    def verify_recalibration(self, initial_phase, phase_shift):
        """Recalibration is actually more complicated than this."""
        deflector = Deflector(initial_phase)
        recalibrate_deflector(deflector, phase_shift)
        self.assertEqual(deflector.phase, initial_phase + phase_shift)

    @inputs(initial_phase=number)
    def verify_phase_inversion(self, initial_phase):
        """Phase inversion is exactly what it says on the tin."""
        deflector = Deflector(initial_phase)
        deflector.trigger_phase_inversion()
        self.assertEqual(deflector.phase, -initial_phase)

VerifyDeflectorCorrectness.assert_correct()

```

$$$NOTES

This is now something we can realistically implement.

We're only specifying the kind of input, not specific values.


$$$

### For real, with Hypothesis

```python
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

```

$$$NOTES

This is a real test case that actually runs.

It doesn't pass, though, because float spiders.

$$$
$$$

## The end of the slides

<br/><br/>

Now you get to ask me hard questions.

<br/>

(Or I can show some more code.)
