import sys
import datetime
from pathlib import Path

from slugify import slugify

import pelicanconf


CONTENT_PATH = Path(__file__).parent / pelicanconf.PATH


today_iso = datetime.date.today().isoformat()
now_iso = datetime.datetime.now().time().isoformat(timespec='minutes')


if len(sys.argv) > 1:
    highlights = ' '.join(sys.argv[1:])
else:
    highlights = input("Post's title: ")

title = f'{highlights}'
slug = slugify(title)


path = CONTENT_PATH / f'{today_iso}_{slug}.md'
content = f'''
Title: {title}
Date: {today_iso} {now_iso}
Category: Python
Tags:
Slug: {slug}

![Description](./images/obrazek.jpg)
[Link's text](URL)

'''.lstrip()

path.write_text(content)
