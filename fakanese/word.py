
from fakanese.syllable import Syllable


def _random_syllables(pool, length):
	syllables = []
	for index in range(length):
		syllable = Syllable.random(pool, first=index == 0)
		if index == 0:
			syllables.append(syllable)
		elif index > 0:
			while syllable < syllables[-1]:
				syllable = Syllable.random(pool)
			syllables.append(syllable)
	return syllables


class Word:

	def __init__(self, pool, delimiter=None, length=None):
		self._pool = pool
		self._delimiter = delimiter or ''
		self._length = length
		self._syllables = _random_syllables(self._pool, self._length)

	def with_delimiter(self, delimiter):
		return delimiter.join(str(x) for x in self._syllables)

	def camel_case(self, inverse=False, start_low=False):
		camel_cased = [str(x).title() for x in self._syllables]
		if start_low:
			camel_cased[0] = camel_cased[0].lower()
		if inverse:
			camel_cased = [x.swapcase() for x in camel_cased]
		return self._delimiter.join(camel_cased)

	def upper(self):
		return self._delimiter.join(str(x) for x in self._syllables).upper()

	def random(self, length=None, delimiter=None):
		return Word(self._pool, delimiter or self._delimiter, length or self._length)

	def __iter__(self):
		return iter(self._syllables)

	def __getitem__(self, item):
		return self._syllables[item]

	def __str__(self):
		return self._delimiter.join(str(x) for x in self._syllables)


def get_word(pool, length, delimiter=None, format=None):
	word = Word(pool, delimiter, length)
	if format.get('method') == 'upper':
		return word.upper()
	elif format.get('method') == 'camel_case':
		inverse = format.get('inverse')
		start_low = format.get('start_low')
		return word.camel_case(inverse=inverse, start_low=start_low)
	return str(word)
