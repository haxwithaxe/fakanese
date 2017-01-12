
from fakanese import word



if __name__ == '__main__':
    print('defaults', word.random(2, delimeter='-'))
    print('4 syllable long', word.random(4, delimeter='.'))
    print('5 syllable long and all upper', word.upper(5, delimeter='-'))
    print('5 syllable long and camel case', word.camel_case(5, delimeter='-'))
    print('5 syllable long and inverted camel case', word.camel_case(5, inverse=True))

