import numpy
import random

line_breaks_list = ['\n'] ## ADD MORE


def split_many(text:str, split_list:list=line_breaks_list) -> list:
    """
    This function splits a string along multiple different split points (default are line breaks). It is case-sensitive.
    :param text: The text to split
    :param split_list: The splitting beacons
    :return: A list of the split text.
    """
    split_separator = '__sep__'
    for separator in split_list:
        while separator in text:
            text = text.replace(separator, split_separator)
    return text.split(split_separator)


def random_hex_color() -> str:
    color_int = random.randint(0, 16777215)
    color_hex = '#' + str(hex(color_int))[2:]
    return color_hex

def random_bool(ponderation_array:list=[0, 1]) -> bool:
    random_bool = bool(ponderation_array[random.randint(0, len(ponderation_array) - 1)])
    return random_bool

def random_from_array(ponderation_array:list) -> str or int or float:
    return ponderation_array[random.randint(0, len(ponderation_array) - 1)]

def random_font_size():
    font_size = numpy.abs(numpy.random.normal(50, 20, 1)[0])
    return font_size

def random_font():
    fonts = ['',
             """"'arial, helvetica, sans-serif'""",
             """"'times new roman', 'new york', times, serif""",
             """'arial black', 'avant garde'""",
             """'courier new', courier, monaco, monospace, sans-serif""",
             """'comic sans ms', 'comic sans', sans-serif""",
             """'lucida console', sans-serif""",
             """garamond, 'new york', times, serif""",
             """georgia, serif""",
             """tahoma, 'new york', times, serif""",
             """terminal, monaco""",
             """'trebuchet ms', sans-serif""",
             """verdana, helvetica, sans-serif"""
    ]
    style_font = fonts[random.randint(0, len(fonts) - 1)]