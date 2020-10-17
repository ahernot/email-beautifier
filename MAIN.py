import random


"""
TO DO
- Add more fonts
"""


text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''



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


class Char(object):

    def __init__(self, text:str, **kwargs):

        self.text = text

        #   Text color (CSS)
        self.text_color = default_attributes['text_color']
        if 'text_color' in kwargs:
            self.text_color = kwargs['text_color']

        #   Background color (CSS)
        self.background_color = default_attributes['background_color']
        if 'background_color' in kwargs:
            self.background_color = kwargs['background_color']

        #   Style underlined (CSS)
        self.style_underlined = default_attributes['style_underlined']
        if 'style_underlined' in kwargs:
            self.style_underlined = kwargs['style_underlined']

        #   Style strikethrough (CSS)
        self.style_strikethrough = default_attributes['style_strikethrough']
        if 'style_strikethrough' in kwargs:
            self.style_strikethrough = kwargs['style_strikethrough']

        #   Style italicised (HTML)
        self.style_italicised = default_attributes['style_italicised']
        if 'style_italicised' in kwargs:
            self.style_italicised = kwargs['style_italicised']

        #   Style bold (HTML)
        self.style_bold = default_attributes['style_bold']
        if 'style_bold' in kwargs:
            self.style_bold = kwargs['style_bold']

        #   Font size (CSS)
        self.font_size = default_attributes['font_size']
        if 'font_size' in kwargs:
            self.font_size = kwargs['font_size']

        #   Style font (CSS)
        self.style_font = default_attributes['style_font']
        if 'style_font' in kwargs:
            self.style_font = kwargs['style_font']





    def generate_html(self) -> str:

        #   1. Initialising the variables
        html_line = '{other_styles_start}<span style="{style_line}">{text}</span>{other_styles_stop}'
        style_line_list = []

        #   2. Adding the CSS styles
        style_line_list.append('color: {};'.format(self.text_color)) # text color
        style_line_list.append('background-color: {};'.format(self.background_color)) # background color
        if self.style_underlined: style_line_list.append('text-decoration: underline;') # underlined
        if self.style_strikethrough: style_line_list.append('text-decoration: line-through;') # struckthrough
        style_line_list.append('font-size: {}pt;'.format(self.font_size)) # font size
        style_line_list.append('font-family: {};') # font style

        #   3. Adding the HTML styles
        other_styles_list = []
        if self.style_bold: other_styles_list.append('strong') # bold
        if self.style_italicised: other_styles_list.append('em') # italicised
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






def random_style_char(text:str) -> Char:
    #   Text color (CSS)
    text_color_int = random.randint(0, 16777215)
    text_color_hex = '#' + str(hex(text_color_int))[2:]

    #   Background color (CSS)
    background_color_int = random.randint(0, 16777215)
    background_color_hex = '#' + str(hex(background_color_int))[2:]

    #   Style underlined (CSS)
    style_underlined = bool(random.randint(0, 1))

    #   Style strikethrough (CSS)
    style_strikethrough = bool(random.randint(0, 1))

    #   Style italicised (HTML)
    style_italicised = bool(random.randint(0, 1))

    #   Style bold (HTML)
    style_bold = bool(random.randint(0, 1))

    #   Font size (CSS)
    font_size = random.randint(6, 250)

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
            html_line_list.append(random_style_char(char).generate_html())
        html_text += '<div>' + ''.join(html_line_list) + '</div>'

    return html_text



print(beautify_text(text))



