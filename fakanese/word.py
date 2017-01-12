
import random

from fakanese.syllable import Syllable

class Word:

	def __init__(self, pool, delimeter=None, length=None):
		self._pool = pool
		self._delimeter = delimeter or ''
		self._length = length

	def __get_delimeter(self, delimeter):
		if isinstance(delimeter, str):
			return delimeter
		return self._delimeter

	def __get_length(self, length):
		if isinstance(length, int):
			return length
		return self._length

	def _get_word(self, delimeter, length):
		return _Word(self._pool, delimeter=self.__get_delimeter(delimeter), length=self.__get_length(length))

	def camel_case(self, length, delimeter=None, inverse=False, start_low=False):
		word = self._get_word(delimeter, length)
		if start_low:
			word[0] = str(word[0]).lower()
		camel_cased = str(word)
		if inverse:
			return camel_cased.swapcase()
		return camel_cased

	def upper(self, length, delimeter=None):
		word = self._get_word(delimeter, length)
		return str(word).upper()

	def random(self, length, delimeter=None):
		word = self._get_word(delimeter, length)
		return str(word)



class _Word:

	def __init__(self, pool, delimeter, length):
		self._syllables = []
		self._pool = pool
		self._delimeter = delimeter
		self._length = length
		self._generate_random()

	def _generate_random(self):
		for index in range(self._length):
			syllable = self._random_syllable()
			self._syllables.append(syllable)

	def _random_syllable(self):
		choice = random.choice(self._pool)
		syllable_length = random.choice([1,2])
		syllable = Syllable()
		for index in range(syllable_length):
			if len(self) > 0:
				while self[-1] >= choice:
					choice = random.choice(self._pool)
			if index == 0:
				syllable.append(choice)
			else:
				while not syllable.append(choice):
					choice = random.choice(self._pool)
		return syllable

	def __len__(self):
		return len(self._syllables)

	def __iter__(self):
		return iter(self._syllables)

	def __getitem__(self, index):
		return self._syllables[index]

	def __setitem__(self, index, value):
		self._syllables[index] = value

	def __str__(self):
		return self._delimeter.join([str(x) for x in self._syllables])
