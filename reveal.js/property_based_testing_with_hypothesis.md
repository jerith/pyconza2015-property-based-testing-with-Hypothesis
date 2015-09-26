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
from magic import assert_correct
from deflector import Deflector, recalibrate_deflector

assert_correct(Deflector)
assert_correct(recalibrate_deflector)

```
<!-- {_class="fragment"} -->

<br/>

<p class="fragment">...but how does `assert_correct` know what's correct?</p>

$$$NOTES

This is the core of testing: Determining correctness.

$$$

### Maybe without the unicorns

```python
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

```

$$$NOTES

We have some methods that test correctness *in general*.

Although these reimplement too much of the code under test.

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

## Part 2

<br/>
<br/>
<br/>
<br/>

### Hypothesis

$$$NOTES

$$$

### Writing tests

```python
from hypothesis import given, strategies as st


@given(st.integers())
def test_addition_identity(x):
    assert x + 0 == x


@given(st.integers(), st.integers())
def test_addition_commutative(x, y):
    assert x + y == y + x


@given(st.integers(), st.integers(), st.integers())
def test_addition_associative(x, y, z):
    assert (x + y) + z == x + (y + z)

```

$$$NOTES

Other tools call them generators.

.example() generates a random example.

Useful for more than just tests.

$$$

### Built-in Strategies

```python
>>> from hypothesis import strategies

>>> text = strategies.text()
>>> text.example()
u''
>>> text.example()
u'm<\x7f&\x02\u0393\r`\x8d<&\x1c\u0393mm\r\x1c\x18\x0c\x02\xa5'

>>> abctext = strategies.text(alphabet="abc")
>>> abctext.example()
u'cacaccccacaaacc'
>>> abctext.example()
u'aaaaaaaabaacabaaacaaaaaabaaaaac'

>>> lists_of_ints = strategies.lists(strategies.integers(-1000, 1000))
>>> lists_of_ints.example()
[-947, 873, -947, -37, 936, 936, 936]
>>> lists_of_ints.example()
[-805, 855, 674, -236, 447, 775, -168, -909, -512, 220, 994, 278, -803, -901]
>>> lists_of_ints.example()
[-75, 487, -468]

```

$$$NOTES

Other tools call them generators.

.example() generates a random example.

Useful for more than just tests.

$$$

### Adapting strategies: filter

```python
>>> even_lists = lists(integers(0, 100)).filter(lambda l: len(l) % 2 == 0)
>>> even_lists.example()
[52, 42]
>>> even_lists.example()
[71, 34, 79, 50, 80, 56, 64, 34]
>>> even_lists.example()
[]

```

$$$NOTES

$$$

### Adapting strategies: map

```python
>>> even_integers = strategies.integers().filter(lambda x: x % 2 == 0)
>>> even_integers.example()
-54
>>> even_integers.example()
0
>>> even_integers.example()
-110212872381391885439645758881510120016L


```

```python
>>> even_integers = strategies.integers().map(lambda x: x * 2)
>>> even_integers.example()
6
>>> even_integers.example()
-52
>>> even_integers.example()
-621603898346041721844744845583782563802L

```

$$$NOTES

Other tools call them generators.

.example() generates a random example.

Useful for more than just tests.

$$$


$$$
$$$

## The end of the slides

<br/><br/>

Now you get to ask me hard questions.

<br/>

(Or I can show some more code.)
