# -*- coding: utf-8 -*-
from flask import render_template
from homework_5.storage import BLOG_ENTRIES

def index_page():
    BE = BLOG_ENTRIES
    return render_template('index.html', BE=BE)
