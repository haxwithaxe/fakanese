fakanese.py is a library for generating random human readable strings for use as IDs.

it uses the romanji style notation for japanese style sylables as the base unit of the "words".

inspired by: http://thedailywtf.com/articles/the-automated-curse-generator.aspx

example:
```
import fakanese
fakanese.get_word()
> kigode
fakanese.get_word(4)
> dafewoqy
fakanese.get_word(2, caps=True)
> BISO
```