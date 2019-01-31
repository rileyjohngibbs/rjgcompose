def compose(*funcs, **kwargs):
    """Composes an arbitrary list of functions."""
    if "initial" not in kwargs:
        return reduce(simple_compose, funcs, identity)
    else:
        return reduce(simple_compose, funcs, identity)(kwargs["initial"])


def simple_compose(f, g):
    """Composes two functions"""
    def composed(*args, **kwargs):
        return f(g(*args, **kwargs))
    return composed


def identity(a):
    return a
