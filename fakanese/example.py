
from fakanese.word import Word
from fakanese.phonemes import pool



def test():
    word = Word(pool, length=5)
    print('defaults', str(word))
    print('4 syllable long', str(word.random(length=4, delimiter='.')))
    print('5 syllable long and all upper', word.upper())
    print('5 syllable long and camel case', word.camel_case())
    print('5 syllable long and inverted camel case', word.camel_case(inverse=True))
    print('5 syllable long and camel case starting with lowercase', word.camel_case(inverse=True))

if __name__ == '__main__':
    test()
