
import random

__license__ = 'GPLv3'

__author__ = 'haxwithaxe <me@haxwithaxe.net>'

COMPOUND_CONSONANTS = ['ch', 'sh', 'th']
# 'z' removed due to easy confusion with 's' when spoken, 'y' removed due to abiguity out of context
CONSONANTS = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x']
CONSONANT_GROUP = CONSONANTS + COMPOUND_CONSONANTS
DIPHTHONGS = ['ay', 'ew', 'oy', 'ow'] # 'y' used rather than 'i' for clarity to english speakers
VOWELS = ['a', 'i', 'o', 'u'] # 'e' removed due to abiguity out of context
VOWEL_GROUP = VOWELS + DIPHTHONGS
VOWEL = 0
CONSONANT = 1

ALL_UPPER_CASE = 1
CAMEL_CASE = 2
INVERSE_CAMEL_CASE = 3

def rand_consonant(strict=False):
	''' Get a random consonant sound from the `CONSONANT_GROUP` or if `strict` is True only from `CONSONANTS`
		@param	strict		Boolean, if True choose only from `CONSONANTS` else use `CONSONANT_GROUP`
		@return				String, consonant sound string
	'''
	if strict:
		return random.choice(CONSONANTS)
	return random.choice(CONSONANT_GROUP)

def rand_vowel(strict=False):
	''' Get a random consonant sound from the `VOWEL_GROUP` or if `strict` is True only from `VOWELS`
	    @param  strict      Boolean, if True choose only from `VOWELS` else use `VOWEL_GROUP`
		@return             String, vowel sound string
	'''
	if strict:
		return random.choice(VOWELS)
	return random.choice(VOWEL_GROUP)

def rand_char_type():
	''' Get a random selection of vowel or consonant
		@return				Int, VOWEL or CONSONANT
	'''
	return random.choice([VOWEL, CONSONANT])

def toggle_char_type(ctype):
	'''Toggle character type (VOWEL vs CONSONANT)
        @return             Int, VOWEL or CONSONANT
	'''
	if ctype == VOWEL:
		return CONSONANT
	return VOWEL

def get_char_of_type(ctype, strict=False):
	''' Get a random vowel or consonant based on ctype
        @param  strict      Boolean, see `rand_consonant()` or `rand_vowel()`
        @return             String, vowel or consonant sound string
	'''
	if ctype == VOWEL:
		return rand_vowel(strict=strict)
	return rand_consonant(strict=strict)

def rand_syllable(pos):
	''' Get a random syllable
		@param	pos		position in word. 0 is the first syllable.
	'''
	chars = []
	ctype = CONSONANT
	if pos == 0:
		ctype = rand_char_type()
	chars.append(get_char_of_type(ctype, strict=(ctype==VOWEL)))
	if ctype != VOWEL:
		chars.append(get_char_of_type(toggle_char_type(ctype)))
	return ''.join(chars)

def camel_case(syllable):
	'''Capitolize the first letter of a syllable'''
	syllable_arr = list(syllable)
	syllable_arr[0] = syllable_arr[0].upper()
	return ''.join(syllable_arr)

def inverse_camel_case(syllable):
	'''Capitolize every letter except the first in a syllable'''
	syllable_arr = list(syllable.upper())
	syllable_arr[0] = syllable_arr[0].lower()
	return ''.join(syllable_arr)

def get_word(length=3, caps=None):
	''' Get a "word" made of random syllables.
		@param	length		Int, number of syllables. default: 3
		@param	caps		Int, use capitalization method specified. default: None
		@return				String, random syllables
	'''
	word = []
	for syl_num in range(0,length):
		syllable = rand_syllable(syl_num)
		if caps == CAMEL_CASE:
			syllable = camel_case(syllable)
		elif caps == INVERSE_CAMEL_CASE:
			syllable = inverse_camel_case(syllable)
		elif caps == ALL_UPPER_CASE:
			syllable = syllable.upper()
		word.append(syllable)
	word = ''.join(word)
	return word

def test():
	print('defaults', get_word())
	print('4 syllable long', get_word(4))
	print('5 syllable long and all upper', get_word(5, caps=ALL_UPPER_CASE))
	print('5 syllable long and camel case', get_word(5, caps=CAMEL_CASE))
	print('5 syllable long and inverted camel case', get_word(5, caps=INVERSE_CAMEL_CASE))

if __name__ == '__main__':
	test()

