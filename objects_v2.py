import random
import numpy
from colour import Color  # pip install colour

import basic_functions as BFunc

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

        #   Vertical alignment
        if 'vertical_alignment' in kwargs:
            self.vertical_alignment = kwargs['vertical_alignment']
        else:
            self.vertical_alignment = numpy.random.normal(0, 1.5, 1)[0]

    def generate_html(self) -> str:
        """
        This function generates the HTML-formatted stylised character contained in the Char object.
        :return: The HTML-formatted character string
        """

        ## print(self.text, self.font_size, self.text_color) ##

        #   1. Initialising the variables
        html_line = '{other_styles_start}<span style="{style_line}">{text}</span>{other_styles_stop}'
        style_line_list = []

        #   2. Adding the CSS styles
        style_line_list.append('color: {};'.format(self.text_color))  # text color
        style_line_list.append('background-color: {};'.format(self.background_color))  # background color
        if self.style_underlined: style_line_list.append('text-decoration: underline;')  # underlined
        if self.style_strikethrough: style_line_list.append('text-decoration: line-through;')  # struckthrough
        style_line_list.append('font-size: {}pt;'.format(self.font_size))  # font size
        style_line_list.append('font-family: {};'.format(self.style_font))  # font style
        style_line_list.append('vertical-align: {}px;'.format(self.vertical_alignment))  # vertical alignment

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
        """
        This class creates a Word object. All unspecified parameters will be chosen at random.
        :param text: The word
        :param kwargs: The parameters to stylise the word
        """

        self.text = text
        self.char_list = []  # a list of Char objects

        #   Character spacing
        if 'character_spacing' in kwargs:
            self.character_spacing = kwargs['character_spacing']
        else:
            self.character_spacing = numpy.random.normal(0.1, 0.4, 1)[0]  # (0, 0.7, 1)[0]

        #   Stylising
        self.stylise()

    def stylise(self):
        """
        This function generates the stylised Char objects from the text's characters, word- or character- wise.
        This function is automatically called when initialising the class.
        :return:
        """

        def apply_char_style():
            """
            This function chooses the style of each character at random, independently.
            :return:
            """

            for char_str in self.text:
                char_str = char_str.encode('ascii', 'xmlcharrefreplace').decode('utf-8')
                char_obj = Char(char_str)
                self.char_list.append(char_obj)

        def apply_word_style():
            """
            This function chooses the general style of the whole word.
            :return:
            """

            #   1. Choosing a general word style, at random
            style = BFunc.random_from_array(['size_ramp_up', 'size_ramp_down', 'wave', 'color_gradient'])

            #   2.1. Size ramp up / everything is random apart from size
            if style == 'size_ramp_up':
                sizes_array = numpy.array([5*i + 9 for i in range(word_len)])

                style_font = BFunc.random_font()  # fixing the font

                for char_index, char_str in enumerate(self.text):
                    char_str = char_str.encode('ascii', 'xmlcharrefreplace').decode('utf-8')
                    char_obj = Char(char_str, font_size=sizes_array[char_index], style_font=style_font)
                    self.char_list.append(char_obj)

            #   2.2. Size ramp down / everything is random apart from size
            elif style == 'size_ramp_down':
                sizes_array = numpy.array([5*i + 9 for i in range(word_len)][::-1])

                style_font = BFunc.random_font()  # fixing the font

                for char_index, char_str in enumerate(self.text):
                    char_str = char_str.encode('ascii', 'xmlcharrefreplace').decode('utf-8')
                    char_obj = Char(char_str, font_size=sizes_array[char_index], style_font=style_font)
                    self.char_list.append(char_obj)

            #   2.3. Size wave / everything is random apart from size
            elif style == 'wave':
                points_array = numpy.array([i*0.15 for i in range(word_len)][::-1])
                sizes_array = (numpy.abs(numpy.sin(points_array)) * 10) ** 2

                style_font = BFunc.random_font()  # fixing the font

                for char_index, char_str in enumerate(self.text):
                    char_str = char_str.encode('ascii', 'xmlcharrefreplace').decode('utf-8')
                    char_obj = Char(char_str, font_size=sizes_array[char_index], style_font=style_font)
                    self.char_list.append(char_obj)

            #   2.4 Color gradient / everything is random apart from text color and text background color
            elif style == 'color_gradient':
                background_color = BFunc.random_hex_color()

                color_start = Color(BFunc.random_hex_color())
                color_stop  = Color(BFunc.random_hex_color())
                colors_array = list(color_start.range_to(color_stop, word_len))

                for char_index, char_str in enumerate(self.text):
                    char_str = char_str.encode('ascii', 'xmlcharrefreplace').decode('utf-8')
                    char_obj = Char(char_str, text_color=colors_array[char_index].get_hex(), background_color=background_color)
                    self.char_list.append(char_obj)

            #   3. Resetting to default method (character-wise)
            else:
                apply_char_style()

        word_len = len(self.text)
        self.char_list = []  # A list of Char objects (resetting in case function called several time)

        #   1. Word-level formatting (chance depends on word length, ≥7%)
        if (random.randint(0, 99) - (word_len * 2)) <= 7: apply_word_style()

        #   2. Character-level formatting (default)
        else: apply_char_style()

    def generate_html(self) -> str:
        """
        This function generates the HTML-formatted stylised word contained in the Word object.
        :return: The HTML-formatted word string
        """

        #   1. Initialising the variables
        html_line = '<span style="{word_style}">{word_str}</span>'
        style_word_list = []
        text_list = []

        #   2. Adding the styles
        style_word_list.append('letter-spacing: {}px;'.format(self.character_spacing))  # character spacing

        #   3. Adding the processed words
        for char_obj in self.char_list:

            if char_obj.text in beacon_chars_list:
                text_list.append(char_obj.text)
                continue

            text_list.append(char_obj.generate_html())

        #   4. Generating the line
        html_line = html_line.format(**{
            'word_style': ' '.join(style_word_list),
            'word_str': ''.join(text_list)
        })

        return html_line





class Line(object):

    def __init__(self, text:str, **kwargs):
        """
        This class creates a Line object. All unspecified parameters will be chosen at random.
        :param text: The line
        :param kwargs: The parameters to stylise the line
        """

        self.text = text
        self.word_list = []  # a list of Word objects

        #   Line spacing
        if 'line_spacing' in kwargs:
            self.line_spacing = kwargs['line_spacing']
        else:
            self.line_spacing = numpy.abs(numpy.random.normal(1.0, 0.125, 1)[0])  # (0.7, 0.2, 1)[0])

        #   Text alignment
        if 'text_alignment' in kwargs:
            self.text_alignment = kwargs['text_alignment']
        else:
            self.text_alignment = BFunc.random_from_array(['left', 'left', 'left', 'left', 'left', 'right', 'center', 'justify'])

        #   Stylising
        self.stylise()

    def stylise(self):
        """
        This function generates the stylised word objects from the text's 'words'.
        This function is automatically called when initialising the class.
        :return:
        """

        self.word_list = []  # A list of Word objects (resetting in case function called several time)

        for word in self.text.split(' '):
            if not word: continue

            word_obj = Word(word)
            self.word_list.append(word_obj)


    def generate_html(self):
        """
        This function generates the HTML-formatted stylised line contained in the Line object.
        :return: The HTML-formatted line string
        """

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

        return html_line