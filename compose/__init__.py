def compose(*funcs):
    return reduce(simple_compose, funcs, identity)


def simple_compose(f, g):
    def composed(*args, **kwargs):
        return f(g(*args, **kwargs))
    return composed


def identity(a):
    return a
