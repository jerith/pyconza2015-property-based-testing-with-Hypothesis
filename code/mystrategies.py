from hypothesis.strategies import floats


def isfinite(f):
    return float('-inf') < f < float('inf')


def finitefloats(*args, **kw):
    return floats(*args, **kw).filter(isfinite)
