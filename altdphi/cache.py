# Tai Sakuma <tai.sakuma@gmail.com>

##__________________________________________________________________||
# https://stackoverflow.com/questions/4037481/caching-attributes-of-classes-in-python#answer-4037979
class cache_once_property(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, instance, owner):
        val = self.f(instance)
        setattr(instance, self.f.__name__, val)
        return val

##__________________________________________________________________||
