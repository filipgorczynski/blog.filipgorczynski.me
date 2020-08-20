#!/usr/bin/env python3
import os
import re

from slugify import slugify

CONTENT_DIR = 'content'
DRAFT_RE = ''

filename_re = re.compile(r'\d+\.md')

# insensitive_title = re.compile(re.escape('title: '), re.IGNORECASE)

for filename in os.listdir(CONTENT_DIR):
    if filename_re.match(filename):
        print(f"REMOVE: {os.path.join(CONTENT_DIR, filename)} file")
        os.remove(os.path.join(CONTENT_DIR, filename))
        # slug = ''
        # oldfile = os.path.join(CONTENT_DIR, filename)
        # with open(oldfile) as infile:
        #     lines = infile.readlines()
        #     for line in lines:
        #         if line.lower().startswith("title: "):
        #             title = re.sub(r'^(?i)title: ', '', line).strip()
        #             slug = slugify(title)
        #             print(f"CHANGING {filename} :: TITLE: {title} -> SLUG: {slug}")

        #             newfile = os.path.join(CONTENT_DIR, slug + '.md')
        #             with open(newfile, 'w+') as outfile:
        #                 print(f"FILE {newfile} created")
        #                 for line in lines:
        #                     if line.lower().startswith("slug: "):
        #                         line = f"Slug: {slug}\n"
        #                     outfile.write(line)


