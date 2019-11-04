# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from homework_5.storage import BLOG_ENTRIES
import random

def create_entry_page():
    error=None
    key = str(random.randint(1,100))

    if request.method =='POST':
        title = request.form.get('title')
        text = request.form.get('text')
        if title:
            return redirect(url_for('entry_page', key=key))
        elif text:
            return render_template('entry.html',title=title, text = text)
        else:
            error = 'Необходимо ввести название или текст статьи'
    return render_template('create_entry.html', error=error)


