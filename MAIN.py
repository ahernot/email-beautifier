import subprocess

import basic_functions as BFunc
from objects import Char, Word, Line

__OPERATING_SYSTEM__ = 'macOS'
__MESSAGES__ = True
_psep_ = '/'
_esep_ = '.'




def stylise(text:str) -> str:
    """
    This function randomly stylises any text using HTML/CSS beacons.
    :param text: The text to stylise
    :return: The HTML-formatted stylised text
    """
    html_text = ''

    for line in BFunc.split_many(text):
        line_obj = Line(line)
        html_text += line_obj.generate_html()

    return html_text



def convert(input_file_path: str):
    """
    This function generates an HTML stylised file from a raw TXT file.
    :param input_file_path: the path to the TXT file to process
    :return:
    """

    #   1. Getting the text to convert
    with open(input_file_path, 'r', encoding='utf-8') as txt_input:
        text = txt_input.read()

    #   2. Stylising the text
    html_text = stylise(text)

    #   3. Generating the output file's path
    output_dir = '/'.join(input_file_path.split(_psep_)[:-1]) + '/'
    file_name_full_split = input_file_path.split(_psep_)[-1].split(_esep_)
    file_name = '.'.join(file_name_full_split[:-1])
    output_path = output_dir + file_name + '.html'

    #   4. Saving the output HTML file
    with open(output_path, 'w', encoding='utf-8') as html_output:
        html_output.write(html_text)
    if __MESSAGES__: print(f'File saved at location {output_path}')

    #   5. Copying the output to the clipboard (macOS only)
    if __OPERATING_SYSTEM__ == 'macOS':
        process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
        process.communicate(html_text.encode('utf-8'))

        if __MESSAGES__: print('HTML-formatted text successfully copied to clipboard.')

# Usage:
# convert('/Desktop/sample_message.txt')