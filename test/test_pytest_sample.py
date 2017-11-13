import time


class TestClass(object):
    def test_one(self):
        time.sleep(10)
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
