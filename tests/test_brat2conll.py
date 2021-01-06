from os import remove
from brat2CoNLL.format_convertor import FormatConvertor
# Ensure that the package is on your python path for it to be imported correctly


def test_brat2conll():
    input_dir = '../sample_input_data/'
    output_file = '../sample_output_data/test.txt'
    verification_file = '../sample_output_data/verification.txt'
    format_convertor = FormatConvertor(input_dir, output_file)
    format_convertor.parse_text()
    with open(output_file, 'r') as fi:
        test = fi.read()
    with open(verification_file, 'r') as fi:
        verification = fi.read()

    remove(output_file)
    assert verification == test
    