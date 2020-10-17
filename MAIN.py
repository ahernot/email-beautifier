import random
import numpy
import subprocess
from colour import Color #pip install colour

import basic_functions as BFunc


__OPERATING_SYSTEM__ = 'macOS'


sample_text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''

_psep_ = '/'
_esep_ = '.'

default_attributes_char = {
        'text_color': '#000000',
        'background_color': '#FFFFFF',
        'style_underlined': False,
        'style_strikethrough': False,
        'style_italicised': False,
        'style_bold': False,
        'font_size': 11,
        'style_font': """'arial black', 'avant garde'"""
    }


beacon_chars_list = ['*']







class Char(object):

    def __init__(self, text:str, **kwargs):
        """
        This class creates a Char object. All unspecified parameters will be chosen at random.
        :param text:
        :param kwargs:
        """

        self.text = text

        #   Text color (CSS)
        if 'text_color' in kwargs:
            self.text_color = kwargs['text_color']
        else:
            self.text_color = BFunc.random_hex_color()


        #   Background color (CSS)
        if 'background_color' in kwargs:
            self.background_color = kwargs['background_color']
        else:
            self.background_color = BFunc.random_hex_color()


        #   Style underlined (CSS)
        if 'style_underlined' in kwargs:
            self.style_underlined = kwargs['style_underlined']
        else:
            self.style_underlined = BFunc.random_bool([0, 0, 0, 0, 1, 1, 1])

        #   Style strikethrough (CSS)
        if 'style_strikethrough' in kwargs:
            self.style_strikethrough = kwargs['style_strikethrough']
        else:
            self.style_strikethrough = BFunc.random_bool([0, 0, 0, 0, 0, 0, 1])

        #   Style italicised (HTML)
        if 'style_italicised' in kwargs:
            self.style_italicised = kwargs['style_italicised']
        else:
            self.style_italicised = BFunc.random_bool([0, 0, 1, 1, 1])

        #   Style bold (HTML)
        if 'style_bold' in kwargs:
            self.style_bold = kwargs['style_bold']
        else:
            self.style_bold = BFunc.random_bool([0, 1, 1])

        #   Font size (CSS)
        if 'font_size' in kwargs:
            self.font_size = kwargs['font_size']
        else:
            self.font_size = BFunc.random_font_size()

        #   Style font (CSS)
        if 'style_font' in kwargs:
            self.style_font = kwargs['style_font']
        else:
            self.style_font = BFunc.random_font()



    def generate_html(self) -> str:

        #   1. Initialising the variables
        html_line = '{other_styles_start}<span style="{style_line}">{text}</span>{other_styles_stop}'
        style_line_list = []

        #   2. Adding the CSS styles
        style_line_list.append('color: {};'.format(self.text_color))  # text color
        style_line_list.append('background-color: {};'.format(self.background_color))  # background color
        if self.style_underlined: style_line_list.append('text-decoration: underline;')  # underlined
        if self.style_strikethrough: style_line_list.append('text-decoration: line-through;')  # struckthrough
        style_line_list.append('font-size: {}pt;'.format(self.font_size))  # font size
        style_line_list.append('font-family: {};')  # font style

        #   3. Adding the HTML styles
        other_styles_list = []
        if self.style_bold: other_styles_list.append('strong')  # bold
        if self.style_italicised: other_styles_list.append('em')  # italicised
        other_styles_start = ''.join(['<{}>'.format(style) for style in other_styles_list])
        other_styles_stop = ''.join(['</{}>'.format(style) for style in other_styles_list])

        #   4. Generating the line
        html_line = html_line.format(**{
            'other_styles_start': other_styles_start,
            'style_line': ' '.join(style_line_list),
            'text': self.text,
            'other_styles_stop': other_styles_stop
        })

        return html_line




class Word(object):

    def __init__(self, text:str, **kwargs):

        self.text = text
        self.char_list = []  # A list of Char objects

        self.stylise()


    def stylise(self):

        def apply_char_style():
            """
            This function chooses the style of each character at random, independently.
            :return:
            """

            for char_str in self.text:
                char_str = char_str.encode('ascii', 'xmlcharrefreplace').decode('utf-8')
                char_obj = Char(char_str)
                self.char_list.append(char_str)

        def apply_word_style():
            """
            This function chooses the general style of the whole word.
            :return:
            """

            #   1. Choosing a general word style, at random
            styles_list = ['size_ramp_up', 'size_ramp_down', 'wave', 'color_gradient']#, 'capitals']
            style = styles_list[random.randint(0, len(styles_list) - 1)]  # choosing at random

            #   1.1. Size ramp up / everything is random apart from size
            if style == 'size_ramp_up':
                word_len = len(self.text)
                sizes_array = numpy.array([i + 9 for i in range(word_len)])

                for char_index, char_str in enumerate(self.text):
                    char_obj = Char(char_str, font_size=sizes_array[char_index])
                    self.char_list.append(char_obj)

            #   1.2. Size ramp down / everything is random apart from size
            elif style == 'size_ramp_down':
                word_len = len(self.text)
                sizes_array = numpy.array([i + 9 for i in range(word_len)][::-1])

                for char_index, char_str in enumerate(self.text):
                    char_obj = Char(char_str, font_size=sizes_array[char_index])
                    self.char_list.append(char_obj)

            #   1.3. Size wave / everything is random apart from size
            elif style == 'wave':
                word_len = len(self.text)
                points_array = numpy.array([i*0.3 for i in range(word_len)][::-1]) # approximately 10/π
                sizes_array = numpy.abs(numpy.sin(points_array))

                for char_index, char_str in enumerate(self.text):
                    char_obj = Char(char_str, font_size=sizes_array[char_index])
                    self.char_list.append(char_obj)

            #   1.4 Color gradient / everything is random apart from text color and text background color
            elif style == 'color_gradient':
                word_len = len(self.text)
                background_color = BFunc.random_hex_color()

                color_start = Color(BFunc.random_hex_color())
                color_stop  = Color(BFunc.random_hex_color())
                colors_array = list(color_start.range_to(color_stop, word_len))

                for char_index, char_str in enumerate(self.text):
                    char_obj = Char(char_str, text_color=colors_array[char_index].get_hex(), background_color=background_color)
                    self.char_list.append(char_obj)

            #   1.5. Resetting to default method (character-wise)
            else:
                apply_char_style()

        self.char_list = []  # A list of Char objects (resetting in case function called several time)

        #   1. Word-level formatting (7% chance)
        if random.randint(0, 99) <= 7: apply_word_style()

        #   2. Character-level formatting (default)
        else: apply_char_style()


    def generate_html(self) -> str:
        html_line_list = []

        for char_obj in self.char_list:

            if char_obj.text in beacon_chars_list:
                html_line_list.append(char_obj.text)
                continue

            html_line_list.append(char_obj.generate_html())

        html_text = '<div>' + ''.join(html_line_list) + '</div>'
        return html_text






class Line(object):

    def __init__(self, text:str, **kwargs):
        self.text = text
        self.word_list = [] # A list of Word objects

        #   Line spacing
        if 'line_spacing' in kwargs:
            self.line_spacing = kwargs['line_spacing']
        else:
            self.line_spacing = numpy.abs(numpy.random.normal(0.7, 0.2, 1)[0])

        #   Text alignment
        if 'text_alignment' in kwargs:
            self.text_alignment = kwargs['text_alignment']
        else:
            self.text_alignment = BFunc.random_from_array(['left', 'left', 'left', 'left', 'left', 'right', 'center', 'justify'])



    def stylise(self):
        """
        This function generates the stylised word objects from the text's 'words'
        :return:
        """

        for word in self.text.split(' '):
            word_obj = Word(word)
            word_obj.stylise()

            self.word_list.append(word_obj)



    def generate_html(self):

        #   1. Initialising the variables
        html_line = '<p style="{line_style}">{line_str}</p>'
        style_line_list = []
        text_list = []

        #   2. Adding the styles
        style_line_list.append('line-height: {};'.format(self.line_spacing))  # line spacing
        style_line_list.append('text-align: {};'.format(self.text_alignment))  # text alignment

        #   3. Adding the processed words
        for word_obj in self.word_list:
            text_list.append(word_obj.generate_html())
            text_list.append(Char(' ').generate_html()) # crude way of adding a processed space (will need to delete the last one)

        #   4. Generating the line
        html_line = html_line.format(**{
            'line_style': ' '.join(style_line_list),
            'line_str': ''.join(text_list[:-1])
        })












def beautify_text(text:str) -> str:
    html_text = ''

    for line in BFunc.split_many(text):
        line_obj = Line(line)
        line_obj.stylise()
        html_text += line_obj.generate_html()

    return html_text


def save(html_text: str, output_path='output.html'):
    with open(output_path, 'w', encoding='utf-8') as html_output:
        html_output.write(html_text)


def convert(input_file_path: str):
    with open(input_file_path, 'r', encoding='utf-8') as txt_input:
        text = txt_input.read()

    html_text = beautify_text(text)

    output_dir = '/'.join(input_file_path.split(_psep_)[:-1]) + '/'
    file_name_full_split = input_file_path.split(_psep_)[-1].split(_esep_)
    file_name = '.'.join(file_name_full_split[:-1])

    output_path = output_dir + file_name + '.html'
    save(html_text, output_path=output_path)
    print(f'File saved at location {output_path}')


    if __OPERATING_SYSTEM__ == 'macOS': # copying to clipboard
        process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
        process.communicate(html_text.encode('utf-8'))

        print('HTML-formatted text successfully copied to clipboard.')



convert('/Users/Anatole/Desktop/t.txt')


# <p style=""><span style="">text</span></p>