
class B:
    def __init__(self, fn):
        self._func = fn

    def __call__(self):
        print("self")
        self._func(self)


class A:
    def __init__(self):
        self._test = "this"
        pass

    @B
    def foo(self):
        print(f"hhi {self._test}")

a = A()
a.foo()

print("this is a test")

