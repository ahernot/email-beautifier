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
    """
    This function generates a random hexadecimal color value.
    :return: The random hexadecimal color value
    """
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())

def random_bool(ponderation_array:list=[0, 1]) -> bool:
    """
    This function generates a random boolean based on a ponderation array (0 = False, 1 = True).
    :param ponderation_array: The ponderation array to use for the boolean generation
    :return: The random boolean
    """
    random_bool = bool(ponderation_array[random.randint(0, len(ponderation_array) - 1)])
    return random_bool

def random_from_array(ponderation_array:list) -> str or int or float:
    """
    This function chooses a random element from a list.
    :param ponderation_array: The list to choose the random element from
    :return: The random element from the list
    """
    return ponderation_array[random.randint(0, len(ponderation_array) - 1)]

def random_font_size() -> int:
    """
    This function generates a random font size using a normal probabilistic model.
    :return: The random font size
    """
    font_size = int(numpy.abs(numpy.random.normal(45, 20, 1)[0]) + 8)
    return font_size

def random_font() -> str:
    """
    This function picks a random font from the list of available fonts.
    :return: The random font's name
    """
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
    return random_from_array(fonts)