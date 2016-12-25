#!/usr/bin/env python3
# coding: utf-8
# Oirign : http://nafiulis.me/making-a-static-blog-with-pelican.html
# edit: ujuc
"""write

Usage:
    write new [-r | --rst] <title>
    write page [-r | --rst] <title>
    write edit <title>
    write backup <title> <date>

-d --date       datetime change

"""

import os

import kroman
import pendulum
from docopt import docopt

POST_PATH = "content/blog"
PAGE_PATH = "content/pages"


def make_entry(title, path, template):
    today = pendulum.now(tz='Asia/Seoul')

    slug = kroman.parse(title).lower().strip().replace(' ', '_')
    date = today.to_datetime_string()
    file_name = f'{path}/{today.to_date_string()}-{slug}'

    if template == 'rst':
        file_create = f'{file_name}.rst'
        hashes = '#' * len(title) * 2
        modified = ''

        article = (
            f'{title}\n'
            f'{hashes}\n\n'
            f':date: {date}\n'
            f':modified: {modified}\n'
            f':category: \n'
            f':tags: \n'
            f':slug: {slug}\n\n'
        )
    elif template == 'md':
        file_create = f'{file_name}.md'
        modified = ''

        article = (
            f'Title: {title}\n'
            f'Date: {date}\n'
            f'Modified: {modified}\n'
            f'Category: \n'
            f'Tags: \n'
            f'Slug: {slug}\n'
            f'Summary: \n\n'
        )

    if not os.path.isdir(path):
        os.mkdir(path)

    with open(file_create, 'w') as w:
        w.write(article)

    print("File created -> " + file_create)


def edit_entry(title):
    """
    title 을 가져오는데, file_path 는 동일하고 앞에 일자-제목이 붙으니
    그것까지 가져와서 변경해야되는 점이있음.
    :param title:
    :return:
    """
    pass


if __name__ == '__main__':
    opt = docopt(__doc__, version='write 1.0')

    if opt['new']:
        if opt["-r"] or opt["--rst"]:
            make_entry(opt["<title>"], POST_PATH, 'rst')
        else:
            make_entry(opt["<title>"], POST_PATH, 'md')
    elif opt['page']:
        if opt["-r"] or opt["--rst"]:
            make_entry(opt["<title>"], PAGE_PATH, 'rst')
        else:
            make_entry(opt["<title>"], PAGE_PATH, 'md')
    elif opt['edit']:
        print("edit")
    elif opt["backup"]:
        print("backup")
    else:
        print(opt)
