
import functools


INVALID_COMBOS = ('wh','gh','ei', 'ng', 'ph', 'ps', 'ts', 'yx')


@functools.total_ordering
class Character:

	def __init__(self, character, allowed_before=None):
		self._value = character
		self._allowed_before = allowed_before
		self.first = self
		self.last = self

	def __eq__(self, other):
		return self.__class__ is other.__class__ and self._value == other._value

	def __lt__(self, other):
		if isinstance(other.first, self._allowed_before):
			return True
		return False

	def __str__(self):
		return self._value

	def __repr__(self):
		return '<%s value = %s, allowed_before = "%s">' % (self.__class__.__name__, self._value, self._allowed_before)


@functools.total_ordering
class Phoneme:

	def __init__(self, *characters, allowed_before=None):
		self.characters = characters

	@property
	def last(self):
		return list(self.characters)[-1]
			
	@property
	def first(self):
		return list(self.characters)[0]

	def __eq__(self, other):
		# same type
		return self.characters == other.characters

	def __lt__(self, other):
		if str(self.last)+str(other.first) in INVALID_COMBOS:
			# (x) 'ew' 'h'
			return False
		elif self.last < other.first:
			return True
		return False

	def __str__(self):
		return str(''.join(str(x) for x in self.characters))

	def __repr__(self):
		return '<%s characters = %s, str = "%s">' % (self.__class__.__name__, [repr(x) for x in self.characters], str(self))


class PhonemeGroup:

	def __init__(self, phoneme_strings, phoneme_type):
		self.phonemes = [phoneme_type(x) for x in phoneme_strings]

	def __contains__(self, other):
		return isinstance(other, self.__class__)

	def __iter__(self):
		return iter(self.phonemes)

	def __repr__(self):
		return '<%s phonemes = %s>' % (self.__class__.__name__, self.phonemes)


class Consonant(Character):

	def __init__(self, character):
		super().__init__(character, allowed_before=Vowel)


class Diagraph(Phoneme):

	def __init__(self, characters):
		super().__init__(*[Consonant(x) for x in characters])

	def __iter__(self):
		return iter(self.phonemes)


class Dipthong(Phoneme):
	""" 'y' used rather than 'i' for clarity to English speakers"""

	def __init__(self, characters):
		super().__init__(*[Vowel(x) for x in characters])

	def __iter__(self):
		return iter(self.phonemes)


class Vowel(Character):

	def __init__(self, character):
		super().__init__(character, allowed_before=Consonant)


class Consonants(PhonemeGroup):
	# 'z' removed due to easy confusion with 's' when spoken
	# 'c', 'y', and 'q' removed due to ambiguity out of context

	def __init__(self):
		super().__init__(('b', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't',
			'v', 'w', 'x'), phoneme_type=Consonant)


class Diagraphs(PhonemeGroup):
	
	def __init__(self):
		super().__init__(('bl', 'gl', 'pl', 'sl', 'sp', 'sw'),
				phoneme_type=Diagraph)


class Dipthongs(PhonemeGroup):
	
	def __init__(self):
		super().__init__(('ay', 'oy'), phoneme_type=Dipthong)


class Vowels(PhonemeGroup):

	def __init__(self):
		super().__init__(('a', 'i', 'o', 'u'), phoneme_type=Vowel)

pool = []
pool.extend(list(Consonants()))
pool.extend(list(Diagraphs()))
pool.extend(list(Dipthongs()))
pool.extend(list(Vowels()))



