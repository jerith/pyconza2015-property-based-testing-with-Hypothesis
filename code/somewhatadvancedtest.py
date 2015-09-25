"""
This is a fake module so that our kittens and rainbows example doesn't make
pytest sad.
"""


class VerifyCorrectness(object):
    @classmethod
    def assert_correct(cls):
        pass


def inputs(**kw):
    def noop(func):
        return func
    return noop


number = None
