# -*- coding: utf-8 -*-
from flask import render_template
from homework_5.storage import BLOG_ENTRIES


def entry_page(key):

    for i in BLOG_ENTRIES:
        if key == i['key']:
            title = i['title']
            text = i['text']
            comments=i['comments']
    return render_template('entry.html', text=text, title=title, comments=comments)
