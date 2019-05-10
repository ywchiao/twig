class logger(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, type=None):
        return self.__class__(self.func.__get__(obj, type))

    def __call__(self, *args, **kw):
        print ('Entering %s' % self.func)
        print (f"{self.func.__class__}")
        print (f"{dir(self.func)}")
        print (f"{self.func.__str__}")
        print (f"{dir(self.func.__func__)}")
        print (f"{self.func.__func__.__qualname__}")
        print (f"{self.func.__qualname__}")

        return self.func(*args, **kw)

class C(object):
    @logger
    def f(self, x, y):
        return x+y

print(C().f(1, 2))
