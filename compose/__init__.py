class NO_INITIAL:
    pass


def compose(initial=NO_INITIAL, *funcs):
    if initial == NO_INITIAL:
        return reduce(simple_compose, funcs, identity)
    else:
        return reduce(simple_compose, funcs, identity)(initial)


def simple_compose(f, g):
    def composed(*args, **kwargs):
        return f(g(*args, **kwargs))
    return composed


def identity(a):
    return a
