from functools import wraps
from structlog.stdlib import BoundLoggerBase
import inspect
from inspect import Signature


def test(x, y, z):
    frame = inspect.currentframe()
    name = inspect.getframeinfo(frame)[2]
    context = inspect.getframeinfo(frame)[3]
    print(inspect.getargvalues(frame)[0])
    print(inspect.getframeinfo(frame))
    print('METHOND NAME: ' + inspect.getframeinfo(frame)[2])
    print('LINE #: ' + str(inspect.getframeinfo(frame)[1]))
    print(f'name={name}, context={context}')
    class x():
        def __init__(self, y, z):
            self.z = z
            self.y = y
    print(inspect.getmembers(x(1, 2)))


def log_enter(func):
    import inspect

    @wraps(func)
    def with_logging(*args, **kwargs):
        titles = inspect.getargvalues(inspect.currentframe())[0]
        print(titles)
        print(f'DICT: {func.__dict__}')
        print(f'ENTERING:{func.__name__} args=[{args}] kwargs=[{kwargs}]')
        return func(*args, **kwargs)

    return with_logging

@log_enter
def test2(x, y, z=None):
    print(f'INSIDE x={x}, y={y}, z={z}')


if __name__ == '__main__':
    print(test2(1, 2, 3))
