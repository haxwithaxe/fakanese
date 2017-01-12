

__license__ = 'GPLv3'
__author__ = 'haxwithaxe <spam@haxwithaxe.net>'
__copyright__ = 'Copyright (c) 2017 haxwithaxe'

from fakanese.word import Word
from fakanese.phonemes import pool


word = Word(pool)

def test():
    print('defaults', word.random(2, delimeter='-'))
    print('4 syllable long', word.random(4, delimeter='.'))
    print('5 syllable long and all upper', word.upper(5, delimeter='-'))
    print('5 syllable long and camel case', word.camel_case(5, delimeter='-'))
    print('5 syllable long and inverted camel case', word.camel_case(5, inverse=True))

if __name__ == '__main__':
    test()

