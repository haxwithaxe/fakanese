
import functools
import random

from fakanese.phonemes import INVALID_COMBOS


@functools.total_ordering
class Syllable:

	def __init__(self, first=False, last=False):
		self._phonemes = []
		self._is_first_syllable = first
		self._is_last_syllable = last

	@classmethod
	def random(cls, pool, first=False, last=False):
		choice = random.choice(pool)
		length = random.choice([1,2])
		syllable = cls(first=first, last=last)
		for index in range(length):
			if index == 0:
				syllable.append(choice)
				if length == 2:
					continue
				choice = random.choice(pool)
				while not syllable.append(choice):
					choice = random.choice(pool)
			else:
				while not syllable.append(choice):
					choice = random.choice(pool)
		return syllable

	def append(self, phoneme):
		if len(self._phonemes) < 1:
			self._phonemes.append(phoneme)
			return True
		else:
			requirements = self._phonemes[-1].requires
			if self._is_first_syllable and requirements.get('if_first_then_next'):
				if isinstance(phoneme, requirements.get('if_first_then_next')):
					return False
			elif not self._is_last_syllable and requirements.get('if_not_last_then_next'):
				if not isinstance(phoneme, requirements.get('if_not_last_then_next')):
					return False
			if self._phonemes[-1] < phoneme:
				self._phonemes.append(phoneme)
				return True
		return False

	@property
	def last(self):
		return self._phonemes[-1].last
			
	@property
	def first(self):
		return self._phonemes[0].first

	def __len__(self):
		return len(self._phonemes)

	def __eq__(self, other):
		return self._phonemes == other._phonemes

	def __lt__(self, other):
		if str(self.last)+str(other.first) in INVALID_COMBOS:
			# (x) 'ew' 'h'
			return False
		elif self.last < other.first:
			return True
		return False

	def __str__(self):
		return str(''.join(str(x) for x in self._phonemes))

	def __repr__(self):
		return '<%s phonemes = %s, str = "%s">' % (self.__class__.__name__, [repr(x) for x in self._phonemes], str(self))
