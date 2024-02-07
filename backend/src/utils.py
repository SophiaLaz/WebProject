import os


def get_name(filename):
    return os.path.splitext(os.path.basename(filename))[0]


def convert_name_to_color(name: str):
    code = hash(name)
    r, g, b = code % 256, code // 12 % 256, (code + 1727) // 27 % 256
    return f'rgb({r}, {g}, {b})'


