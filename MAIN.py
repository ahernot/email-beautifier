


text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
'''

# Every line starts with "<div>" and ends in "</div>"
# Text color            <span style="color: #993300;">test</span>
# Background color      <span style="background-color: #339966;">test</span>
# Text & Bck color      <span style="color: #993300; background-color: #339966;">test</span>
# Underline             <span style="text-decoration: underline;">test</span>
# Strikethrough         <span style="text-decoration: line-through;">test</span>
# Italicize             <em>test</em>
# Bold                  <strong>test</strong>


# Font size             <span style="font-size: 11pt;">test</span></div>
# Font & size           <span style="font-size: 11pt;"><span style="font-family: 'arial black', 'avant garde';">Anatole</span> Hernot (P20)</span>



'''
random color (bck & txt)
random style
random font
random size
'''


# if multiple same letters then choose between gradient / wave
# color gradient, size gradient


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


class char(object):

    def __init__(self, text:str, **kwargs):

        self.text = text

        #   Text color
        self.text_color = default_attributes['text_color']
        if 'text_color' in kwargs:
            self.text_color = kwargs['text_color']

        #   Background color
        self.background_color = default_attributes['background_color']
        if 'background_color' in kwargs:
            self.background_color = kwargs['background_color']

        #   Style underlined
        self.style_underlined = default_attributes['style_underlined']
        if 'style_underlined' in kwargs:
            self.style_underlined = kwargs['style_underlined']

        #   Style strikethrough
        self.style_strikethrough = default_attributes['style_strikethrough']
        if 'style_strikethrough' in kwargs:
            self.style_strikethrough = kwargs['style_strikethrough']

        #   Style italicised
        self.style_italicised = default_attributes['style_italicised']
        if 'style_italicised' in kwargs:
            self.style_italicised = kwargs['style_italicised']

        #   Style bold
        self.style_bold = default_attributes['style_bold']
        if 'style_bold' in kwargs:
            self.style_bold = kwargs['style_bold']

        #   Font size
        self.font_size = default_attributes['font_size']
        if 'font_size' in kwargs:
            self.font_size = kwargs['font_size']

        #   Style font
        self.style_font = default_attributes['style_font']
        if 'style_font' in kwargs:
            self.style_font = kwargs['style_font']





    def generate_html(self) -> str:

        #   1. Initialising the variables
        html_line = '{other_styles_start}<span style="{style_line}">{text}</span>{other_styles_stop}'
        style_line_list = []

        #   2. Adding the CSS styles
        style_line_list.append('color: {};'.format(self.text_color))
        style_line_list.append('background-color: {};'.format(self.background_color))
        if self.style_underlined: style_line_list.append('text-decoration: underline;')
        if self.style_strikethrough: style_line_list.append('text-decoration: line-through;')
        style_line_list.append('font-size: {}pt;'.format(self.font_size))
        style_line_list.append('font-family: {};')

        #   3. Adding the HTML styles
        other_styles_list = []
        if self.style_bold: other_styles_list.append('strong')
        if self.style_italicised: other_styles_list.append('em')
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


X = char('text', style_bold=True)
print(X.generate_html())






