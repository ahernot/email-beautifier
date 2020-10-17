import random
import numpy
import subprocess


__OPERATING_SYSTEM__ = 'macOS'


sample_text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''

_psep_ = '/'
_esep_ = '.'



beacon_chars_list = ['*']


class Char(object):

    default_attributes = {
        'text_color': '#000000',
        'background_color': '#FFFFFF',
        'style_underlined': False,
        'style_strikethrough': False,
        'style_italicised': False,
        'style_bold': False,
        'font_size': 11,
        'style_font': """'arial black', 'avant garde'"""
    }

    def __init__(self, text:str, **kwargs):

        self.text = text

        #   Text color (CSS)
        self.text_color = default_attributes_char['text_color']
        if 'text_color' in kwargs:
            self.text_color = kwargs['text_color']

        #   Background color (CSS)
        self.background_color = default_attributes_char['background_color']
        if 'background_color' in kwargs:
            self.background_color = kwargs['background_color']

        #   Style underlined (CSS)
        self.style_underlined = default_attributes_char['style_underlined']
        if 'style_underlined' in kwargs:
            self.style_underlined = kwargs['style_underlined']

        #   Style strikethrough (CSS)
        self.style_strikethrough = default_attributes_char['style_strikethrough']
        if 'style_strikethrough' in kwargs:
            self.style_strikethrough = kwargs['style_strikethrough']

        #   Style italicised (HTML)
        self.style_italicised = default_attributes_char['style_italicised']
        if 'style_italicised' in kwargs:
            self.style_italicised = kwargs['style_italicised']

        #   Style bold (HTML)
        self.style_bold = default_attributes_char['style_bold']
        if 'style_bold' in kwargs:
            self.style_bold = kwargs['style_bold']

        #   Font size (CSS)
        self.font_size = default_attributes_char['font_size']
        if 'font_size' in kwargs:
            self.font_size = kwargs['font_size']

        #   Style font (CSS)
        self.style_font = default_attributes_char['style_font']
        if 'style_font' in kwargs:
            self.style_font = kwargs['style_font']

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

            # not the same as a char: all attributes are determined randomly


        def stylise(self):

            pass

            # will either single out characters or choose gradients etc


        def generate_html(self) -> str:
            pass





    class Line(object):

        def __init__(self, text:str, **kwargs):

            self.text = text

            self.height = 0.7







"""
CHARACTER: span style="vertical-align: 5.0px;"
WORD-WISE: span style="letter-spacing: -0.7px;"
LINE-WISE: line-height: 0.7
LINE-WISE: text-align: right/center/left/justify
"""


def random_style_char(text:str) -> Char:
    #   Text color (CSS)
    text_color_int = random.randint(0, 16777215)
    text_color_hex = '#' + str(hex(text_color_int))[2:]

    #   Background color (CSS)
    background_color_int = random.randint(0, 16777215)
    background_color_hex = '#' + str(hex(background_color_int))[2:]

    #   Style underlined (CSS)
    style_underlined_spread = [0, 0, 0, 0, 1, 1, 1]
    style_underlined = bool(style_underlined_spread[random.randint(0, len(style_underlined_spread) - 1)]) #style_underlined = bool(random.randint(0, 1))


    #   Style strikethrough (CSS)
    style_strikethrough_spread = [0, 0, 0, 0, 0, 0, 1]
    style_strikethrough = bool(style_strikethrough_spread[random.randint(0, len(style_strikethrough_spread) - 1)]) #style_strikethrough = bool(random.randint(0, 1))

    #   Style italicised (HTML)
    style_italicised_spread = [0, 0, 1, 1, 1]
    style_italicised = bool(style_italicised_spread[random.randint(0, len(style_italicised_spread) - 1)]) #style_italicised = bool(random.randint(0, 1))

    #   Style bold (HTML)
    style_bold_spread = [0, 1, 1]
    style_bold = bool(style_bold_spread[random.randint(0, len(style_bold_spread) - 1)]) #style_bold = bool(random.randint(0, 1))

    #   Font size (CSS)
    font_size = numpy.abs(numpy.random.normal(50, 20, 1)[0]) #font_size = random.randint(6, 250)

    #   Style font (CSS)
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


    text_char = Char(
        text = text,
        text_color = text_color_hex,
        background_color = background_color_hex,
        style_underlined = style_underlined,
        style_strikethrough = style_strikethrough,
        style_italicised = style_italicised,
        style_bold = style_bold,
        font_size = font_size,
        style_font = style_font
    )


    return text_char






def beautify_text(text:str) -> str:
    html_text = ''

    for line in text.split('\n'):#TO BETTER
        html_line_list = []

        for char in line:

            if char in beacon_chars_list:
                html_line_list.append(char)
                continue

            char = char.encode('ascii', 'xmlcharrefreplace').decode('utf-8')

            html_line_list.append(random_style_char(char).generate_html())
        html_text += '<div>' + ''.join(html_line_list) + '</div>'

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