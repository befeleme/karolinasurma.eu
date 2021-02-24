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

is_draft = input("Place to drafts? Y/N: ")
if is_draft.lower() == "y":
    path = CONTENT_PATH / "drafts" / f'{today_iso}_{slug}.md'
else:
    path = CONTENT_PATH / f'{today_iso}_{slug}.md'

content = f'''
Title: {title}
Date: {today_iso} {now_iso}
Category:
Tags: EN
Slug: {slug}

## Accomplishments
## Last week I learned
## Plans and hopes


![Description](./images/obrazek.jpg)
[Link's text](URL)

'''.lstrip()

path.write_text(content)
