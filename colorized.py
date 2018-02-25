import sys

from enum import Enum


__all__ = ['colorized']


class Color(Enum):
    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    ORANGE = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    DARK_GRAY = '\033[1;30m'
    LIGHT_RED = '\033[1;31m'
    LIGHT_GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    LIGHT_BLUE = '\033[1;34m'
    LIGHT_PURPLE = '\033[1;35m'
    LIGHT_CYAN = '\033[1;36m'
    NO_COLOR = '\033[0m'


colors = {
    'black': Color.BLACK,
    'red': Color.RED,
    'green': Color.GREEN,
    'orange': Color.ORANGE,
    'blue': Color.BLUE,
    'purple': Color.PURPLE,
    'cyan': Color.CYAN,
    'dark_gray': Color.DARK_GRAY,
    'light_red': Color.LIGHT_RED,
    'light_green': Color.LIGHT_GREEN,
    'yellow': Color.YELLOW,
    'light_blue': Color.LIGHT_BLUE,
    'light_purple': Color.LIGHT_PURPLE,
    'light_cyan': Color.LIGHT_CYAN,
    'no_color': Color.NO_COLOR,
}


def colorized(color=Color.NO_COLOR):
    def func_wrapper(func):
        def wrapper(*args, **kwargs):
            if sys.platform.startswith('linux'):
                print(colors[color].value, end='')
                result = func(*args, **kwargs)
                print(Color.NO_COLOR.value, end='')
                return result
            else:
                return func(*args, **kwargs)
        return wrapper
    return func_wrapper


if __name__ == '__main__':
    @colorized(color='light_green')
    def kentang(a, b):
        print('hello')
        return a + b

    print(kentang(1, 2))
