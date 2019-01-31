def compose(*funcs, **kwargs):
    if "initial" not in kwargs:
        return reduce(simple_compose, funcs, identity)
    else:
        return reduce(simple_compose, funcs, identity)(kwargs["initial"])


def simple_compose(f, g):
    def composed(*args, **kwargs):
        return f(g(*args, **kwargs))
    return composed


def identity(a):
    return a
