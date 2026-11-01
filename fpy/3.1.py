from pymonad.reader import Compose
from pymonad.tools import curry


@curry(2)
def tag(tag, s):
    return f'<{tag}>{s}</{tag}>'

print(tag('b', 'string'))

bold = tag('b')
italic = tag('i')

print(bold('str'))
print(italic('str'))
