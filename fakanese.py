
import random
COMPOUND_CONSONANTS = ['ch', 'sh', 'th']
# 'z' removed due to easy confusion with 's' when spoken, 'y' removed due to abiguity out of context
CONSONANTS = ['b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x']
CONSONANT_GROUP = CONSONANTS + COMPOUND_CONSONANTS
DIPHTHONGS = ['ay', 'ew', 'oy', 'ow'] # 'y' used rather than 'i' for clarity to english speakers
VOWELS = ['a', 'i', 'o', 'u'] # 'e' removed due to abiguity out of context
VOWEL_GROUP = VOWELS + DIPHTHONGS
VOWEL = 0
CONSONANT = 1

def rand_consonant(strict=False):
	if strict:
		return random.choice(CONSONANTS)
	return random.choice(CONSONANT_GROUP)

def rand_vowel(strict=False):
	if strict:
		return random.choice(VOWELS)
	return random.choice(VOWEL_GROUP)

def rand_char_type():
	return random.choice([VOWEL, CONSONANT])

def toggle_char_type(ctype):
	if ctype == VOWEL:
		return CONSONANT
	return VOWEL

def get_char_of_type(ctype, strict=False):
	if ctype == VOWEL:
		return rand_vowel()
	return rand_consonant()

def rand_sylable(pos):
		chars = []
		ctype = CONSONANT
		if pos == 0:
			ctype = rand_char_type()
		chars.append(get_char_of_type(ctype, strict=(ctype==VOWEL)))
		if ctype != VOWEL:
			chars.append(get_char_of_type(toggle_char_type(ctype)))
		return ''.join(chars)

def get_word(length=3, caps=False):
	word = []
	for syl_num in range(0,length):
		sylable = rand_sylable(syl_num)
		word.append(sylable)
	word = ''.join(word)
	if caps:
		word = word.upper()
	return word

if __name__ == '__main__':
	print(get_word())
	print(get_word(4))
	print(get_word(5, caps=True))

