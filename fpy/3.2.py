from pymonad.reader import Compose
from pymonad.tools import curry


@curry(3)
def tag(tag, cls, s):

    return f'<{tag} {" ".join([f"{k}=\"{cls[k]}\"" for k in cls])}>{s}</{tag}>'

print(tag('li', {'class': 'list-group', 'tt': 'aa'}, 'item 23'))
