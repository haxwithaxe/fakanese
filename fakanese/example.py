
from fakanese.word import Word
from fakanese.phonemes import pool



def test():
    word = Word(pool)
    print('defaults', word.random(2, delimiter='-'))
    print('4 syllable long', word.random(4, delimiter='.'))
    print('5 syllable long and all upper', word.upper(5, delimiter='-'))
    print('5 syllable long and camel case', word.camel_case(5, delimiter='-'))
    print('5 syllable long and inverted camel case', word.camel_case(5, inverse=True))

if __name__ == '__main__':
    test()

