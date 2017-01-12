import functools

from fakanese.phonemes import INVALID_COMBOS

@functools.total_ordering
class Syllable:

	def __init__(self):
		self._phonemes = []

	def append(self, phoneme):
		if len(self._phonemes) < 1:
			self._phonemes.append(phoneme)
			return True
		elif self._phonemes[-1] < phoneme:
			self._phonemes.append(phoneme)
			return True
		return False

	@property
	def last(self):
		return self._phonemes[-1].last
			
	@property
	def first(self):
		return self._phonemes[0].first

	def __eq__(self, other):
		# same type
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
