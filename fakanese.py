
import random
CONSONANTS = ['b','c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x']
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

def rand_cons():
	return random.choice(CONSONANTS)

def rand_vowel():
	return random.choice(VOWELS)

def rand_sylable():
		chars = []
		chars.append(rand_cons())
		chars.append(rand_vowel())
		return ''.join(chars)

def get_word(length=3, caps=False):
	word = []
	for syl_num in range(0,length):
		sylable = rand_sylable()
		word.append(sylable)
	word = ''.join(word)
	if caps: word = word.upper()
	return word

if __name__ == '__main__':
	print(get_word())
	print(get_word(4))
	print(get_word(5, caps=True))

